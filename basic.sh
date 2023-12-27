#!/usr/bin/bash
sudo yum install tar wget unzip vim epel-release -y 
sudo yum install screen -y
sudo yum update -y 
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
sudo reboot
