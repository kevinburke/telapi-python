from setuptools import setup, find_packages
setup(
    name = "telapi",
    version = "3.0.1",
    description = "Tel API client and TwiML generator",
    author = "Telapi",
    author_email = "help@telapi.com",
    url = "http://github.com/telapi/telapi-python/",
    keywords = ["telapi","twiml"],
    install_requires = ["httplib2"],
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony"
        ],
    long_description = """\
    Python Telapi Helper Library
    ----------------------------

    DESCRIPTION
    The Telapi REST SDK simplifies the process of makes calls to the Telapi REST.
    The Telapi REST API lets to you initiate outgoing calls, list previous calls,
    and much more.  See http://www.github.com/telapi/telapi-python for more information.

     LICENSE The Telapi Python Helper Library is distributed under the MIT
    License """ )
