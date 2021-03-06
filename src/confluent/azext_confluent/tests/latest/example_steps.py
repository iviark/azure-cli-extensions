# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /MarketplaceAgreements/get/MarketplaceAgreements_List
@try_manual
def step_terms_list(test, rg, checks=None):  # pylint: disable=unused-argument
    if checks is None:
        checks = []
    test.cmd('az confluent terms list',
             checks=checks)


# EXAMPLE: /Organization/put/Organization_Create
@try_manual
def step_organization_create(test, rg, checks=None):  # pylint: disable=unused-argument
    if checks is None:
        checks = []
    test.cmd('az confluent organization create '
             '--location "eastus2euap" '
             '--offer-detail id="confluent-cloud-azure-stag" plan-id="confluent-cloud-azure-payg-stag" '
             'plan-name="Confluent Cloud - Pay as you Go" publisher-id="confluentinc" term-unit="P1M" '
             '--user-detail email-address="contoso@microsoft.com" first-name="contoso" last-name="zhou" '
             '--tags environment="Dev" '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=checks)
    test.cmd('az confluent organization wait --created '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Organization/get/Organization_Get
@try_manual
def step_organization_show(test, rg, checks=None):  # pylint: disable=unused-argument
    if checks is None:
        checks = []
    test.cmd('az confluent organization show '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Organization/get/Organization_ListByResourceGroup
@try_manual
def step_organization_list(test, rg, checks=None):  # pylint: disable=unused-argument
    if checks is None:
        checks = []
    test.cmd('az confluent organization list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Organization/patch/Confluent_Update
@try_manual
def step_organization_update(test, rg, checks=None):  # pylint: disable=unused-argument
    if checks is None:
        checks = []
    test.cmd('az confluent organization update '
             '--tags client="dev-client" env="dev" '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Organization/delete/Confluent_Delete
@try_manual
def step_organization_delete(test, rg, checks=None):  # pylint: disable=unused-argument
    if checks is None:
        checks = []
    test.cmd('az confluent organization delete -y '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=checks)
