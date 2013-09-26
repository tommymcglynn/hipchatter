import hipchat

api_key = '7f5bcfce32f121ae98e1e2eba602bb'
room_id = '159382'
hipchat_api = hipchat.HipChat(token=api_keu)
message = 'Test'
hipchat_api.method('rooms/message', method='POST', parameters={'room_id': room_id, 'from': 'HipChatter', 'message': message})
