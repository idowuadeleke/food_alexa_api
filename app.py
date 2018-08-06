import requests
from flask import Flask,Response
from flask_ask import Ask, statement, question, session
import json

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def launch():
    speech_text = "Welcome to Food dashboard "
    return question(speech_text)


@ask.intent("UsersIntent")
def Users():
    intent="UsersIntent"
    ans=message(intent)
    return question(ans)

@ask.intent("SingleUserIntent",mapping={'name': 'name'})
def SingleUser(name):
    intent="SingleUserIntent"
    ans=name_message(name,intent)
    return question(ans)

@ask.intent("SingleUserOrdersIntent",mapping={'name': 'name'})
def SingleUserOrders(name):
    intent="SingleUserOrdersIntent"
    ans=name_message(name,intent)
    return question(ans)

@ask.intent("ItemsAvailIntent")
def ItemsAvailIntent():
    intent="ItemsAvailIntent"
    ans=message(intent)
    return question(ans)

@ask.intent("ItemsNotAvailIntent")
def ItemsNotAvailIntent():
    intent="ItemsNotAvailIntent"
    ans=message(intent)
    return question(ans)

@ask.intent("SingleItemOrdersIntent",mapping={'item': 'item'})
def SingleItemOrders(item):
    intent="SingleItemOrdersIntent"
    ans=item_message(item,intent)
    return question(ans)
    
@ask.intent("OrdersIntent")
def OrdersIntent():
    intent="OrdersIntent"
    ans=message(intent)
    return question(ans)



@ask.intent('AMAZON.HelpIntent')
def help():
   speech_text = "you can ask for operaional data by saying show operational data"
   return question(speech_text).reprompt(speech_text)

@ask.intent("AMAZON.CancelIntent")
def cancel():
   speech_text="bye, have a nice day"
   return statement(speech_text)


@ask.intent("AMAZON.FallbackIntent")
def fallback():
   speech_text="unable to process your request, please try again with another word"
   return question(speech_text)

@ask.intent("AMAZON.StopIntent")
def Stop():
   speech_text="bye, have a nice day"
   return statement(speech_text)

def message(intent):
    headers={'content-type':'application/json'}
    payload={'intent':intent}
    r = requests.post('http://alexa-voice-core.test.vggdev.com/api/ServiceCall',
    data=json.dumps(payload), headers=headers)
    if r.status_code != 200:
        return 'error'
    else:
        return str(r.text)


def item_message(item,intent):
    headers={'content-type':'application/json'}
    val={'name':item}
    payload={'Data':val,'intent':intent}
    r = requests.post('http://alexa-voice-core.test.vggdev.com/api/ServiceCall',
     data=json.dumps(payload), headers=headers)
    if r.status_code != 200:
        return 'error'
    else:
        return str(r.text)

def name_message(name,intent):
    headers={'content-type':'application/json'}
    val={'username':name}
    payload={'Data':val,'intent':intent}
    r = requests.post('http://alexa-voice-core.test.vggdev.com/api/ServiceCall', 
    data=json.dumps(payload), headers=headers) 
    if r.status_code != 200:
        return 'error'
    else:
        return str(r.text)


if __name__ == '__main__':
   app.run(debug=True)