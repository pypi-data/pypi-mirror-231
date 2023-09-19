# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import iparapheur_provisioning
from iparapheur_provisioning.paths.api_provisioning_v1_admin_tenant_tenant_id_typology_type_type_id_subtype_subtype_id import delete  # noqa: E501
from iparapheur_provisioning import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiProvisioningV1AdminTenantTenantIdTypologyTypeTypeIdSubtypeSubtypeId(ApiTestMixin, unittest.TestCase):
    """
    ApiProvisioningV1AdminTenantTenantIdTypologyTypeTypeIdSubtypeSubtypeId unit test stubs
        Delete a subtype  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
