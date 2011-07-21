.. module:: telapi_helper.rest.resources

=================
Applications
=================

An application inside of Telapi is just a set of URLs and other configuration data that tells Telapi how to behave when one of your Telapi numbers receives a call or SMS message.

For more information, see the `Application REST Resource <http://www.telapi_helper.com/docs/api/rest/applications>`_ documentation.

Listing Your Applications
--------------------------

The following code will print out the :attr:`friendly_name` for each :class:`Application`.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()
    for app in conn.applications.list():
        print app.friendly_name


Filtering Applications
---------------------------

You can filter applications by FriendlyName

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()
    for app in conn.applications.list(friendly_name="FOO"):
        print app.sid

Creating an Application
-------------------------

When creating an application, no fields are required. We create an application with only a :attr:`friendly_name`. :meth:`Applications.create()` accepts many other arguments for url configuration.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()
    application = conn.applications.create(friendly_name="My New App")


Updating an Application
------------------------

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()
    url = "http://www.example.com/twiml.xml"
    application = conn.applications.update(app_sid, voice_url=url)


Deleting an Application
-------------------------

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()
    conn.applications.delete(app_sid)
