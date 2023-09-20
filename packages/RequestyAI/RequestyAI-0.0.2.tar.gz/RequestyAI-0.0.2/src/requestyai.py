import logging
import threading
import uuid
from datetime import datetime, timedelta

import openai
import requests


class ChatbotTracker:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.session_id = None
        self.last_message_time = None

    def get_session_id(self):
        now = datetime.now()
        if self.session_id is None or (now - self.last_message_time) > timedelta(minutes=15):
            self.session_id = str(uuid.uuid4())
            self.last_message_time = now
        return self.session_id

    # An attribute to keep track of consecutive failures in sending the data to the endpoint
    consecutive_failures = 0
  
    def send_data(self, user_message, user_timestamp, bot_message, bot_timestamp, organization_id, engine, ip_address=None, user_url=None):
      data = {
          'session_id': self.get_session_id(),
          'user_message': user_message,
          'user_timestamp': user_timestamp,
          'ip_address': ip_address if ip_address else '192.0.2.0',  # example IP address
          'user_url': user_url if user_url else 'http://example.com/chat',  # example URL
          'bot_message': bot_message,
          'bot_timestamp': bot_timestamp,
          'organization_id': organization_id,
          'engine': engine
      }
      
      # Create a new thread to send the data without blocking the main thread
      threading.Thread(target=self._send_to_endpoint, args=(data,)).start()

    def _send_to_endpoint(self, data):
      print("Sending message to chat endpoint")
      try:
        requests.post(self.endpoint, json=data)
        # Reset the consecutive failures if the request succeeds
        self.consecutive_failures = 0
      except Exception as e:
        self.consecutive_failures += 1
        print(f"Error sending data to endpoint: {e}")
        if self.consecutive_failures >= 5:  # This threshold can be adjusted
          print("Warning: Consecutive failures have reached a threshold. The endpoint may be down.")

tracker = None

def track_completion(endpoint, organization_id, ip_address=None, user_url=None):
    global tracker
    tracker = ChatbotTracker(endpoint)

    # Save the original functions
    original_completion_create = openai.Completion.create
    original_chat_completion_create = openai.ChatCompletion.create

    def wrapper_completion(*args, **kwargs):
        # The prompt is the user's message
        user_message = kwargs.get('prompt', args[0] if args else '')

        # Get the user timestamp before the bot response
        user_timestamp = datetime.now().isoformat()

        # Get the engine used for the completion
        engine = kwargs.get('engine', 'unknown')

        # Call the original function and get the bot's response
        response = original_completion_create(*args, **kwargs)

        # Attempt to extract the bot's message using several different paths
        try:
            bot_message = response['choices'][0]['text'].strip()
        except KeyError:
            try:
                bot_message = response.choices[0].text.strip()
            except KeyError:
                try:
                    bot_message = response['choices'][0]['message']['content'].strip()
                except KeyError:
                    bot_message = ''

        # Get the bot timestamp after the bot response
        bot_timestamp = datetime.now().isoformat()

        # Send the data to the endpoint
        tracker.send_data(user_message, user_timestamp, bot_message, bot_timestamp, organization_id, engine, ip_address, user_url)

        return response
    
    def wrapper_chat_completion(*args, **kwargs):
        # Extract user message
        message_log = kwargs.get('messages', [])
        user_message = message_log[-1]['content'] if message_log and 'content' in message_log[-1] else ''
        user_timestamp = datetime.now().isoformat()
        engine = kwargs.get('model', 'unknown')

        # Call the original function
        response = original_chat_completion_create(*args, **kwargs)

        # Extract bot message
        bot_message = ''
        if response.choices:
            choice = response.choices[0]
            bot_message = choice['message']['content'].strip()

        # Get the bot timestamp
        bot_timestamp = datetime.now().isoformat()

        # Send data to the endpoint
        tracker.send_data(user_message, user_timestamp, bot_message, bot_timestamp, organization_id, engine, ip_address, user_url)

        return response

    # Replace the original functions with our wrappers
    openai.Completion.create = wrapper_completion
    openai.ChatCompletion.create = wrapper_chat_completion