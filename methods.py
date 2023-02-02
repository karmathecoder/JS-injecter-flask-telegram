import requests

api_key = "5873986871:AAHiLRAY_5-NLRRlw1ma-7ui5_jXnR3taVI"


def send_msg(msg):
    endpoint = f"https://api.telegram.org/bot{api_key}/sendMessage"
    chat_id = "2065924254"
    parameters = {'chat_id':chat_id,'text':msg}
    requests.get(url = endpoint, params = parameters)

