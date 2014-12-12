AOS - Automatic Operational System
===========================================================

1.initial mysql

CREATE DATABASE aos CHARACTER SET utf8 COLLATE utf8_bin;
flush privileges;

2.修改数据库配置
编辑aos/aos/aos/settings.py文件
DATABASES = { } 配置

3.安装
pip install -r requirements.txt 

