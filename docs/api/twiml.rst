====================
:mod:`telapi_helper.twiml`
====================

.. automodule:: telapi_helper.twiml

.. autoclass:: telapi_helper.twiml.Response
   :members:

Primary Verbs
~~~~~~~~~~~~~

.. autoclass:: telapi_helper.twiml.Say
   :members:

.. autoclass:: telapi_helper.twiml.Play
   :members:

.. autoclass:: telapi_helper.twiml.Dial
   :members:

.. autoclass:: telapi_helper.twiml.Gather
   :members:

.. autoclass:: telapi_helper.twiml.Record
   :members:

Seconday Verbs
~~~~~~~~~~~~~~

.. autoclass:: telapi_helper.twiml.Hangup
   :members:

.. autoclass:: telapi_helper.twiml.Redirect
   :members:

.. autoclass:: telapi_helper.twiml.Reject
   :members:

.. autoclass:: telapi_helper.twiml.Pause
   :members:

.. autoclass:: telapi_helper.twiml.Sms
   :members:

Nouns
~~~~~~

.. autoclass:: telapi_helper.twiml.Conference
   :members:

.. autoclass:: telapi_helper.twiml.Number
   :members:

Constants
~~~~~~~~~

Many TwiML verbs accept only certain values for specific attributes, such as :data:`MAN` and :data:`WOMAN` for voices.

Voices
>>>>>>
.. data:: MAN
.. data:: WOMAN

Languages
>>>>>>>>>
.. data:: ENGLISH
.. data:: SPANISH
.. data:: FRENCH
.. data:: GERMAN

HTTP Method
>>>>>>>>>>>
.. data:: GET
.. data:: POST

Rejection Reasons
>>>>>>>>>>>>>>>>>
.. data:: REJECTED
.. data:: BUSY
