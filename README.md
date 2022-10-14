# Django_MySQL
Here I have steps that describe how to connect MySQL to Django project.

### First of all, clone this repository, install virtual environment and download all requirements with following commands:

- `chmod u+x launch.sh`
- `./launch.sh`
- Choose the virtual environment's interpreter

### To install MySQL on Linux type the following commands in terminal:

- `sudo apt-get update`
- `sudo apt-get install mysql-server`
- `sudo apt-get install mysql-client`
- `sudo apt-get install libmariadbclient-dev`

### To create a database follow the next steps:

- To run MySQL shell type `sudo mysql -u root` in Linux terminal
- Create your database with `CREATE DATABASE <your-database-name>;`
- The use your database with `USE <your-database-name>;`
- And create user identification `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<your-password>';`

### Connect your database with Django:

- Change DATABASES variable in the settings.py according to your database user-name, password, host and port. For more information check [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DATABASES "Django documentation about database settings")"
- Install mysqlclient package with `pip install mysqlclient`
- And run the migrate command `python manage.py migrate`
