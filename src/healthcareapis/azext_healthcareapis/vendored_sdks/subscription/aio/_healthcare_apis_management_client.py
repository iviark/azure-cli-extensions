# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import HealthcareApisManagementClientConfiguration
from .operations import ServiceOperations
from .operations import OperationOperations
from .operations import OperationResultOperations
from .operations import PrivateEndpointConnectionOperations
from .operations import PrivateLinkResourceOperations
from .. import models


class HealthcareApisManagementClient(object):
    """Azure Healthcare APIs Client.

    :ivar service: ServiceOperations operations
    :vartype service: healthcare_apis_management_client.aio.operations.ServiceOperations
    :ivar operation: OperationOperations operations
    :vartype operation: healthcare_apis_management_client.aio.operations.OperationOperations
    :ivar operation_result: OperationResultOperations operations
    :vartype operation_result: healthcare_apis_management_client.aio.operations.OperationResultOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection: healthcare_apis_management_client.aio.operations.PrivateEndpointConnectionOperations
    :ivar private_link_resource: PrivateLinkResourceOperations operations
    :vartype private_link_resource: healthcare_apis_management_client.aio.operations.PrivateLinkResourceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = HealthcareApisManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_result = OperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resource = PrivateLinkResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "HealthcareApisManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
