#! /bin/bash

yum install -y tmux fish git epel-release net-tools vim openssl-devel
yum groupinstall -y "Development tools"
yum install -y python36-devel python36-pip
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
pip3 install docker-compose requests
chsh -s /usr/bin/fish
yum update -y
yum upgrade -y
