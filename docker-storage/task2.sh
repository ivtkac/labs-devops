container=$(docker run -d --name mypostgres -e POSTGRES_PASSWORD=mysecretpassword postgres:15.1)
docker inspect "$container"
volume=$(docker volume ls)
docker volume inspect "$volume"
docker run --name myalpine --volumes-from mypostgres alpine:3.17
