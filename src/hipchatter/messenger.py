import hipchat
import norris

def send_message(api_key, room_id, message):
    hipchat_api = hipchat.HipChat(token=api_key)
    hipchat_api.method('rooms/message', method='POST', parameters={'room_id': room_id, 'from': 'HipChatter', 'message': message})

def send_joke(api_key, room_id):
    joke = norris.get_joke()
    send_message(api_key, room_id, joke)