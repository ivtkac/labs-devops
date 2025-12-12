docker build -t env_image -f ./Dockerfile.0 .
docker run --rm env_image echo "$MY_ENV"

docker build -t arg_image -f ./Dockerfile.1 .
docker run --rm arg_image echo "$MY_ENV"

docker build -t over_arg_image --build-arg MY_ENV=EPAM -f ./Dockerfile.1 .
docker run --rm over_arg_image echo "$MY_ENV"

docker build -t arg2_image --build-arg CUSTOM_USER=100 ./Dockerfile.2 .
docker run --rm arg2_image id

docker build -t arg2_image --build-arg CUSTOM_USER=999 -f ./Dockerfile.2 .
docker run --rm arg2_image id
