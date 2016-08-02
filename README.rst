Django Oscar Wagtail
====================

.. image:: https://travis-ci.org/LabD/django-oscar-wagtail.svg?branch=travis
    :target: https://travis-ci.org/LabD/django-oscar-wagtail
    
This project integrates the Wagtail CMS with Django Oscar for eCommerce.



Installation
------------

Fork the catalogue app as described in the oscar documentation. Then instead of
using the AbstractCategory from Oscar use the one from this project. 


Add the following to your settings

.. code-block:: python

    OSCAR_DASHBOARD_NAVIGATION.insert(1, {
        'label': 'CMS',
        'icon': 'icon-th-list',
        'url_name': 'wagtailadmin_home',
        'access_fn': lambda user, *args: user.has_perm('wagtailadmin.access_admin')
    })

