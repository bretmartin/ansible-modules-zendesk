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

    result['triggers'] = client.triggers_list()['triggers']

    result['groups'] = {}
    for trigger in result['triggers']:
        for action in trigger['actions']:

            if action['field'] == 'group_id':
                group = client.group_show(id=action['value'])
                result['groups'][action['value']] = group['group']['name']

        for condition_type in ['all', 'any']:
            condition_strings = []
            for condition in trigger['conditions'][condition_type]:
                condition_string = '%s %s %s' % (condition['field'], condition['operator'], condition['value'])
                condition_strings.append(condition_string)
            trigger['conditions'][condition_type] = condition_strings

    module.exit_json(**result)


if __name__ == '__main__':
    main()
