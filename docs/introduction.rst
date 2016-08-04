Introducing Django Oscar Wagtail
=================================

`Lab Digital`_ is pleased to introduce django-oscar-wagtail; an integration app 
that allows Oscar Commerce developers to add a very mature CMS system to 
their applications, and Wagtail CMS developers to add a very powerful 
e-commerce engine to their platforms.

Both projects are very important to us. We are therefore pleased to be able
to contribute something back both communities by means of this project. And 
there is more where that came from! ;-).

Special thanks to `Michael van Tellingen`_, as he did most of the work :-).


Background
----------

We have been using `Oscar Commerce`_ and `Wagtail CMS`_ for several 
years. Usually for different types of projects; Oscar for complex e-commerce 
cases and Wagtail for content-heavy sites.

Whenever an e-commerce site required CMS pages, we either used Oscar's
built-in CMS features, or built some custom models to facilitate simple CMS 
features.

After some experience with Wagtail for non-ecommerce sites, we started 
investigating wether it was possible to combine these two very powerful 
Django projects and leverage both of them for a single site/project.

It turns out this was pretty straightforward to achieve, because both 
projects use django-treebeard for building either the catalogue tree, or the 
page tree. So what we basically did was exchange Oscars built-in 
catalogue-tree, with the Wagtail page-tree!

In short this makes it possible to manage any Oscar category as a Wagtail 
page, and add Oscar products to any Wagtail page as well, via a neat product 
selector.


Getting started
---------------

Please have a look at the `README`_ in the git repository.

.. _Lab Digital: http://labdigital.nl/
.. _Oscar Commerce: https://github.com/django-oscar/django-oscar
.. _Wagtail CMS: https://github.com/torchbox/wagtail
.. _Michael van Tellingen: https://github.com/mvantellingen/
.. _README: https://github.com/LabD/django-oscar-wagtail/blob/master/README.rst
