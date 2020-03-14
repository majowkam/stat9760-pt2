from datetime import datetime
from elasticsearch import Elasticsearch
import json


def send_to_es(jsonfile:str,esindex:str):
	with open(jsonfile) as f:
		data = json.load(f)
	es = Elasticsearch()
	res = es.index(index=esindex, doc_type='violation', id=1,body=data[0])
	
	
	"""
	url = 'http://192.168.99.100:9200'
	payload = ojson
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	r = requests.post(url, data=payload, headers=headers)
	"""