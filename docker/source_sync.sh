# server
cp -R ../source/common ../docker/poestat/ComposePoeServer/src/.
cp -R ../source/database ../docker/poestat/ComposePoeServer/src/.
cp ../source/main_*.py ../docker/poestat/ComposePoeServer/src/.

# webserver
cp -R ../source/common ../docker/poestat/ComposePoeWebServer/src/.
cp -R ../source/database ../docker/poestat/ComposePoeWebServer/src/.
cp -R ../source/web_app ../docker/poestat/ComposePoeWebServer/src/.
