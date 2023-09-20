Python Integration
Documentation
Overview
This Python library, requesty, tracks user and AI interactions for chatbots that use the OpenAI API. The library captures and sends the following data to the specified endpoint:

session_id: A unique identifier for a session.
user_message: The message that the user sends to the AI.
user_timestamp: The timestamp of when the user message is sent.
bot_message: The message that the AI sends back to the user.
bot_timestamp: The timestamp of when the AI responds.
engine: The type of OpenAI engine used in the interaction, such as "davinci" or "gpt-3.5-turbo".
ip_address: The IP address of the user (optional).
user_url: The URL from which the user is interacting with the chatbot (optional).
Installation
To use the requesty, you must first import the track_completion function at the top of your Python file:

from requesty import track_completion

Then, you call track_completion with the URL of your endpoint:

track_completion('https://your-endpoint-url.com')

This code must be placed before your chat interaction code. You only need to call track_completion once.

Usage
There are two main ways to use the requesty library, depending on whether or not you want to track the ip_address and user_url:

Basic Usage (without ip_address and user_url): For basic usage, all you need to do is call the track_completion function with your endpoint:

from requesty import track_completion 

track_completion('https://your-endpoint-url.com')

Advanced Usage (with ip_address and user_url): If you want to track the ip_address and user_url, you need to extract these values in your chat function (e.g., chat()) and pass them to track_completion:

from flask import request
from requesty import track_completion 

@app.route('/api/chat', methods=['POST'])
def chat():
    user_url = request.headers.get('Referer', 'N/A')
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    track_completion('https://your-endpoint-url.com', ip_address=ip_address, user_url=user_url)


This code attempts to extract the Referer and X-Forwarded-For headers from the incoming HTTP request. If these headers aren't available, it uses default values ('N/A' for user_url and the client's IP address for ip_address).

Diagram
The following diagram provides a high-level overview of how the library works:

 User Message
        |
        v
OpenAI API <-- Requesty Library captures 'user_message', 'user_timestamp', and 'engine'
        |
        v
  AI Response
        |
        v
 Requesty Library captures 'bot_message' and 'bot_timestamp', then sends all data to the endpoint


Please note: This library is designed to work with OpenAI's Python library and it modifies the behavior of openai.Completion.create to capture data. Make sure you import and initialize chatbot_library before you use openai.Completion.create in your code.

