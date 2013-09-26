import unittest
from hipchatter import messenger

class GeneralTest(unittest.TestCase):

    def test_message(self):
        api_key = '7f5bcfce32f121ae98e1e2eba602bb'
        room_id = '159382'
        message = 'Hello'
        messenger.send_message(api_key, room_id, message)
