====================
:mod:`telapi.twiml`
====================

.. automodule:: telapi.twiml

.. autoclass:: telapi.twiml.Response
   :members:

Primary Verbs
~~~~~~~~~~~~~

.. autoclass:: telapi.twiml.Say
   :members:

.. autoclass:: telapi.twiml.Play
   :members:

.. autoclass:: telapi.twiml.Dial
   :members:

.. autoclass:: telapi.twiml.Gather
   :members:

.. autoclass:: telapi.twiml.Record
   :members:

Seconday Verbs
~~~~~~~~~~~~~~

.. autoclass:: telapi.twiml.Hangup
   :members:

.. autoclass:: telapi.twiml.Redirect
   :members:

.. autoclass:: telapi.twiml.Reject
   :members:

.. autoclass:: telapi.twiml.Pause
   :members:

.. autoclass:: telapi.twiml.Sms
   :members:

Nouns
~~~~~~

.. autoclass:: telapi.twiml.Conference
   :members:

.. autoclass:: telapi.twiml.Number
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
