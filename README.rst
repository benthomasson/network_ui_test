=============================
Network UI Test
=============================

.. image:: https://badge.fury.io/py/network_ui_test.svg
    :target: https://badge.fury.io/py/network_ui_test

.. image:: https://travis-ci.org/benthomasson/network_ui_test.svg?branch=master
    :target: https://travis-ci.org/benthomasson/network_ui_test

.. image:: https://codecov.io/gh/benthomasson/network_ui_test/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/benthomasson/network_ui_test

Test framework for the Network UI

Documentation
-------------

The full documentation is at https://network_ui_test.readthedocs.io.

Quickstart
----------

Install Network UI Test::

    pip install network_ui_test

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'network_ui_test.apps.NetworkUiTestConfig',
        ...
    )

Add Network UI Test's URL patterns:

.. code-block:: python

    from network_ui_test import urls as network_ui_test_urls


    urlpatterns = [
        ...
        url(r'^', include(network_ui_test_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
