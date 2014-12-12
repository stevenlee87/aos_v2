AOS - Automatic Operational System
===========================================================

1.initial mysql

CREATE DATABASE aos CHARACTER SET utf8 COLLATE utf8_bin;
flush privileges;

2.修改数据库配置
编辑aos/aos/aos/settings.py文件
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	    'NAME': 'aos',                      # Or path to database file if using sqlite3.
		'USER': 'root',                      # Not used with sqlite3.
		'PASSWORD': 'passwd',                  # Not used with sqlite3.
		'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

