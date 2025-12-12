docker build -t add_url_image -f ./Dockerfile.0 .
docker run --rm add_url_image ls /home

wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.39.0.tar.gz
docker build -t copy_local_image -f ./Dockerfile.1 .
docker run --rm copy_local_image ls /home

docker build -t add_local_image -f ./Dockerfile.2 .
docker run --rm add_local_image ls /home
