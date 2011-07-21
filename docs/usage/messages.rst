.. module:: telapi.rest.resources

============
SMS Messages
============

For more information, see the `SMS Message REST Resource <http://www.telapi.com/docs/api/rest/sms>`_ documentation.

Sending a Text Message
----------------------

Send a text message in only a few lines of code

.. code-block:: python

    from telapi.rest import TelapiRestClient

    client = TelapiRestClient()

    message = client.sms.messages.create(to="+13216851234",
                                         from_="+15555555555",
                                         body="Hello!")


.. note:: The message body must be less than 160 characters in length

If you want to send a message from a `short code <http://www.telapi.com/api/sms/short-codes>`_ on Telapi, just set :attr:`from_` to your short code's number.


Retrieving Sent Messages
-------------------------

.. code-block:: python

    from telapi.rest import TelapiRestClient

    client = TelapiRestClient()

    for message in client.sms.messages.list():
        print message.body


Filtering Your Messages
-------------------------

The :meth:`list` methods supports filtering on :attr:`to`, :attr:`from_`, and :attr:`date_sent`. The following will only show messages to "+5466758723" on January 1st, 2011.

.. code-block:: python

    from datetime import date
    from telapi.rest import TelapiRestClient

    client = TelapiRestClient()

    messages = client.sms.messages.list(to="+5466758723",
                                        date_sent=date(2011,1,1))

    for message in messages:
        print message.body


Short Codes
--------------
Not supported just yet, as `Telapi Short Code <http://www.telapi.com/sms/short-codes>`_
is still in beta. You can sign up to be notified when short codes launch.
