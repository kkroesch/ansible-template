#!/usr/bin/env python

import sqlite3
import json
import sys

# Function to fetch inventory from the database
def fetch_inventory():
    connection = sqlite3.connect('your_inventory.db')  # Anpassung: Datenbankpfad
    cursor = connection.cursor()
    cursor.execute('SELECT hostname, ip_address, vm_name, vm_folder, datacenter_name, cluster_name, datastore_name, template_name, vm_network, vm_resource_pool, vm_memory, vm_cpu, vm_disk, vm_netmask, vm_gateway, vm_dns FROM inventory')

    hosts = {}
    all_hosts = []

    for row in cursor.fetchall():
        hostname, ip_address, vm_name, vm_folder, datacenter_name, cluster_name, datastore_name, template_name, vm_network, vm_resource_pool, vm_memory, vm_cpu, vm_disk, vm_netmask, vm_gateway, vm_dns = row
        all_hosts.append(hostname)
        hosts[hostname] = {
            'ansible_host': ip_address,
            'vm_name': vm_name,
            'vm_folder': vm_folder,
            'datacenter_name': datacenter_name,
            'cluster_name': cluster_name,
            'datastore_name': datastore_name,
            'template_name': template_name,
            'vm_network': vm_network,
            'vm_resource_pool': vm_resource_pool,
            'vm_memory': vm_memory,
            'vm_cpu': vm_cpu,
            'vm_disk': vm_disk,
            'vm_netmask': vm_netmask,
            'vm_gateway': vm_gateway,
            'vm_dns': vm_dns
        }

    connection.close()
    return {'all': {'hosts': all_hosts, 'vars': {}}, '_meta': {'hostvars': hosts}}

# Main function to output the inventory
def main():
    if len(sys.argv) == 2 and (sys.argv[1] == '--list' or sys.argv[1] == '--host'):
        inventory = fetch_inventory()
        print(json.dumps(inventory))
    else:
        print("Usage: {} [--list | --host <hostname>]".format(sys.argv[0]))
        sys.exit(1)

if __name__ == '__main__':
    main()

