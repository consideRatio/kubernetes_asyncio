# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.22.6
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.apis_api import ApisApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestApisApi(unittest.TestCase):
    """ApisApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.apis_api.ApisApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_versions(self):
        """Test case for get_api_versions

        """
        pass


if __name__ == '__main__':
    unittest.main()
