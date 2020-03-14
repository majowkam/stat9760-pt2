from datetime import datetime as dt
from elasticsearch import Elasticsearch
import json


def send_to_es(jsonfile:str,esindex:str):
	with open(jsonfile) as f:
		data = json.load(f)
	data = field_to_date(data[:],'issue_date','%m/%d/%Y')
	es = Elasticsearch()
	for i in range(len(data)):
		es.index(index=esindex, doc_type='violation', id=i,body=data[i])
	
def field_to_date(listdata:list,fieldname:str,dateformat:str):
	for row in listdata[:]:
		row['issue_date'] = dt.strptime(row[fieldname],dateformat)
	return listdata