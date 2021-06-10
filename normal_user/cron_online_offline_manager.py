import requests

url = "https://teamconnecthub.net/cron_request"

try:
	req_obj = requests.post(url)
	print(req_obj)
except:
	pass