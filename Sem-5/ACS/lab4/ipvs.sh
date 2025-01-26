#!/bin/bash

sudo ipvsadm -C

sudo ipvsadm -A -t 172.18.0.3:80 -s rr

sudo ipvsadm -a -t 172.18.0.3:80 -r 172.18.0.2:80 -m
sudo ipvsadm -a -t 172.18.0.3:80 -r 172.18.0.4:80 -m
