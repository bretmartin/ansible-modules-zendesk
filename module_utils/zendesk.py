#!/usr/bin/env python

from zdesk import Zendesk


def zendesk_api_client(module):
    return Zendesk(
        zdesk_url=module.params.get('url'),
        zdesk_email=module.params.get('username'),
        zdesk_api=module.params.get('token'),
    )


def zendesk_argument_spec():
    return dict(
        url=dict(type='str', required=True),
        username=dict(type='str', required=True),
        token=dict(type='str', required=True, no_log=True),
    )
