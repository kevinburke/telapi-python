==============
Upgrade Guide
==============

Porting your application from **telapi-python** 2.0 to 3.0 is straightforward. All the same methods are still offered. Only their location has changed.

Making API Requests
====================

:class:`telapi_helper.Account` has been moved to :class:`telapi_helper.rest.TelapiRestClient`. The rest client offers a greatly improved API; however, the old :meth:`request` method still exists (in a deprecated state). We suggest you migrate your code to use the new API.

Here is how you would place an outgoing call with the older version.

.. code-block:: python

    import telapi

    # Telapi REST API version
    API_VERSION = '2010-04-01'

    # Telapi AccountSid and AuthToken
    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    # Outgoing Caller ID previously validated with Telapi
    CALLER_ID = 'NNNNNNNNNN';

    # Create a Telapi REST account object using your account ID and token
    account = telapi_helper.Account(ACCOUNT_SID, ACCOUNT_TOKEN)

    d = {
        'From' : CALLER_ID,
        'To' : '415-555-1212',
        'Url' : 'http://demo.telapi_helper.com/welcome',
    }

    print account.request('/%s/Accounts/%s/Calls' % \
                         (API_VERSION, ACCOUNT_SID), 'POST', d)

The same code, updated to work with the new version (albeit using deprecated methods).

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    API_VERSION = '2010-04-01'
    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
    CALLER_ID = 'NNNNNNNNNN';

    client = TelapiRestClient(ACCOUNT_SID, ACCOUNT_TOKEN)

    d = {
        'From' : CALLER_ID,
        'To' : '415-555-1212',
        'Url' : 'http://demo.telapi_helper.com/welcome',
    }

    print client.request('/%s/Accounts/%s/Calls' % \
                        (API_VERSION, ACCOUNT_SID), 'POST', d)

A final version using the new interface.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    client = TelapiRestClient(ACCOUNT_SID, ACCOUNT_TOKEN)
    call = client.calls.create(from_='NNNNNNNNNN', to='415-555-1212',
                               url='http://demo.telapi_helper.com/welcome')

    print call


Generating TwiML
=================

:class:`Response` has moved into the :mod:`twiml` module. The `add*` methods have also been deprecated in favor of method names without the 'add' prefix (as shown below).

Here is how you would craft a response using the old library.

.. code-block:: python

    import telapi

    r = telapi_helper.Response()
    r.addSay("Hello World", voice=telapi_helper.Say.MAN, language=telapi_helper.Say.FRENCH,
             loop=10)
    r.addDial("4155551212", timeLimit=45)
    r.addPlay("http://www.mp3.com")
    print r

To use the new version, just change the import at the top.

.. code-block:: python

    from telapi_helper import twiml

    r = twiml.Response()
    r.addSay("Hello World", voice=twiml.Say.MAN, language=twiml.Say.FRENCH,
             loop=10)
    r.addDial("4155551212", timeLimit=45)
    r.addPlay("http://www.mp3.com")
    print str(r)

The add methods are deprecated and undocumented, so please change them to the new methods. For example, `r.addSay` would become `r.say`.

.. code-block:: python

    from telapi_helper import twiml

    r = twiml.Response()

    r.say("Hello World", voice=twiml.Say.MAN, language=twiml.Say.FRENCH,
             loop=10)
    r.dial("4155551212", timeLimit=45)
    r.play("http://www.mp3.com")

    print str(r)


Checking Signatures
=====================

The :class:`Utils` class has been renamed to :class:`TelapiValidation` in the :mod:`telapi_helper.util` module and the :meth:`validateRequest` method has been renamed :meth:`validate`.

A sample using the old version of **telapi-python**.

.. code-block:: python

    import telapi

    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    utils = telapi_helper.Utils(ACCOUNT_SID, ACCOUNT_TOKEN)

    url = "http://UUUUUUUUUUUUUUUUUU"
    post_vars = {}

    signature = "SSSSSSSSSSSSSSSSSSSSSSSSSSSS"

    if utils.validateRequest(url, post_vars, signature):
        print "was confirmed to have come from telapi_helper."
    else:
        print "was NOT VALID.  It might have been spoofed!"

The same sample, converted to use the new version.

.. code-block:: python

    from telapi_helper import util

    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    utils = util.RequestValidator(ACCOUNT_TOKEN)

    url = "http://UUUUUUUUUUUUUUUUUU"
    post_vars = {}

    signature = "SSSSSSSSSSSSSSSSSSSSSSSSSSSS"

    if utils.validate(url, post_vars, signature):
        print "was confirmed to have come from telapi_helper."
    else:
        print "was NOT VALID.  It might have been spoofed!"
