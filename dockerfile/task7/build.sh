docker run -d --name registry -p 5000:5000 --restart=always registry:2
docker pull alpine:3.17
docker tag alpine:3.17 localhost:5000/my-alpine
docker push localhost:5000/my-alpine
docker rmi localhost:5000/my-alpine alpine:3.17
docker pull localhost:5000/my-alpine
