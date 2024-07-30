# env file -- dot env ffile used ot store the all credential
# how to do you store your passwrds and credentials in the framework
# pip install python-dotenv

from dotenv import load_dotenv

import os


def test_update_id():
    load_dotenv()
    url = os.getenv("url")
    print(url)












