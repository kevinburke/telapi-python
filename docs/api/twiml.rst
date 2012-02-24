====================
:mod:`telapi_helper.telml`
====================

.. automodule:: telapi_helper.telml

.. autoclass:: telapi_helper.telml.Response
   :members:

Primary Verbs
~~~~~~~~~~~~~

.. autoclass:: telapi_helper.telml.Say
   :members:

.. autoclass:: telapi_helper.telml.Play
   :members:

.. autoclass:: telapi_helper.telml.Dial
   :members:

.. autoclass:: telapi_helper.telml.Gather
   :members:

.. autoclass:: telapi_helper.telml.Record
   :members:

Seconday Verbs
~~~~~~~~~~~~~~

.. autoclass:: telapi_helper.telml.Hangup
   :members:

.. autoclass:: telapi_helper.telml.Redirect
   :members:

.. autoclass:: telapi_helper.telml.Reject
   :members:

.. autoclass:: telapi_helper.telml.Pause
   :members:

.. autoclass:: telapi_helper.telml.Sms
   :members:

Nouns
~~~~~~

.. autoclass:: telapi_helper.telml.Conference
   :members:

.. autoclass:: telapi_helper.telml.Number
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
