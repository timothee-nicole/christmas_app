all:
	flask run

docker-build:
	docker build -t christmas-list .

docker-run: 
	docker run -p 5000:5000 christmas-list
