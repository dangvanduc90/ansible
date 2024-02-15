import subprocess

from ansible.errors import AnsibleParserError
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import combine_vars


class VarsModule(BaseVarsPlugin):

    def get_vars(self, loader, path, entities):
        ''' Lookup become password '''

        if not isinstance(entities, list):
            entities = [entities]

        super(VarsModule, self).get_vars(loader, path, entities)

        data = {}
        for entity in entities:
            cmd = ''

            if isinstance(entity, Host):
                try:
                    cmd = self.get_option('host_command')
                except (KeyError, AttributeError):
                    self._display.v(
                        'znerol.become_password.command host_command '
                        'not configured'
                    )

            elif isinstance(entity, Group):
                try:
                    cmd = self.get_option('group_command')
                except (KeyError, AttributeError):
                    self._display.v(
                        'znerol.become_password.command group_command '
                        'not configured'
                    )

            else:
                raise AnsibleParserError(
                    'Supplied entity must be Host or Group, got %s instead' %
                    (type(entity))
                )

            if (cmd):
                argv = [cmd, str(entity)]

                try:
                    stdout = subprocess.check_output(
                        argv,
                        cwd=self._basedir,
                    )

                except Exception as e:
                    raise AnsibleParserError(to_native(e))

                password = to_text(stdout).rstrip('\r\n')

                if password:
                    data = combine_vars(data, {
                        'ansible_become_password': password,
                    })

        return data
