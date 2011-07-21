.. module:: telapi_helper.rest.resources

=================
Phone Numbers
=================

With Telapi you can search and buy real phones numbers, just using the API.

For more information, see the `IncomingPhoneNumbers REST Resource <http://www.telapi_helper.com/docs/api/rest/incoming-phone-numbers>`_ documentation.


Searching and Buying a Number
--------------------------------

Finding numbers to buy couldn't be easier. We first search for a number in area code 530. Once we find one, we'll purchase it for our account.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    numbers = client.phone_numbers.search(area_code=530)

    if len(numbers) > 0:
        numbers[0].purchase()
    else:
        print "No numbers in 530 available"

Toll Free Numbers
^^^^^^^^^^^^^^^^^^^^^^^^

By default, :meth:`search` looks for local phone numbers. Set :data:`type` to ``tollfree`` to search toll-free numbers instead.

.. code-block:: python

    numbers = client.phone_numbers.search(type="tollfree")


Numbers Containing Words
^^^^^^^^^^^^^^^^^^^^^^^^^^

Phone number search also supports looking for words inside phone numbers. The following example will find any phone number with "FOO" in it.

.. code-block:: python

    numbers = client.phone_numbers.search(contains="FOO")

You can use the ''*'' wildcard to match any character. The following example finds any phone number that matches the pattern ''D*D''.

.. code-block:: python

    numbers = client.phone_numbers.search(contains="D*D")

:meth:`PhoneNumbers.search` method has plenty of other options to augment your search. The `AvailablePhoneNumbers REST Resource <http://www.telapi_helper.com/docs/api/rest/available-phone-numbers>`_ documentation also documents the various search options.


Buying a Number
---------------

If you've found a phone number you want, you can purchase the number

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    number = client.phone_numbers.purchase("+15305431234")

However, it's easier to purchase numbers after finding them using search (as shown in the first example).


Changing Applications
----------------------

An :class:`Application` encapsulates all necessary URLs for use with phone numbers. Update an application on a phone number using :meth:`update`.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    phone_sid = "PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    client = TelapiRestClient()
    number = client.phone_numbers.update(phone_sid, application="AP123")

See :doc:`/usage/applications` for instructions on updating and maintaining Applications.

Validate Caller Id
-----------------------
Telapi Adding a new phone number to your validated numbers is quick and easy

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    response = client.caller_ids.validate("+9876543212")
    print response["validation_code"]

Telapi will call the provided number and wait for the  validation code to be entered.




