__version_info__ = ('3', '0', '1')
__version__ = '.'.join(__version_info__)

class TelapiException(Exception):
    pass


class TelapiRestException(TelapiException):

    def __init__(self, status, uri, msg=""):
        self.uri = uri
        self.status = status
        self.msg = msg

    def __str__(self):
        return "HTTP ERROR %s: %s \n %s" % (self.status, self.msg, self.uri)
