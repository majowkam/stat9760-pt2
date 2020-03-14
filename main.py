from src import opcv, es
import sys
import os
import requests

def main(page_size:int, num_pages:int=1, output:str='app//temp.json', esindex:str='index-violation'): 
	opcv.get_data(apitoken, int(page_size), int(num_pages), output)
	es.send_to_es(output, esindex)
	
	
	
if __name__ == "__main__":
	args   = sys.argv[1:]
	apitoken = os.environ['APIKEY']
	main(*args)
	