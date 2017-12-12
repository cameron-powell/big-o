def response(title, message, session_attributes={}, end_session=True):
    # Build the speech
    speech = {
        'type': 'PlainText',
        'text': message
    }
    # Build the card
    card = {
        'type': 'Simple',
        'title': title,
        'content': message
    }
    # Build the content of the overall response
    content = {
        'outputSpeech': speech,
        'card': card,
        'shouldEndSession': end_session
    }
    # Build the response
    response = {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': content
    }
    # Return the response
    return response


# Routers
def handle_launch_request():
    intro_phrase = 'Hello, I\'m Big O.'
    return response('Hello', intro_phrase)


def handle_intent_request(event, context):
    pass


def handle_session_ended_request():
    pass


# MAIN
def lambda_handler(event, context):
    # Get the type of request from the event
    request_type = event['request']['type']
    # Route based on the type of request
    if request_type == 'LaunchRequest':
        return handle_launch_request()
    elif request_type == 'IntentRequest':
        handle_intent_request(event, context)
    else:
        # The only option at this point is a SessionEndedRequest
        handle_session_ended_request()
