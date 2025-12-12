docker build -t cmd_image -f ./Dockerfile.1
docker run --rm cmd_image

docker build -t entrypoint_image -f ./Dockerfile.2
docker run --rm entrypoint_image

docker build -t combine_image -f ./Dockerfile.3
docker run --rm combine_image
