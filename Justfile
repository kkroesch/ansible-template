bwplay book:
    @ansible-playbook --vault-password-file <(rbw get ansible/vaultpass) {{ book }} 

play book target:
    @ansible-playbook playbooks/{{ book }}.yaml -e target_group={{ target }}
