from __future__ import annotations

from typing import Optional

from dplib.models import Resource
from dplib.plugins.ckan.models.package import CkanResource


class DepositarDPResource(Resource):
    """Depositar CKAN Data Resource model"""

    encoding: Optional[str] = None
    resource_crs: Optional[int] = None


class DepositarCkanResource(CkanResource):
    """Depositar CKAN Resource model"""

    encoding: Optional[str] = None
    resource_crs: Optional[int] = None

    # Converters

    def to_dp(self) -> Resource:
        """Convert to Data Package resource

        Returns:
           Data Resource
        """
        resource = super().to_dp()

        resource.title = self.name

        if self.encoding:
            resource.encoding = self.encoding

        if self.resource_crs:
            resource.resource_crs = self.resource_crs

        return resource

    @classmethod
    def from_dp(cls, resource: DepositarDPResource) -> Optional[CkanResource]:
        """Create CKAN Resource from Data Resource

        Parameters:
            resource: Data Resource

        Returns:
            CKAN Resource
        """
        ckan = super().from_dp(resource)

        if resource.title:
            ckan.name = resource.title

        if resource.encoding:
            ckan.encoding = resource.encoding

        if resource.resource_crs:
            ckan.resource_crs = resource.resource_crs

        return ckan
