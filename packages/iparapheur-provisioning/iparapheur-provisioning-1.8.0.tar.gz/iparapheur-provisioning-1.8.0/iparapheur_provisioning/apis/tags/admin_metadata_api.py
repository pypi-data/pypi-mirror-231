# coding: utf-8

"""
    iparapheur

    iparapheur v5.x main core application.  The main link between every sub-services, integrating business code logic.   # noqa: E501

    The version of the OpenAPI document: DEVELOP
    Contact: iparapheur@libriciel.coop
    Generated by: https://openapi-generator.tech
"""

from iparapheur_provisioning.paths.api_provisioning_v1_admin_tenant_tenant_id_metadata.post import CreateMetadata
from iparapheur_provisioning.paths.api_provisioning_v1_admin_tenant_tenant_id_metadata_metadata_id.delete import DeleteMetadata
from iparapheur_provisioning.paths.api_provisioning_v1_admin_tenant_tenant_id_metadata_metadata_id.get import GetMetadata
from iparapheur_provisioning.paths.api_provisioning_v1_admin_tenant_tenant_id_metadata.get import ListMetadata
from iparapheur_provisioning.paths.api_provisioning_v1_admin_tenant_tenant_id_metadata_metadata_id.put import UpdateMetadata


class AdminMetadataApi(
    CreateMetadata,
    DeleteMetadata,
    GetMetadata,
    ListMetadata,
    UpdateMetadata,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
