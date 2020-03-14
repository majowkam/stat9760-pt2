from sodapy import Socrata
import json
import os

def get_data(apitoken:str, page_size:int, num_pages:int, output:str):
	client = Socrata("data.cityofnewyork.us",apitoken)
	i = 0
	if os.path.exists(output):
		os.remove(output)
	resp = list()
	while i < num_pages:
		resp += client.get("nc67-uf89", limit=page_size, offset=i*page_size)
		i += 1
	if len(output) > 1:
		with open(output, 'a+') as fh:
			fh.write(json.dumps(resp))
	else:
		for item in resp:
			print(str(item))