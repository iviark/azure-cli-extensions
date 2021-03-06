# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddServicePrincipalIdentityDetails(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.service_principal_identity_details = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'application-id':
                d['application_id'] = v[0]
            elif kl == 'object-id':
                d['object_id'] = v[0]
            elif kl == 'audience':
                d['audience'] = v[0]
            elif kl == 'aad-authority':
                d['aad_authority'] = v[0]
            elif kl == 'raw-cert-data':
                d['raw_cert_data'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter service_principal_identity_details. All '
                               'possible keys are: tenant-id, application-id, object-id, audience, aad-authority, '
                               'raw-cert-data'.format(k))
        return d


class AddAgentDetails(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.agent_details = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'key-vault-uri':
                d['key_vault_uri'] = v[0]
            elif kl == 'key-vault-id':
                d['key_vault_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter agent_details. All possible keys are: '
                               'key-vault-uri, key-vault-id'.format(k))
        return d
