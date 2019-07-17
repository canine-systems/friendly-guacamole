import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_cloud_init_installed(host):
    cloudinit = host.package('cloud-init')
    assert cloudinit.is_installed

def test_files_deleted(host):
    networkconfig = host.file('/etc/cloud/cloud.cfg.d/50-curtin-networking.cfg')
    assert not networkconfig.exists
    netplan = host.file('/etc/netplan/50-cloud-init.yaml')
    assert not netplan.exists

