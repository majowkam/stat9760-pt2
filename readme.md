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

## Kibana Visualize
![Visualize1](/img/Kibana_Visualize_StateCounty.png)
visualizing the count of tickets by county and driver state is interesting because we can expect that counties with neighboring states may show other states with significant violations.
Here it is interesting to see PA with violations in county K.  It is not clear which county K represents (maybe Staten Island?).

![Visualize2](/img/Kibana_Visualize_State.png)
This visualization is interesting because we can see what portion of the total violations come from a certain state's drivers.  CT, PA, NJ and NY all make sense, however it is interesting to see Florida with more violations than CT.
I suspect this may be due to New Yorkers with multi state residences registering their car to Florida for insurance purposes.

## Kibana Dashboard
![Dashboard](/img/Kibana_Dashboard.png)

