docker build -t multi_image .

docker run -d -p 8999:8999 --name golang_app multi_image

curl http://localhost:8999/hello

docker history multi_image

docker inspect multi_image
