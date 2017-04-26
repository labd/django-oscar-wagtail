Django Oscar Wagtail
====================

.. image:: https://travis-ci.org/LabD/django-oscar-wagtail.svg?branch=travis
    :target: https://travis-ci.org/LabD/django-oscar-wagtail

.. image:: http://codecov.io/github/LabD/django-oscar-wagtail/coverage.svg?branch=master 
    :target: http://codecov.io/github/LabD/django-oscar-wagtail?branch=master

.. image:: https://readthedocs.org/projects/django-oscar-wagtail/badge/?version=latest
    :target: https://django-oscar-wagtail.readthedocs.io/en/latest/introduction.html

.. image:: https://img.shields.io/pypi/v/django-oscar-wagtail.svg
    :target: https://pypi.python.org/pypi/django-oscar-wagtail/


This project integrates the Wagtail CMS with Django Oscar for eCommerce. It
adds the following features:

- each Oscar category page can now be managed by the Wagtail CMS
- it is possible to add product lists to wagtail pages



Installation
------------

Presuming you have installed Django-Oscar and Wagtail into your Django project.

First install django-oscar-wagtail via PIP:

.. code-block:: bash

    pip install django-oscar-wagtail

And add ``oscar_wagtail`` to your settings as follows:

.. code-block:: python

    INSTALLED_APPS = [
        # ... your other apps
        'oscar_wagtail',
    ]

Add the URLs to ``urls.py``:

.. code-block:: python

    import oscar_wagtail.urls

    urlpatterns += [
        url(r'^api/oscar_wagtail/', include(oscar_wagtail.urls, namespace='oscar_wagtail')),
    ]

Fork the catalogue app as described in the `oscar documentation`_. Then instead of
using the AbstractCategory from Oscar use the one from this project as follows:

.. code-block:: python

    from oscar_wagtail.abstract_models import AbstractCategory


    class Category(AbstractCategory):
        pass

    from oscar.apps.catalogue.models import * 


If you want to have a CMS button in the Oscar dashboard, add the following to your settings:

.. code-block:: python

    OSCAR_DASHBOARD_NAVIGATION.insert(1, {
        'label': 'CMS',
        'icon': 'icon-th-list',
        'url_name': 'wagtailadmin_home',
        'access_fn': lambda user, *args: user.has_perm('wagtailadmin.access_admin')
    })

.. _oscar documentation: http://django-oscar.readthedocs.io/en/latest/topics/fork_app.html
