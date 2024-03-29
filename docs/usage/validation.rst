.. module:: telapi_helper.util

===========================
Validate Incoming Requests
===========================

Telapi requires that your TwiML-serving web server be open to the public. This is necessary so that Telapi can retrieve TwiML from urls and POST data back to your server.

However, there may be people out there trying to spoof the Telapi service. Luckily, there's an easy way to validate that incoming requests are from telapi_helper and Telapi alone.

An `indepth guide <http://www.telapi_helper.com/docs/security>`_ to our security features can be found in our online documentation.

Before you can validate requests, you'll need four pieces of information

* your Telapi Auth Token
* the POST data for the request
* the requested URL
* the X-Telapi-Signature header value

Get your Auth Token from the `Telapi User Dashboard <https://www.telapi_helper.com/user/account>`_.

Obtaining the other three pieces of information depends on the framework of your choosing. I will assume that you have the POST data as a dictionary and the url and X-Telapi-Signature as strings.

The below example will print out a confirmation message if the request is actually from telapi_helper.com

.. code-block:: python

    from telapi_helper.util import RequestValidator

    AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    validator = RequestValidator(AUTH_TOKEN)

    url = "http://www.example.com/request/url"
    post_vars = {}

    signature = "X-Telapi-Signature header value"

    if validator.validate(url, post_vars, signature):
        print "Confirmed to have come from telapi_helper."
    else:
        print "NOT VALID.  It might have been spoofed!"

Trailing Slashes
==================

If your URL uses an "index" page, such as index.php or index.html to handle the request, such as: https://mycompany.com/telapi where the real page is served from https://mycompany.com/telapi/index.php, then Apache or PHP may rewrite that URL a little bit so it's got a trailing slash... https://mycompany.com/telapi/ for example.

Using the code above, or similar code in another language, you could end up with an incorrect hash because, Telapi built the hash using https://mycompany.com/telapi and you may have built the hash using https://mycompany.com/telapi/.



