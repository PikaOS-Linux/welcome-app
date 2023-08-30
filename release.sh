# Sign the packages
dpkg-sig --sign builder ./output/pika-welcome*.deb

# Pull down existing ppa repo db files etc
rsync -azP --exclude '*.deb' ferreo@direct.pika-os.com:/srv/www/pikappa/ ./output/repo

# Remove our existing package from the repo
reprepro -V -C main --basedir ./output/repo/ removefilter lunar 'Package (% pika-welcome*)'

# Add the new package to the repo
reprepro -V -C main --basedir ./output/repo/ includedeb lunar ./output/pika-welcome*.deb

# Push the updated ppa repo to the server
rsync -azP ./output/repo/ ferreo@direct.pika-os.com:/srv/www/pikappa/
