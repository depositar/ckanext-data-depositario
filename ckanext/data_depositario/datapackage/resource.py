from __future__ import annotations

from typing import Optional

from dplib.models import Resource
from dplib.plugins.ckan.models.package import CkanResource


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
