#! /bin/bash

apt update && apt $@ -y && apt autoremove -y
