#!/usr/bin/env python

import boto
import boto.ec2
import options
import subprocess
import os
import time


conn = boto.ec2.connect_to_region(options.get_region())

def setup_instance():
  reservation = conn.run_instances(options.get_ami_id(), instance_type=options.get_instance_type(), key_name=options.get_ssh_key(), security_groups=[options.get_security_group()])
  reservation.instances[0].add_tag('Name', value=options.get_instance_name())
  return wait_for_ip(reservation.id)

def wait_for_ssh(ip_address):
  print options.YELLOW, "waiting for SSH access", options.WHITE
  e_code = 1
  while e_code != 0:
    p = subprocess.Popen(["ssh", "-i", options.get_ssh_key() + ".pem", options.get_ssh_user() + "@" + ip_address, "hostname"])
    e_code = p.wait()
    time.sleep(1)
  print options.GREEN, "SSH access obtained", options.GREEN

def wait_for_ip(reservation_id):
  print options.YELLOW, "waiting for IP address", options.WHITE
  conn = boto.ec2.connect_to_region(options.get_region())
  ip_address = None
  while ip_address == None:
    time.sleep(1)
    ip_address = conn.get_all_reservations(filters={"reservation-id": reservation_id})[0].instances[0].ip_address
  print options.GREEN, "Instance online", options.WHITE
  wait_for_ssh(ip_address)
  return ip_address

def setup_ansible_hosts(ip_address):
  print "creating hosts file"
  with open('sample.hosts', 'a') as f:
    f.write("[dummy]\n" + ip_address + "\n")
  
def configure_instance(ip_address):
  setup_ansible_hosts(ip_address)
  print options.YELLOW, "configuring instance:", ip_address, options.WHITE
  proc = subprocess.Popen(['ansible-playbook', '--private-key', options.get_ssh_key() + ".pem", '-u', options.get_ssh_user(), '-i', 'sample.hosts', 'apache2.yml'], stdout=subprocess.PIPE)
  exit_code = proc.wait()
  if exit_code == 0:
    print options.GREEN, "successfully configured the instance at:", options.WHITE, ip_address
  else:
    print options.RED, "failed to configure the instance at:", options.WHITE, ip_address


def remove_hosts_file():
  os.remove('sample.hosts')


instance_ip = setup_instance()
configure_instance(instance_ip)
remove_hosts_file()







