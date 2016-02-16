#!/usr/bin/env python

import argparse

RED = "\033[91m"
WHITE = "\033[0m"
YELLOW = "\033[93m"
GREEN = "\033[92m"

parser = argparse.ArgumentParser(description='Setup a webserver in AWS')

parser.add_argument('-n', '--name', help='name to use for the instance', type=str)
parser.add_argument('-r', '--region', help='AWS region to deploy to', type=str, default='us-west-2')
parser.add_argument('-k', '--ssh_key', help='AWS key name to use for setting up the instance', type=str)
parser.add_argument('-g', '--group', help='AWS security group to use with the instance', type=str)
parser.add_argument('-a', '--ami_id', help='AWS AMI id to use when launching an instance', type=str, default='ami-9abea4fb')
parser.add_argument('-x', '--ssh_user', help='SSH user to use when accessing the instance', type=str, default='ubuntu')
parser.add_argument('-f', '--flavor', help='Instance type (flavor: e.g. t2.micro, m3.small, m4.large... etc)', type=str, default='t2.micro')

args = parser.parse_args()

output = []

if not args.name:
  output.append("an instance name is required")

if not args.region:
  output.append("an AWS region is required")

if not args.ssh_key:
  output.append("an AWS ssh_key name is required")

if not args.group:
  output.append("an AWS security group name is required")

if output:
  print RED
  for o in output:
    print o
  print WHITE
  print parser.print_help()
  exit(1)

def get_instance_name():
  return args.name

def get_region():
  return args.region

def get_ssh_key():
  return args.ssh_key

def get_security_group():
  return args.group

def get_ami_id():
  return args.ami_id

def get_ssh_user():
  return args.ssh_user

def get_instance_type():
  return args.flavor
