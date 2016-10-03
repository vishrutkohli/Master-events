

from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests

# Create your views here.

VERIFY_TOKEN = '7thseptember2016'
PAGE_ACCESS_TOKEN = 'EAAJz4ZB0zviUBAJZBslH5fjCxDvWcZBU7Oz2aYcQWNYEaU4GKTHJ01jCg6JlMVCLaZCmvB1Sqis7B0GxQA43whyC7AbroQ94M03nHvnpumpR1MPzkxpYFXa9NEZAw3a0H9ZBESpA0RvsvVmbAZBJzMFvl0wcxl6lVRwfPzTcWOSdgZDZD'
API_token = '85b82a55e643435fb11b903effdb9b3b'

def post_facebook_message(fbid,message_text):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
	
	print status.json()

def post_football_message(text):
	#post_message_url = 'http://api.football-data.org/v1/teams//players/85b82a55e643435fb11b903effdb9b3b+/'

	#response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
	url = 'https://www.googleapis.com/gmail/v1/users/me/labels/'
	
	new_url = url + text + "/?key={YOUR_API_KEY}'"
	req = urllib2.Request(new_url)
	r = urllib2.urlopen(req)
	data = r.read()
	j = json.loads(data)

	#status = requests.post(post_message_url, headers={"Content-Type": "application/json"})
	#print status.json()	
	return j


class MyChatBotView(generic.View):
	def get (self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Oops invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		incoming_message= json.loads(self.request.body.decode('utf-8'))
		print  incoming_message

		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				print message
				try:
					sender_id = message['sender']['id']
					message_text = message['message']['text']
					data = post_football_message(message_text)
					post_facebook_message(sender_id,data[messagesUnread])

					
					

					

							



					 
				except Exception as e:
					print e
					pass

		return HttpResponse()  

def index(request):
	return HttpResponse('Hello world')