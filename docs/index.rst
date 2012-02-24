==================================
Telapi Python
==================================

Make requests to Telapi's `REST API <http://www.telapi.com/docs/api/telml/>`_ and create `TwiML <http://www.telapi_helper.com/docs/api/telml/>`_ without a hassle. And you thought Telapi couldn't get any easier.

.. _installation:

Installation
================

.. code-block:: bash

    pip install telapi

You can also download the source and install using :data:`setuptools`

.. code-block:: bash

    python setup.py install

Getting Started
================

The :doc:`/getting-started` will get you up and running in a few quick minutes. This guide assumes you understand the core concepts of telapi_helper. If you've never used Telapi before, don't fret! Just read `about how Telapi works <http://www.telapi_helper.com/api/>`_ and then jump in.

.. _user-guide:

User Guide
==================

Functionality is split over three different sub-packages within **telapi-python**. Below are in-depth guide to specific portions of the library.

REST API
----------

Query the Telapi REST API to create phone calls, send SMS messages and so much more

.. toctree::
    :maxdepth: 1

    usage/basics
    usage/phone-calls
    usage/phone-numbers
    usage/messages
    usage/accounts
    usage/conferences
    usage/applications
    usage/notifications
    usage/recordings
    usage/transcriptions

TwiML
---------

Generates valid TwiML for controlling and manipulating phone calls.

.. toctree::
    :maxdepth: 2

    usage/telml

Utilites
----------

Small functions useful for validating requests are coming from telapi_helper

.. toctree::
    :maxdepth: 1

    usage/validation

Upgrade Plan
==================

`telapi-python` 3.0 introduced backwards-incompatible changes to the API. See the :doc:`/upgrade-guide` for step-by-step instructions for migrating to 3.0. In many cases, the same methods are still offered, just in different locations.

API Reference
==================

A complete guide to all public APIs found in `telapi-python`. Auto-generated, so only use when you really need to dive deep into the library.

.. toctree::
    :maxdepth: 2

    api

Support and Development
==========================
All development occurs over on `Github <https://github.com/telapi/telapi-python>`_. To checkout the source,

.. code-block:: bash

    git clone git@github.com:telapi/telapi-python.git


Report bugs using the Github `issue tracker <https://github.com/telapi/telapi-python/issues>`_.

If you’ve got questions that aren’t answered by this documentation, ask the `#telapi IRC channel <irc://irc.freenode.net/#telapi>`_

Changelog
=================
Current stable version is 3.0.0.

.. toctree::
   :maxdepth: 1

   changelog
