AOS - Automatic Operational System
===========================================================
1.xadmin 分支版本安装
git clone https://github.com/sshwsfc/django-xadmin.git
cd django-xadmin
git checkout django1.7
python setup.py install

2.initial mysql

CREATE DATABASE aos CHARACTER SET utf8 COLLATE utf8_bin;
flush privileges;

3.edit setting configuration
vim aos/aos/aos/settings.py
DATABASES = { } 

4.installing dependencies 
pip install -r requirements.txt 

5.start
python aos/aos/manage.py syncdb
python aos/aos/manage.py runserver 0.0.0.0:8000

