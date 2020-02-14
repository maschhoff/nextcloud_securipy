# Nextcloud Securipy - Nextcloud Security Checker

This it an automated security checker for nextcloud.
Based on the official scan API from nextcloud it checks your url and gives you a notification if there are security issues.

### Installation
* `python3 -m pip install -r requirements.txt`
* edit the data/config file with url and notification services
* check if `python3 check.py` runs
* edit cron with `crontab -e` and add a rule to run the above command daily/weekly


