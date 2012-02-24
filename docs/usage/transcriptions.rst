.. module:: telapi_helper.rest.resources

================
Transcriptions
================

Transcriptions are generated from recordings via the `TwiML <Record> verb <http://www.telapi_helper.com/docs/api/telml/record>`_. Using the API, you can only read your transcription records.

For more information, see the `Transcriptions REST Resource <http://www.telapi_helper.com/docs/api/rest/transcription>`_ documentation.

Listing Your Transcriptions
----------------------------

The following code will print out lengths :attr:`friendly_name` for each :class:`Application`.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    conn = TelapiRestClient()
    for transcription in conn.transcriptions.list():
        print transcription.duration
