# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import MySQLManagementClientConfiguration
from .operations import ServersOperations
from .operations import ReplicasOperations
from .operations import ServerKeysOperations
from .operations import FirewallRulesOperations
from .operations import DatabasesOperations
from .operations import ConfigurationsOperations
from .operations import LocationBasedCapabilitiesOperations
from .operations import CheckVirtualNetworkSubnetUsageOperations
from .operations import CheckNameAvailabilityOperations
from .operations import Operations
from . import models


class MySQLManagementClient(SDKClient):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, log files and configurations with new business model.

    :ivar config: Configuration for client.
    :vartype config: MySQLManagementClientConfiguration

    :ivar servers: Servers operations
    :vartype servers: azure.mgmt.rdbms.mysql_flexibleservers.operations.ServersOperations
    :ivar replicas: Replicas operations
    :vartype replicas: azure.mgmt.rdbms.mysql_flexibleservers.operations.ReplicasOperations
    :ivar server_keys: ServerKeys operations
    :vartype server_keys: azure.mgmt.rdbms.mysql_flexibleservers.operations.ServerKeysOperations
    :ivar firewall_rules: FirewallRules operations
    :vartype firewall_rules: azure.mgmt.rdbms.mysql_flexibleservers.operations.FirewallRulesOperations
    :ivar databases: Databases operations
    :vartype databases: azure.mgmt.rdbms.mysql_flexibleservers.operations.DatabasesOperations
    :ivar configurations: Configurations operations
    :vartype configurations: azure.mgmt.rdbms.mysql_flexibleservers.operations.ConfigurationsOperations
    :ivar location_based_capabilities: LocationBasedCapabilities operations
    :vartype location_based_capabilities: azure.mgmt.rdbms.mysql_flexibleservers.operations.LocationBasedCapabilitiesOperations
    :ivar check_virtual_network_subnet_usage: CheckVirtualNetworkSubnetUsage operations
    :vartype check_virtual_network_subnet_usage: azure.mgmt.rdbms.mysql_flexibleservers.operations.CheckVirtualNetworkSubnetUsageOperations
    :ivar check_name_availability: CheckNameAvailability operations
    :vartype check_name_availability: azure.mgmt.rdbms.mysql_flexibleservers.operations.CheckNameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.mysql_flexibleservers.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MySQLManagementClientConfiguration(credentials, subscription_id, base_url)
        super(MySQLManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-07-01-privatepreview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.server_keys = ServerKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.location_based_capabilities = LocationBasedCapabilitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.check_virtual_network_subnet_usage = CheckVirtualNetworkSubnetUsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
