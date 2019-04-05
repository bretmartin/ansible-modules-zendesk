#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.zendesk \
    import zendesk_api_client, zendesk_argument_spec


def main():
    module = AnsibleModule(
        argument_spec=zendesk_argument_spec(),
        supports_check_mode=True,
    )

    result = {'changed': False}

    client = zendesk_api_client(module)

    result['macros'] = client.macros_list()['macros']

    module.exit_json(**result)


if __name__ == '__main__':
    main()
