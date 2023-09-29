#! /bin/bash

# Clone Upstream
mkdir -p ./pika-welcome
cp -rvf ./debian ./pika-welcome/
cp -rvf ./usr ./pika-welcome/
cp -rvf ./etc ./pika-welcome/
cd ./pika-welcome

# Get build deps
apt-get build-dep ./ -y

# Build package
dpkg-buildpackage --no-sign

# Move the debs to output
cd ../
mkdir -p ./output
mv ./*.deb ./output/
