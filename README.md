`vagrant up`

copy noi dung file hosts vao day
vi /etc/ansible/hosts


run command duoi de xuat file ssh config
`vagrant ssh-config > vagrant-ssh`

copy noi dung file vagrant-ssh vaof ~/.ssh/config

### Check your syntax before running
`ansible-playbook --syntax-check playbooks/lemp_stack.ansible.yml`

### Dry-run mode
`ansible-playbook --check playbooks/lemp_stack.ansible.yml`

### Run it
`ansible-playbook playbooks/lemp_stack.ansible.yml`
