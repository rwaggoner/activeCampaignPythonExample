import json
import requests



# Grab the API credientals we will need for our calls from the property file we setup for this project
from appProperties import API_URL, API_KEY, API_ENDPOINT_ACCOUNT_VIEW

class ApiConnectorTest():
	def __init__(self) :
		self.contentType = 'application/json'
		self.apiKey = API_KEY;
		self.apiUrl = API_URL;

	def testApiConnection(self):

		# Create the URL to the account view as our test endpoint to see if we have this setup correctly
		testUrl = '%s%s' % (API_URL, API_ENDPOINT_ACCOUNT_VIEW);
		testUrl2 = '%s&api_action=group_view&api_output=%s&id=3' % (self.apiUrl, self.output)

		# Take a look at the data we get from making our call to the endpoint
		response = requests.get(testUrl2)

		# Return the data we got from the api call
		return response.json();