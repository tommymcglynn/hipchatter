import hipchat

def send_message(api_key, room_id, message):
    hipchat_api = hipchat.HipChat(token=api_key)
    hipchat_api.method('rooms/message', method='POST', parameters={'room_id': room_id, 'from': 'HipChatter', 'message': message})
