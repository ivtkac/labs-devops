docker volume create my_volume
docker run -d --name mypostgres2 -e POSTGRES_PASSWORD=mysecretpassword \
  -v my_volume:/var/lib/postgresql/data/ postgres:15.1
docker run --name myalpine2 --volumes-from mypostgres2 alpine:3.17
