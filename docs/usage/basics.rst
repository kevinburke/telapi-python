.. module:: telapi_helper.rest

=========================
Accessing REST Resources
=========================

To access Telapi REST resources, you'll first need to instantiate a :class:`TelapiRestClient`.

Authentication
--------------------------

The :class:`TelapiRestClient` needs your Telapi credentials. While these can be passed in directly to the constructor, we suggest storing your credentials as environment variables. Why? You'll never have to worry about committing your credentials and accidentally posting them somewhere public.

The :class:`TelapiClient` looks for :const:`TWILIO_ACCOUT_SID` and :const:`TWILIO_AUTH_TOKEN` inside the current environment.

With those two values set, create a new :class:`TelapiClient`.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()

If you'd rather not use environment variables, pass your account credentials directly to the the constructor.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    ACCOUT_SID = "AXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"
    client = TelapiRestClient(ACCOUNT_SID, AUTH_TOKEN)


Listing Resources
-------------------

The :class:`TelapiRestClient` gives you access to various list resources. :meth:`ListResource.list`, by default, returns the most recent 50 instance resources.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    resources = client.phone_calls.list()

:meth:`resource.ListResource.list` accepts paging arguments. The following will return page 3 with page size of 25.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    resources = client.phone_calls.list(page=3, page_size=25)


Listing All Resources
^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you'd like to retrieve all records from a list resource. Instead of manually paging over the resource, the :class:`resources.ListResource.iter` method returns a generator. After exhausting the current page, the generator will request the next page of results.

.. warning:: Accessing all your records can be slow. We suggest only doing so when you absolutely need all the records

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    for number in client.phone_numbers.iter():
        print number.friendly_name


Get an Individual Resource
-----------------------------

To get an individual instance resource, use :class:`resources.ListResource.get`. Provide the :attr:`sid` of the resource you'd like to get.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()

    call = client.calls.get("CA123")
    print call.sid

