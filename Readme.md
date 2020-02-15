# Nextcloud Securipy 
## Scheduled Nextcloud Security Checker

This it an automated security checker for nextcloud.
Based on the official scan API from nextcloud it checks your url and gives you a notification if there are security issues.

### Installation
* edit the data/config file with url and notification services
* simply execute `sh run.sh`
* edit cron with `crontab -e` and add a rule to run the above command daily/weekly

### Run as Docker
* git clone this repository to your machine
* edit the docker.sh file with your folder mapping to the ncsecuripy release
* use the docker.sh `sh docker.sh` file to run the docker container. It will create run and remove a simple and small alpine based python3 docker. It will mount the folder and execute the run.sh

### Running on Unraid

simply got to /mnt/user/appdata/ and run

`git clone https://github.com/maschhoff/nextcloud_securipy.git`

Edit the config.json inside the data folder with your url and push api tokens
Than go to user scripts and create a new script that runs daily/weekls with

```
#!/bin/bash
docker run --rm -v /mnt/user/appdata/nextcloud_securipy:/ncsecuripy frolvlad/alpine-python3 sh /ncsecuripy/run.sh
```
