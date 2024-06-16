import requests
import time

# A class used to interact with the 2Captha API.
class 2Captcha:
	# Creates a new instance of the 2Capcha API.
	def __init__(self, key):
		# Sets the API key for the class.
		self.key = key

	# Solves the given captcha.
	def solve_captcha(self, method, googlekey, pageurl):
		# Constructs the API query.
		params = {'key': key, 'method': method, 'googlekey': googlekey, 'pageurl': pageurl, 'json': 1}
		# Sends the query to the API.
		result = requests.get("http://2captcha.com/in.php", params=params)
		# Checks the result status
		# Converts the result to json
		result = result.json()
		# Ensures a successful submittion.
		if result['status']:
			# Response loop.
			while True:
				# Gets the captcha response.
				response = get_captcha_response(result['request'])
				# Validates the response.
				if response != "CAPCHA_NOT_READY":

	# Gets the response of a captcha resolution.
	def get_captcha_response(self, id):
		# Constructs the API query.
		params = {'key': key, 'action': 'get', 'id': id, 'json': 1}
		# Sends the query to the API.
		result = requests.get("http://2captcha.com/res.php", params=params)
		# Checks the result status
		# Converts the result to json
		result = result.json()
		# Returns the response
		return result['captcha']


# creates a new session
with session as requests.session():
	# gets the site cookies
	session.get("https://www.quora.com")

if __name__ == '__main__':
	# Creates a new instance of the 2Captcha API bot.
	captcha = 2Captcha("")
	# Solves the captcha.
	captcha.solve_captcha("userrecaptcha", "", "")