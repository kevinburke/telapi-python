from telapi_helper.rest import TelapiRestClient

def test_client_init():
    telapi = TelapiRestClient("AC123", "SECRET")
