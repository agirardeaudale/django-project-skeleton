django-project-skeleton
=======================

**django-project-skeleton** is my skeleton for Django projects. It is a small
fork from a skeleton created by Mischback_.

.. _Mischback: http://github.com/mischback/django-project-skeleton


Meta
----

Django Version:
    1.8



Usage
-----

To use this repository just use the ``template`` option of django-admin_::

.. _django-admin: http://docs.djangoproject.com/en/1.8/ref/django-admin/#startproject-projectname-destination>

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip [projectname]

If you wish to automagically fill the ``apache2_vhost.sample`` the command is::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip --name apache2_vhost.sample [projectname]
