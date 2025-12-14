docker run -d --name tmpfs_container \
  --mount type=tmpfs,destination=/my_folder1 \
  -v /tmp:/my_folder2 \
  nginx:1.23

docker inspect tmpfs_container >/tmp/container_inspect.json
cat /tmp/container_inspect.json

docker inspect -f '{{json .Mounts}}' tmpfs_container | jq '.' >/tmp/mounts_config.json
cat /tmp/mounts_config.json

docker inspect -f '{{json .HostConfig.Tmpfs}}' tmpfs_container | jq '.' >/tmp/tmpfs_config.json
cat /tmp/tmpfs_config.json

docker exec tmpfs_container sh -c \
  "dd if=/dev/zero of=/my_folder1/speed_file bs=512M count=1 2>&1 | tee /my_folder1/result"

docker exec tmpfs_container sh -c \
  "dd if=/dev/zero of=/my_folder2/speed_file bs=512M count=1 2>&1 | tee /my_folder2/result"

docker exec tmpfs_container cat /my_folder{1,2}/result

docker stop tmpfs_container
docker rm tmpfs_container
