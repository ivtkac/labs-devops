docker build -t opt_image -f ./Dockerfile.1 .
docker history opt_image

docker build -t opt_image2 - ./Dockerfile.2 .
docker history opt_image2
