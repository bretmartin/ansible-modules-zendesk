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

    macros = []

    for macro in client.macros_list()['macros']:
        action_dicts = []
        for action in macro['actions']:
            action_dict = {action['field']: action['value']}
            action_dicts.append(action_dict)
        macro['actions'] = action_dicts
        macros.append(macro)

    result['macros'] = macros

    module.exit_json(**result)


if __name__ == '__main__':
    main()
