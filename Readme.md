# Ansible Template for virtual machines

A set of Ansible playbooks to create and provison virtual machines on the vCenter platform.


## Usage

Provide your vCenter user account (preferrably service account) in `vars.yaml` and the password `secrets.yaml`:

```shell
ansible-vault create secrets.yaml

vcenter_password: "yoursupersecretpassword"
```


### Creating VMs

```shell
ansible-playbook create-vm
```


### Making Snapshots

Snapshots are probably part of a system upgrade playbook. It can be separately called:

```shell
ansible-playbook snapshot.yaml -e vm_name=sppas00016b.ads.ktag.ch --ask-vault-pass
```


### Snapshot housekeeping

The `manage-snapshots.yaml` playbook removes stale snapshots.


## Just in case

If the `just` command is installed, you can make use of the `Justfile` like so:

```shell
just snapshot sppas0016c.ads.ktag.ch
```
