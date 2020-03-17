docker-compose up -d
sleep 60s
docker-compose run pyth python main.py 10000 2
#docker-compose down
