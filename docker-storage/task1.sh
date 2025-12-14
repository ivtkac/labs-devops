container=$(docker run -d -v /opt/docker/storage/task1:/home alpine:3.17)
docker exec "$container" sh -c "echo 'Hello world!' > myfile1 && echo 'Hello from EPAM!' > myfile2; ls -l /home"
rm -f /opt/docker/storage/task1/myfile1
docker exec "$container" ls -l /home
docker volume ls
