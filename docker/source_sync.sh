# server
cp -R ../source/common ../docker/alpine/ComposePoeServer/src/.
cp -R ../source/database ../docker/alpine/ComposePoeServer/src/.
cp ../source/main_server.py ../docker/alpine/ComposePoeServer/src/.

# webserver
cp -R ../source/common ../docker/alpine/ComposePoeWebServer/src/.
cp -R ../source/database ../docker/alpine/ComposePoeWebServer/src/.
cp -R ../source/web_app ../docker/alpine/ComposePoeWebServer/src/.
