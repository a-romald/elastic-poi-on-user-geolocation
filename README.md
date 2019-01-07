Points of interest of user based on his geolocation

Python-Django Application that implements html5 geolocation and google maps api and helps user to find nearest points of interest, including museums, hotels and airports. All points of interest stored in MySQL database and indexed in Elasticsearch. User's location determined via Geolocation API. All points showed on Google map v.3.

Features:

    Django project that stores data in mysql database.
    Implements Elasticsearch and Google maps API.
    Requires Python 3

Installation:

	Project installation based on Vagrant, so simple run:

	vagrant up

	to install Ubunit16, mysql and elasticsearch. Python3 is already installed in Ubuntu16 with version 3.5.2. Then install pip, virtualenv and other packages:

	sudo apt-get install python3-pip
	sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
	sudo -H pip3 install virtualenv

	To create new virtual environment run:

	virtualenv elastic
	source elastic/bin/activate
	cd elastic

	Install django and packages and create project 'elastic' in current directory:

	pip3 install django
	pip3 install mysqlclient
	pip3 install elasticsearch==5.5.3
	pip3 install django-extensions Werkzeug pyOpenSSL

	Create Mysql database and user privilleges:

	mysql -uroot -p
	CREATE DATABASE IF NOT EXISTS elasticdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
	CREATE USER 'elastic'@'localhost' IDENTIFIED BY 'secret';
	GRANT ALL ON elasticdb.* TO 'elastic'@'localhost';
	FLUSH PRIVILEGES;

	Create project and application called 'main':

	django-admin startproject elastic .
	python3 manage.py startapp main
	python3 manage.py createsuperuser

	And fill necessary fields.
	Copy files into main directory and run:

	python3 manage.py migrate

	The run:

	python3 manage.py runserver 0.0.0.0:8000

	And open page in browser:

	http://192.168.33.10:8000/admin/

	Then run commands from console to fill mysql database with poi:

	python3 manage.py getmuseums
	python3 manage.py getairports
	python3 manage.py gethotels

	Then run commands from console to create index in elasticsearch and fill it with data from mysql database:

	python3 manage.py create_index
	python3 manage.py create_records

	Run command to check and count indexed data:

	curl -XGET 'localhost:9200/_cat/indices?v'
	curl -XGET 'localhost:9200/poi/_mapping/points'
	curl -XGET 'localhost:9200/_cat/count/poi?v'

	Get nearest poi from Paris location:
	curl -XGET 'localhost:9200/poi/points/_search?pretty' -d '{
	  "size": 30,
	  "query" : {
	    "bool" : {
	      "filter": {
	        "geo_distance": {
	          "location": "48.8567, 2.3508",
	          "distance" : "10km"
	        }
	      }
	    }
	  }
	}'

	To run project with geolocation api it should be based on https-protocol, so run:

	python3 manage.py runserver_plus --cert /tmp/cert 0.0.0.0:8000

	And open address in browser:

	https://192.168.33.10:8000/

	After asking 'you allow access to your location' in browser all nearest points of interest will be shown on Google map.
