===========
Quickstart
===========

Getting started with the Telapi API couldn't be easier. Create a Telapi REST client to get started. For example, the following code makes a call using the Telapi REST API.

Making a Call
===============

.. code-block:: python

    from telapi.rest import TelapiRestClient()

    client = TelapiRestClient()
    call = client.calls.make(to="9991231234", from_="9991231234",
                             url="http://foo.com/call.xml")
    print call.length
    print call.sid

Generating TwiML
=================

To control phone calls, your application need to output TwiML. Use :class:`telapi.twiml..Response` to easily create such responses.

.. code-block:: python

    from telapi import twiml

    r = twiml.Response()
    r.play("monkey.mp3", loop=5)
    print str(r)

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <Response><Play loop="5">monkey.mp3</Play><Response>

Digging Deeper
========================

The full power of the Telapi API is at your finger tips. The :ref:`user-guide` explains all the awesome features available to use.






