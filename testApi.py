from CreateCampaignRequest import CreateCampaignRequest
from SendCampaignRequest import SendCampaignRequest
from CampaignAPIService import CampaignAPIService


# Helper method used to create our create campaign request object
def createCreateCampiangRequest():

	# Set up the params for our create Campaign Request
	type = 'single'
	name = 'Ryans Test Campaign' 

	# We are using a future sent date to satisfy the 'schedule' requirement
	sDate = '2018-10-05 08:40:00' 
	status = '1'
	public = '1'
	tracklinks = 'all'

	# We know that list id 1 will be the test list we creating specifically for this exercise
	p = ['1']
	m = ['100']

	return CreateCampaignRequest(type, name, sDate, status, public, tracklinks, p, m)

# Helper method used to create our send campaign request object
def createSendCampiangRequest():

	# Set up the params for our create Campaign Request
	email = 'ryan@ryan.com'

	# We know that campaign id 1 will be the campaign id of the one we already created, we can just use that instead of doing a look up for this litt example
	campaignId = '1'
	messageId = '1'
	type = 'MIME'
	action = 'send'

	return SendCampaignRequest(email, campaignId, messageId, type, action)

# Method used to call the create code in our servce class
def callCreateCampaignApiEndpoint(CreateCampaignRequest):

	campaignApiService = CampaignAPIService()
	campaignApiService.createCampaign(CreateCampaignRequest)

# Method used to call the send code in our servce class
def callSendCampaignApiEndpoint(SendCampaignRequest):

	campaignApiService = CampaignAPIService()
	campaignApiService.sendCampaign(SendCampaignRequest)


if __name__ == '__main__':

	# Create our create campaign request object
	createCampaignRequest = createCreateCampiangRequest()

	# Use the create campaign request to send to the api end point
	callCreateCampaignApiEndpoint(createCampaignRequest)

	#Create the request to send the campaign
	sendCampaignRequest = createSendCampiangRequest()

	# Use the create campaign request to send to the api end point
	callSendCampaignApiEndpoint(sendCampaignRequest)
	