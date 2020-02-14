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


