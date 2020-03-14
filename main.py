from src import opcv, es
import sys
import os
from datetime import datetime as dt

temp_path = "app//_temp//"
temp_json = dt.now().strftime('%Y%m%d.%M%S') + '_temp.json'

def main(page_size:int, num_pages:int=1, output:str=temp_path + temp_json, esindex:str='index-default'): 
	opcv.get_data(apitoken, int(page_size), int(num_pages), output)
	es.send_to_es(output, esindex)

def temp_dir(temppath):
	if not os.path.exists(temppath):
		os.makedirs(temppath)
		return True
	return False

if __name__ == "__main__":
	args   = sys.argv[1:]
	madetempdir = temp_dir(temp_path)
	apitoken = os.environ['APIKEY']
	main(*args)
	if os.path.exists(temp_path + temp_json):
		os.remove(temp_path + temp_json)
	if madetempdir:
		os.rmdir(temp_path)