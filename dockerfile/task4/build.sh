# sub-task 1
docker run --rm nginx:1.23.3 pwd # prints /

docker build -t dir_image -f ./Dockerfile.1 .
docker run --rm dir_image pwd # prints /my-directory

# sub-task 2
docker build -t expose_image -f ./Dockerfile.2 .
docker run --rm expose_image
curl localhost:8080

docker run -p 8080:8080 expose_image
curl localhost:8080

# sub-task 3
docker build -t user_image -f ./Dockerfile.3 .
docker run --rm user_image id
