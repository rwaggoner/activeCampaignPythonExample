import json
import requests

# Grab the API credientals we will need for our calls from the property file we setup for this project
from AppProperties import API_FULL_URL_WITHOUT_ACTION, API_ACTION_URL_PARAM, API_CAMPAIGN_CREATE_ACTION, API_CAMPAIGN_SEND_ACTION, API3_URL, API3_CAMPAIGN_ENDPOINT, API3_API_TOKEN_HEADER, API_KEY
from CreateCampaignRequest import CreateCampaignRequest


# This file will help us with the functions we need to perform to connect to, and call the campaign API end points
class CampaignAPIService():
	def __init__(self) :

		self.headers = {
						'Content-Type': 'application/json',
						'Api-Token': API_KEY
					}
						

	# This method will list out of campaings for us. Not needed, but useful for debugging / confirming results
	def listCampaigns(self):

	    # Create the URL for the list campaign api endpoint
		listCampaignsURL = '%s%s' % (API3_URL, API3_CAMPAIGN_ENDPOINT)

		# Do the post, and see what happens
		response = requests.get(listCampaignsURL, headers=self.headers)

		# Just log the request so we can see how we are doing here
		self.logRequest(listCampaignsURL, self.headers, "", response)


	# This method will be used do call the create campaign endpoint
	def createCampaign(self, CreateCampaignRequest):

		# Create the URL for the create campaign api endpoint
		createCampaignApiURL = '%s?%s%s' % (API_FULL_URL_WITHOUT_ACTION, API_ACTION_URL_PARAM, API_CAMPAIGN_CREATE_ACTION)

		# Get all of the properties of the request object as a json string, to send with our post call
		jsonRequestData = CreateCampaignRequest.toJsonDataString()
		#jsonRequestData = CreateCampaignRequest.getJsonString()

		# Do the post, and see what happens
		response = requests.post(createCampaignApiURL, headers=self.headers, data=jsonRequestData)

		# Just log the request so we can see how we are doing here
		self.logRequest(createCampaignApiURL, self.headers, jsonRequestData, response)

	# This method will be used do call the sending campaign endpoint
	def sendCampaign(self, SendCampaignRequest):

		# Create the URL for the create campaign api endpoint
		sendCampaignApiURL = '%s?%s%s' % (API_FULL_URL_WITHOUT_ACTION, API_ACTION_URL_PARAM, API_CAMPAIGN_SEND_ACTION)

		# Get all of the properties of the request object as a json string, to send with our post call
		jsonRequestData = SendCampaignRequest.toJsonDataString()

		# Do the post, and see what happens
		response = requests.post(sendCampaignApiURL, headers=self.headers, data=jsonRequestData)

		# Just log the request so we can see how we are doing here
		self.logRequest(sendCampaignApiURL, self.headers, jsonRequestData, response)


	# Small helper method to do the logging of our requests / responses for us
	def logRequest(self, url, headers, data, response):
		print('API Call URL: %s' % url)
		print('API Call Headers: %s' % headers)
		print('API Call Data: %s' % data)
		print('API Call Response: %s' % response)
		print('\n\n\n')

