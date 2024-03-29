import logging
import os
from telapi_helper import TelapiException
from telapi_helper.rest.resources import make_request
from telapi_helper.rest.resources import Accounts
from telapi_helper.rest.resources import Applications
from telapi_helper.rest.resources import Calls
from telapi_helper.rest.resources import CallerIds
from telapi_helper.rest.resources import Notifications
from telapi_helper.rest.resources import Recordings
from telapi_helper.rest.resources import Transcriptions
from telapi_helper.rest.resources import Sms
from telapi_helper.rest.resources import Participants
from telapi_helper.rest.resources import PhoneNumbers
from telapi_helper.rest.resources import Conferences
from telapi_helper.rest.resources import Sandboxes
from urllib import urlencode
from urlparse import urljoin


def find_credentials():
    """
    Look in the current environment for Telapi credentails
    """
    try:
        account = os.environ["TWILIO_ACCOUNT_SID"]
        token = os.environ["TWILIO_AUTH_TOKEN"]
        return account, token
    except KeyError:
        return None, None


class TelapiRestClient(object):
    """
    A client for accessing the Telapi REST API
    """

    def request(self, path, method=None, vars=None):
        """sends a request and gets a response from the Telapi REST API

        .. deprecated:: 3.0

        :param path: the URL (relative to the endpoint URL, after the /v1
        :param url: the HTTP method to use, defaults to POST
        :param vars: for POST or PUT, a dict of data to send

        :returns: Telapi response in XML or raises an exception on error

        This method is only included for backwards compatability reasons.
        It will be removed in a future version
        """
        logging.warning(":meth:`TelapiRestClient.request` is deprecated and "
                        "will be removed in a future version")

        vars = vars or {}
        params = None
        data = None

        if not path or len(path) < 1:
            raise ValueError('Invalid path parameter')
        if method and method not in ['GET', 'POST', 'DELETE', 'PUT']:
            raise NotImplementedError(
                'HTTP %s method not implemented' % method)

        if path[0] == '/':
            uri = _TWILIO_API_URL + path
        else:
            uri = _TWILIO_API_URL + '/' + path

        if method == "GET":
            params = vars
        elif method == "POST" or method == "PUT":
            data = vars

        headers = {
            "User-Agent": "telapi-python",
            }

        resp = make_request(method, uri, auth=self.auth, data=data,
                            params=params, headers=headers)

        return resp.content

    def __init__(self, account=None, token=None, base="https://api.telapi.com",
                 version="2010-04-01", client=None):
        """
        Create a Telapi REST API client.
        """

        # Get account credentials
        if not account or not token:
            account, token = find_credentials()
            if not account or not token:
                raise TelapiException("Could not find account credentials")

        auth = (account, token)
        version_uri = "%s/%s" % (base, version)
        account_uri = "%s/%s/Accounts/%s" % (base, version, account)

        self.accounts = Accounts(version_uri, auth)
        self.applications = Applications(account_uri, auth)
        self.calls = Calls(account_uri, auth)
        self.caller_ids = CallerIds(account_uri, auth)
        self.notifications = Notifications(account_uri, auth)
        self.recordings = Recordings(account_uri, auth)
        self.transcriptions = Transcriptions(account_uri, auth)
        self.sms = Sms(account_uri, auth)
        self.phone_numbers = PhoneNumbers(account_uri, auth)
        self.conferences = Conferences(account_uri, auth)
        self.sandboxes = Sandboxes(account_uri, auth)

        self.auth = auth
        self.account_uri = account_uri

    def participants(self, conference_sid):
        """
        Return a :class:`Participants` instance for the :class:`Conference`
        with conference_sid,
        """
        base_uri = "%s/Conferences/%s" % (self.account_uri, conference_sid)
        return Participants(base_uri, self.auth)

