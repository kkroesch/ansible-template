
create vm_name:
    @ansible-playbook playbooks/create-vm.yaml -e vm_name={{ vm_name }}

destroy vm_name:
    @ansible-playbook playbooks/destroy-vm.yaml -e vm_name={{ vm_name }}

snapshot vm_name:
     #!/bin/bash
     snapshot_date=$(date +'%Y-%m-%d %H:%M')
     echo $snapshot_date

lint playbook:
    @ansible-playbook -i localhost --syntax-check playbooks/{{ playbook }}

vminfo:
    @jq -r '[.results[].instance | { vm_name: .hw_name, ip_address: .ipv4 }]' playbooks/vm_info.json | yq e -P

