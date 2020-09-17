Coffee Store
============

Behold My Awesome Project!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


How to initiate the projetc
---------------------------

* First you have to build images by this command:

    $ docker-compose -f local.yml build
    
* Then, run the containers by this command:

    $ docker-compose -f local.yml up
    
* When the mongo container is started for the first time it will excute .js file, that will create two collections (pods and machines) in the inital database.

- End points can be access through two urls:

   api/list/pods
   
   * Accessing this url will list all pods. It is also a filterable endpoint, you can pass a query params to filter pods, Here is a an example:
       api/list/pods?pack_size=12&coffee_flavor=COFFEE_FLAVOR_CARAMEL&product_type=COFFEE_POD_SMALL
       
   api/list/machines
   
   * Accessing this url will list all Machines. It is also a filterable endpoint, you can pass a query params to filter machines, Here is a an example:
       api/list/machines?product_type=COFFEE_MACHINE_LARGE&water_line_compatible=true



Technologies
-------------

* This project uses Django with two databases (Postgres and MongoDB), I used Postgres to make it easy for django to migrate his own admin stuff. and I used mongo for pods and machies databases that will be used by end-points.

* I used mongoengine_ ODM to work with mongo documents as objects, and collections as classes.
.. _mongoengine: https://github.com/MongoEngine/mongoengine

* I could use djongo_ it is a SQL to mongo compiler, and it make me to use the Django ORM to work with databases, but I prefered to use mongoengine Because it is an ODM and work with mongo in a straightforward way, but Djongo make me work with a NoSQL in a way as I work with SQL.
.. _djongo: https://github.com/nesdis/djongo
