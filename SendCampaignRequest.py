

class SendCampaignRequest():

	def __init__(self, email, campaignId, messageId, type, action):
		self.email = email
		self.campaignId = campaignId
		self.messageId = messageId
		self.type = type
		self.action = action

	# Our handy little helper method that will take all of the atrributes of this object, and format it to a json string
	def toJsonDataString(self):

		# Create the string we will use to hold the attributes
		jsonDataString = ''

		# Grab all the attributes on this object
		attributes = self.__dict__.items()

		#Start the string with an open bracket
		jsonDataString = "\n{ \n"

		# Loop through the attribute and make the rest of our json data string with them
		for attribute, value in attributes:
			jsonDataString += ("\t\'%s\' : \'%s\', \n" % (attribute, value))

		#End the string with a close bracket
		jsonDataString += " \n }"

		return(jsonDataString)