from rdflib import URIRef, BNode, Literal
from rdflib.namespace import Namespace, RDF, XSD, DC, RDFS, SKOS, FOAF, DCTERMS

from ckantoolkit import config

from ckan.lib.helpers import markdown_extract

from ckanext.dcat.utils import resource_uri
from ckanext.dcat.profiles import RDFProfile, CleanedURIRef

DCAT = Namespace("http://www.w3.org/ns/dcat#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
SCHEMA = Namespace("http://schema.org/")
LOCN = Namespace("http://www.w3.org/ns/locn#")
WD = Namespace("http://www.wikidata.org/entity/")
ORG = Namespace("http://www.w3.org/ns/org#")
CNT = Namespace("http://www.w3.org/2011/content#")

IMT_PREFIX = "https://www.iana.org/assignments/media-types/"
GEOJSON_IMT = IMT_PREFIX + "application/vnd.geo+json"
LANG_PREFIX = "http://www.lexvo.org/page/iso639-3/"
DATA_TYPE_PREFIX = "http://registry.it.csiro.au/def/re3data/contentType/_"
EPSG_PREFIX = "http://www.opengis.net/def/crs/EPSG/0/"

namespaces = {
    "dct": DCTERMS,
    "dcat": DCAT,
    "vcard": VCARD,
    "foaf": FOAF,
    "schema": SCHEMA,
    "skos": SKOS,
    "locn": LOCN,
    "xsd": XSD,
    "dc": DC,
    "org": ORG,
    "wd": WD,
    "cnt": CNT
}

class DCATProfile(RDFProfile):
    '''
    An RDF profile based on DCAT for depositar
    '''

    def graph_from_dataset(self, dataset_dict, dataset_ref):

        g = self.g

        for prefix, namespace in namespaces.items():
            g.bind(prefix, namespace)

        # Dataset

        g.add((dataset_ref, RDF.type, DCAT.Dataset))

        ## Simple values
        items = [
            ("title", DCTERMS.title, None, Literal),
            ("name", DCTERMS.identifier, None, Literal),
            ("author", DC.creator, None, Literal),
        ]
        self._add_triples_from_dict(dataset_dict, dataset_ref, items)

        ## Description
        dataset_desc = dataset_dict.get("notes")
        if dataset_desc:
            dataset_desc_value = markdown_extract(dataset_desc, extract_length=0)
        g.add((dataset_ref, DCTERMS.description,
               Literal(dataset_desc)))

        ## Language
        langs = dataset_dict.get("language")
        if langs:
            for lang in langs:
                language_uri = LANG_PREFIX + lang
                g.add((dataset_ref, DCTERMS.language, URIRef(language_uri)))

        ## Tags
        for tag in dataset_dict.get("tags", []):
            g.add((dataset_ref, DCAT.keyword, Literal(tag["name"])))

        ## Wikidata keywords
        for keyword in dataset_dict.get("keywords", []):
            g.add((dataset_ref, DCAT.theme, WD[keyword]))

        ## Data Type
        data_types = dataset_dict.get("data_type")
        if data_types:
            for data_type in data_types:
                g.add((dataset_ref, DCTERMS.type,
                       URIRef(DATA_TYPE_PREFIX + data_type)))

        ## Temporal Resolution
        temp_res = dataset_dict.get("temp_res")
        temp_res_mapping = {"yearly": "P1Y", "daily": "P1D", "monthly": "P1M"}
        if temp_res:
            temp_res_value = temp_res_mapping[temp_res]
            g.add((dataset_ref, DCAT.temporalResolution,
                    Literal(temp_res_value, datatype=XSD.duration)))

        ## Start Time, End Time, and Created Time
        items = [
            ("start_time", SCHEMA.startDate, None, Literal),
            ("end_time", SCHEMA.endDate, None, Literal),
            ("created_time", DCTERMS.issued, None, Literal)
        ]
        self._add_date_triples_from_dict(dataset_dict, dataset_ref, items)

        ## Spatial Coverage
        spatial = dataset_dict.get("spatial")
        x_min = dataset_dict.get("x_min")
        x_max = dataset_dict.get("x_max")
        y_min = dataset_dict.get("y_min")
        y_max = dataset_dict.get("y_max")

        if any([spatial, x_min, x_max, y_min, y_max]):
            spatial_ref = BNode()
            g.add((spatial_ref, RDF.type, DCTERMS.Location))
            g.add((dataset_ref, DCTERMS.spatial, spatial_ref))

            if spatial:
                g.add((spatial_ref, LOCN.geometry, Literal(spatial, datatype=GEOJSON_IMT)))

            if x_min and x_max and y_min and y_max:
                box_value = "%s %s %s %s" % (y_min, x_min, y_max, x_max)
                box_ref = BNode()
                g.add((box_ref, RDF.type, SCHEMA.GeoShape))
                g.add((box_ref, SCHEMA.box, Literal(box_value)))
                g.add((spatial_ref, LOCN.geometry, box_ref))

        ## Spatial Resolution
        spatial_res = dataset_dict.get("spatial_res")

        if spatial_res:
           g.add((dataset_ref, DCAT.spatialResolutionInMeters,
                    Literal(spatial_res, datatype=XSD.decimal)))

        ## Process Step
        proc_step = dataset_dict.get("process_step")

        if proc_step:
            proc_step_value = markdown_extract(proc_step, extract_length=0)
            proc_ref = BNode()
            g.add((proc_ref, RDF.type, DCTERMS.ProvenanceStatement))
            g.add((proc_ref, RDFS.label, Literal(proc_step_value)))
            g.add((dataset_ref, DCTERMS.provenance, proc_ref))

        ## Project details
        project = dataset_dict.get("organization")

        if project:
            project["description"] = markdown_extract(project["description"],
                                                extract_length=0)
            project_details = BNode()
            g.add((project_details, RDF.type, ORG.Organization))
            g.add((dataset_ref, DCTERMS.publisher, project_details))
            items = [
                ("title", FOAF.name, None, Literal),
                ("description", ORG.purpose, None, Literal)
            ]

            self._add_triples_from_dict(project, project_details, items)

        ## Contact details
        contact_person = dataset_dict.get("contact_person")
        contact_email = dataset_dict.get("contact_email")

        if any([contact_person, contact_email]):
            contact_details = BNode()
            g.add((contact_details, RDF.type, VCARD.Individual))
            g.add((dataset_ref, DCAT.contactPoint, contact_details))

            self._add_triple_from_dict(
                dataset_dict, contact_details,
                VCARD.fn, "contact_person"
            )

            self._add_triple_from_dict(
                dataset_dict, contact_details,
                VCARD.hasEmail, "contact_email",
                _type=URIRef, value_modifier=self._add_mailto
            )

        ## Theme
        themes = dataset_dict.get("groups")

        if themes:
            for theme in themes:
                theme_details = BNode()
                g.add((theme_details, RDF.type, SKOS.Concept))
                g.add((theme_details, SKOS.prefLabel, Literal(theme["title"])))
                g.add((dataset_ref, DCAT.theme, theme_details))

        # Resources

        ## Depositar defines license in the dataset level
        license = dataset_dict.get("license_url")

        for resource_dict in dataset_dict.get("resources", []):
            distribution = CleanedURIRef(resource_uri(resource_dict))

            g.add((dataset_ref, DCAT.distribution, distribution))

            g.add((distribution, RDF.type, DCAT.Distribution))

            ## Simple values
            items = [
                ("name", DCTERMS.title, None, Literal),
                ("description", DCTERMS.description, None, Literal),
                ("encoding", CNT.characterEncoding, None, Literal),
                ("url", DCAT.downloadURL, None, URIRef),
            ]
            self._add_triples_from_dict(resource_dict, distribution, items)

            ## License
            if license:
                g.add((distribution, DCTERMS.license, URIRef(license)))

            ## Coordinate Systems
            crs = resource_dict.get("resource_crs")

            if crs:
                crs_value = EPSG_PREFIX + str(crs)
                g.add((distribution, DCTERMS.conformsTo, URIRef(crs_value)))

            ## Format (mimetype)
            mimetype = resource_dict.get("mimetype")

            if mimetype:
                mimetype_value = IMT_PREFIX + mimetype
                g.add((distribution, DCAT.mediaType, URIRef(mimetype_value)))

    def graph_from_catalog(self, catalog_dict, catalog_ref):

        g = self.g

        for prefix, namespace in namespaces.items():
            g.bind(prefix, namespace)

        g.add((catalog_ref, RDF.type, DCAT.Catalog))

        # Basic fields
        items = [
            ("title", DCTERMS.title, config.get("ckan.site_title"), Literal),
            ("homepage", FOAF.homepage, config.get("ckan.site_url"), URIRef),
            ("language", DCTERMS.language, LANG_PREFIX + "zho", URIRef),
        ]
        for item in items:
            key, predicate, fallback, _type = item
            if catalog_dict:
                value = catalog_dict.get(key, fallback)
            else:
                value = fallback
            if value:
                g.add((catalog_ref, predicate, _type(value)))

        # Dates
        modified = self._last_catalog_modification()
        if modified:
            self._add_date_triple(catalog_ref, DCTERMS.modified, modified)
