# server
cp -R ../source/common ../docker/alpine/ComposeMediaKrakenServer/src/.
cp -R ../source/database ../docker/alpine/ComposeMediaKrakenServer/src/.
cp ../source/main_server.py ../docker/alpine/ComposeMediaKrakenServer/src/.

# webserver
cp -R ../source/common ../docker/alpine/ComposeMediaKrakenWebServer/src/.
cp -R ../source/database ../docker/alpine/ComposeMediaKrakenWebServer/src/.
cp -R ../source/web_app ../docker/alpine/ComposeMediaKrakenWebServer/src/.
