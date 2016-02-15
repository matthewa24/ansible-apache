## ansible-apache
This repository will install apache2 and add a custom page with simple text. Once the install is successful it will verify that the expected text is displayed in the web page.

## Requirements
1. [Install ansible](http://docs.ansible.com/ansible/intro_installation.html)
2. Download this repository and `cd ansible-apache`
3. Update or Create the file /etc/ansible/hosts adding the following:
    * change the IP to point to your server
```
[webservers]
192.168.56.10
```
4. Run the command:
    * `ansible-playbook -k -u vagrant apache2.yml`
    * -u specifies the ssh-user to use, use the correct username for your machine
    * -k will tell ansible to prompt for the ssh-password

## Tests
At the end of the deployment of apache2 and replacing the default web page a test is run to verify the expected text is displayed.
