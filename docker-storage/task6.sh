docker volume create sidecar_volume
docker run -d --name producer -v sidecar_volume:/home alpine:3.17 sh -c 'while sleep 5; do echo "Hello from EPAM!" >> /home/logs; done'

docker run -d --name consumer -v sidecar_volume:/opt alpine:3.17 tail -f /opt/logs
