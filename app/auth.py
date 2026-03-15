API_KEYS = {
    "my_phone": "CHANGE_THIS_SECRET_KEY"
}

def verify_key(key):
    return key in API_KEYS.values()
