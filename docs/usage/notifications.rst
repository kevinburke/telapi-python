.. module:: telapi_helper.rest.resources

====================
Notifications
====================

For more information, see the `Notifications REST Resource <http://www.telapi_helper.com/docs/api/rest/notification>`_ documentation.

Listing Your Notifications
----------------------------

The following code will print out additional information about each of your current :class:`Notification` resources.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    for notification in client.notifications.list():
        print notification.more_info

You can filter transcriptions by :attr:`log` and :attr:`message_date`. The :attr:`log` value is 0 for `ERROR` and 1 for `WARNING`.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()

    ERROR = 0

    for notification in client.notifications.list(log=ERROR):
        print notification.error_code

.. note:: Due to the potentially voluminous amount of data in a notification, the full HTTP request and response data is only returned in the :class:`Notification` instance resource representation.

Deleting Notifications
------------------------

Your account can sometimes generate an inordinate amount of :class:`Notification` resources. The :class:`Notifications` resource allows you to delete unnecessary notifications.

.. code-block:: python

    from telapi_helper.rest import TelapiRestClient

    client = TelapiRestClient()
    client.notifications.delete("NO123")
