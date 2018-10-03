First attempt at writing a Python application that actually does a meaningful amount of work, that is not used in a Raspberry Pi.

There are, I am sure, a lot of obvious mistakes, formatting issues, and all around puzzling when looking at this code, if you know anything about how to code with Python.

I used Sublime Text for the first time, and did not invest any time into looking for Python plugins, which almost certainly, would have helped me create better looking code.

I am also aware that my method naming is wrong as well. I started reading about this a little bit, to get a better idea, but has not updated them all yet.

So here you have it, a Java developer's attempt at writing Python for the first time, using an "IDE" for the first time.

# [testApi.py](testApi.py)
This is the main file used for running the app. It will simply create a couple of request objects that will be used to make some of our api calls.

# [CampaignAPIService.py](CampaignAPIService.py)
This is the file used to make our calls to the API. In this class, we will create the calls with the appropiate URLs, request parameters, and get the responses.

This class also, currently has logging (printing) for all calls.

# [CreateCampaignRequest.py](CreateCampaignRequest.py)
This is our create campaign request object. Used to help us store and pass around the values that will be used in the create call.

This class also includes a small helper method used to return all of the attributes and values in the object as a formatted json string.

# [SendCampaignRequest.py](SendCampaignRequest.py)
This is our send campaign request object. Used to help us store and pass around the values that will be used in the create call.

This class also includes a small helper method used to return all of the attributes and values in the object as a formatted json string.

# [AppProperties.py](AppProperties.py)
This is the file used to store a lot of the properties used in the app. Mostly API constants.
