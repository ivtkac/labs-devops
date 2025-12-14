docker run -d --name backup_container -v /etc/nginx nginx:1.23
mkdir -p /opt/docker/storage/task5

docker run --rm \
  --volumes-from backup_container \
  -v /opt/docker/storage/task5:/backup \
  alpine:3.17 \
  tar cvf /backup/backup.tar /etc/nginx

tar -tvf /opt/docker/storage/task5/backup.tar

docker run -d --name restore_container -v /etc/nginx alpine:3.17 sleep infinity

docker run --rm --volumes-from restore_container -v /opt/docker/storage/task5:/backup alpine:3.17 tar xvf /backup/backup.tar --strip 2 -C /etc/nginx
