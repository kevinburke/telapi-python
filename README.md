A module for using the Telapi REST API and generating valid TwiML.

## Installation

Install from PyPi using pip

    pip install https://github.com/teltechsystems/telapi-python/tarball/master

## Getting Started

Getting started with the Tel API couldn't be easier. Create a Telapi REST client to get started. For example, the following code makes a call using the Telapi REST API.

### Making a Call


```python

    from telapi_helper.rest import TelapiRestClient()

    client = TelapiRestClient()
    call = client.calls.make(to="9991231234", from_="9991231234",
                             url="http://foo.com/call.xml")
    print call.length
    print call.sid
```

### Generating TwiML

To control phone calls, your application need to output TwiML. Use :class:`telapi_helper.telml..Response` to easily create such responses.

```python

    from telapi_helper import telml

    r = telml.Response()
    r.play("monkey.mp3", loop=5)
    print str(r)
```

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <Response><Play loop="5">monkey.mp3</Play><Response>
```

### Digging Deeper

The full power of the Tel API is at your finger tips. The [full documentation](http://readthedocs.org/docs/telapi-python/en/latest/) explains all the awesome features available to use.
