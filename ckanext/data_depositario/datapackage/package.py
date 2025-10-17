from __future__ import annotations

import json
from typing import List, Optional

from dplib.models import Package
from dplib.plugins.ckan.models.package import CkanPackage

from ckanext.data_depositario.datapackage.resource import DepositarCkanResource
from ckanext.data_depositario.datapackage.resource import DepositarDPResource


class DepositarDPPackage(Package):
    """Depositar Data Package model"""

    data_type: List[str] = []
    wd_keywords: List[str] = []
    language: List[str] = []
    remarks: Optional[str] = None
    temp_res: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    spatial: Optional[dict] = None
    x_min: Optional[float] = None
    x_max: Optional[float] = None
    y_min: Optional[float] = None
    y_max: Optional[float] = None
    spatial_res: Optional[float] = None
    created_time: Optional[str] = None
    process_step: Optional[str] = None
    contact_person: Optional[str] = None
    contact_email: Optional[str] = None


class DepositarCkanPackage(CkanPackage):
    """Depositar CKAN Package model"""

    resources: List[DepositarCkanResource] = []

    data_type: List[str] = []
    keywords: List[str] = []
    language: List[str] = []
    remarks: Optional[str] = None
    temp_res: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    spatial: Optional[str] = None
    x_min: Optional[str] = None
    x_max: Optional[str] = None
    y_min: Optional[str] = None
    y_max: Optional[str] = None
    spatial_res: Optional[str] = None
    created_time: Optional[str] = None
    process_step: Optional[str] = None
    contact_person: Optional[str] = None
    contact_email: Optional[str] = None

    # Converters

    def to_dp(self) -> Package:
        """Convert to Data Package

        Returns:
           Data Package
        """
        package = super().to_dp()

        if self.data_type:
            package.data_type = self.data_type

        if self.keywords:
            wd_keywords = \
                [f"http://www.wikidata.org/entity/{keyword}"
                 for keyword in self.keywords]
            package.wd_keywords = wd_keywords

        if self.language:
            package.language = self.language

        if self.remarks:
            package.remarks = self.remarks

        if self.temp_res:
            package.temp_res = self.temp_res

        if self.start_time:
            package.start_time = self.start_time

        if self.end_time:
            package.end_time = self.end_time

        if self.spatial:
            package.spatial = json.loads(self.spatial)

        if self.x_min:
            package.x_min = float(self.x_min)

        if self.x_max:
            package.x_max = float(self.x_max)

        if self.y_min:
            package.y_min = float(self.y_min)

        if self.y_max:
            package.y_max = float(self.y_max)

        if self.spatial_res:
            package.spatial_res = float(self.spatial_res)

        if self.created_time:
            package.created_time = self.created_time

        if self.process_step:
            package.process_step = self.process_step

        if self.contact_person:
            package.contact_person = self.contact_person

        if self.contact_email:
            package.contact_email = self.contact_email

        sources_path = f"https://data.depositar.io/dataset/{self.name}"

        if hasattr(self, "ark"):
            package.id = f"https://n2t.net/{self.ark}"
            sources_path = package.id

        package.sources = [{
            "title": "depositar",
            "path": sources_path,
            "email": "data.contact@depositar.io"
        }]

        package.custom["$schema"] = \
            "https://raw.githubusercontent.com/depositar/" \
            "ckanext-data-depositario/master/depositar-dp/1.0.0/" \
            "depositar-dp-profile.json"

        # Resources
        package.resources = []
        for index, item in enumerate(self.resources, start=1):
            resource = item.to_dp()

            # Override dplib-py to avoid slugification
            # - https://github.com/frictionlessdata/dplib-py/
            # blob/v1.1.0/dplib/plugins/ckan/models/resource.py#L35
            resource.name = f"resource_{str(index)}"

            package.resources.append(resource)

        return package

    @classmethod
    def from_dp(cls, package: DepositarDPPackage) -> CkanPackage:
        """Create a CKAN Package from Data Package

        Parameters:
            package: Data Package

        Returns:
            CKAN Package
        """
        ckan = super().from_dp(package)

        if package.data_type:
            ckan.data_type = package.data_type

        if package.wd_keywords:
            keywords = [keyword.split("/")[-1] for keyword in package.wd_keywords]
            ckan.keywords = keywords

        if package.language:
            ckan.language = package.language

        if package.remarks:
            ckan.remarks = package.remarks

        if package.temp_res:
            ckan.temp_res = package.temp_res

        if package.start_time:
            ckan.start_time = package.start_time

        if package.end_time:
            ckan.end_time = package.end_time

        if package.spatial:
            ckan.spatial = json.dumps(package.spatial)

        if package.x_min:
            ckan.x_min = str(package.x_min)

        if package.x_max:
            ckan.x_max = str(package.x_max)

        if package.y_min:
            ckan.y_min = str(package.y_min)

        if package.y_max:
            ckan.y_max = str(package.y_max)

        if package.spatial_res:
            ckan.spatial_res = str(package.spatial_res)

        if package.created_time:
            ckan.created_time = package.created_time

        if package.process_step:
            ckan.process_step = package.process_step

        if package.contact_person:
            ckan.contact_person = package.contact_person

        if package.contact_email:
            ckan.contact_email = package.contact_email

        # Resources
        ckan.resources = []
        for resource in package.resources:
            depositar_resource = DepositarDPResource(**resource.model_dump())
            item = DepositarCkanResource.from_dp(depositar_resource)
            if item:
                ckan.resources.append(item)

        return ckan
