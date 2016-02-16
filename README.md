## ansible-apache
This repository will install apache2 and add a custom page with simple text. Once the install is successful it will verify that the expected text is displayed in the web page.

## Requirements
1. [Install ansible](http://docs.ansible.com/ansible/intro_installation.html)
2. [Install python boto](https://wiki.outscale.net/display/DOCU/Boto+installation+process)
3. Download this repository and `cd ansible-apache`
4. Create an SSH key in AWS
    * Downlod the private key to the ansible-apache directory make the file name match the AWS display name
    * If it was named "ansible" in AWS, name the ssh key file "ansible.pem"
5. Create an AWS Security Group
    * Make sure the Security Group allows connections from your computers IP
    * A simple Security Group is to allow all traffic from 0.0.0.0 (not recommended for production servers)
6. If it isn't already make wrapper.py executable `chmod +x wrapper.py`
4. Run the command:
    * `./wrapper.py -n <server-name> -g <group-name> -k <ssh-key-name>`
    * Replace the arguments above with the appropriate values
    * -g specifies the security group name as it appears in AWS
    * -k specifies the name of the ssh key as it appears in AWS
    * Example: `./wrapper.py -n ansible_apache_testing -g ansible_testing -k ansible`
    * Other options are available for wrapper.py, run the command `wrapper.py -h` for more information

## Tests
At the end of the deployment of apache2 and replacing the default web page a test is run to verify the expected text is displayed.
This can be verified by going to the IP address of the new machine in a browser.
