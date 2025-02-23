# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

from c7n_tencentcloud.provider import resources
from c7n_tencentcloud.query import ResourceTypeInfo, QueryResourceManager
from c7n_tencentcloud.utils import PageMethod


@resources.register("tag")
class TAG(QueryResourceManager):
    """TAG"""

    class resource_type(ResourceTypeInfo):
        """resource_type"""
        endpoint = "tag.tencentcloudapi.com"
        service = "tag"
        version = "2018-08-13"
        taggable = True
        enum_spec = ("GetResources",
                     "Response.ResourceTagMappingList[]",
                     {}
                     )
        paging_def = {
            "method": PageMethod.PaginationToken,
            "pagination_token_path": "Response.PaginationToken",
            "limit": {
                "Key": "MaxResults",
                "value": 200
            }
        }

    def get_resource_query_params(self):
        """
        get_resource_query_params
        param format:
        {
            "ResourceList": ["", ""],
            "TagFilters": [{
                "TagKey": "",
                "TagValue": ["", ""]
            }]
        }
        """
        return self.data.get("query", {})

    @staticmethod
    def get_simple_call_params(resource6_name):
        """
        get_simple_call_params
        """
        params = {
            "ResourceList": [resource6_name]
        }
        params.update()
        return params
