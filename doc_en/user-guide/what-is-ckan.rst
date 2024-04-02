-------------
What is CKAN?
-------------

CKAN is a tool for making open data websites. (Think of a content management
system like WordPress - but for data, instead of pages and blog posts.) It
helps you manage and publish collections of data. It is used by national and
local governments, research institutions, and other organizations who collect a
lot of data. |site_name| is built with CKAN.

Once your data is published, users can use its faceted search features to
browse and find the data they need, and preview it using maps, graphs and
tables - whether they are developers, journalists, researchers, NGOs, citizens,
or even your own staff.

Datasets and resources
======================

For CKAN purposes, data is published in units called "datasets". A dataset is a
parcel of data - for example, it could be the crime statistics for a region,
the spending figures for a government department, or temperature readings from
various weather stations. When users search for data, the search results they
see will be individual datasets.

A dataset contains two things:

* Information or "metadata" about the data. For example, the title and
  publisher, date, what formats it is available in, what license it is released
  under, etc.

* A number of "resources", which hold the data itself. CKAN does not mind what
  format the data is in. A resource can be a CSV or Excel spreadsheet, XML file,
  PDF document, image file, linked data in RDF format, etc. CKAN can store the
  resource internally, or store it simply as a link, the resource itself being
  elsewhere on the web. A dataset can contain any number of resources. For
  example, different resources might contain the data for different years, or
  they might contain the same data in different formats.
