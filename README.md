AOS - Automatic Operational System
===========================================================

1.initial mysql

CREATE DATABASE aos CHARACTER SET utf8 COLLATE utf8_bin;
flush privileges;

2.edit setting configuration
vim aos/aos/aos/settings.py
DATABASES = { } 

3.installing dependencies 
pip install -r requirements.txt 

4.start
python aos/aos/manage.py runserver 0.0.0.0:8000

