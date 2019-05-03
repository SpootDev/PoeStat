git pull
./source_sync.sh

# must move base dir so the docker-compose commands work
cd ./poestat

docker-compose down

# base python 3 images
cd ./ComposePoeBase38Py3
docker build -t poestat/psbase38py3 --build-arg ALPMIRROR=10.0.0.122 --build-arg PIPMIRROR=pypi.python.org .

cd ../ComposePoeBase39Py3
docker build -t poestat/psbase39py3 --build-arg ALPMIRROR=10.0.0.122 --build-arg PIPMIRROR=pypi.python.org .

# move here so all the "deps" are built first
docker-compose build

# containers here and later are "standalone" with no deps

# nuke old images (commented due to base ffmpeg)
#../../purge_images_none.sh

# retag all the images - need to back out of docker/alpine as well as docker directory for container
./tag_rename_images.sh
