docker build -t my_own_image .
docker tag my_own_image my_new_image:1.0.0
docker run --rm my_own_image nginx -t
