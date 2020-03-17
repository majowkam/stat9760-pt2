# Part 2

## run.sh
### This script will do the following:
	- use docker-compose to create 3 services in daemon mode (python, elastic search and kibana), and will wait for 60 seconds to ensure all services are running
	- execute a python script that will pass in two required arguments page_size=10000 and num_pages=2 (to pull 20k records of NYC parking violations)
	- these violations will then be dumped into a json file and then sent to the elastic search service
	- before sending to the elastic search service the violation date field will be converted into a date

### Requirements
	- docker service is installed and running

# Part 3
	## Kibana Discover
	![Discover](/img/Kibana_Discover.png)