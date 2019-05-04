# Download base image - using 38 for openssl
FROM poestat/psbase38py3

LABEL AUTHOR="Quinn D Granfor, spootdev@gmail.com"
LABEL Description="This image holds the main server app"

ARG ALPMIRROR
ARG PIPMIRROR

# copy PIP requirements
ADD requirements.txt /poestat
WORKDIR /poestat

RUN sed -i "s/dl-cdn.alpinelinux.org/${ALPMIRROR}/" /etc/apk/repositories \
  && apk add --update \
  alpine-sdk \
  libffi-dev \
  libressl \
  libressl-dev \
  py3-psycopg2 \
  python3-dev \
  && pip3 install --trusted-host ${PIPMIRROR} -i https://${PIPMIRROR}/simple -r requirements.txt \
  && apk del \
  alpine-sdk \
  python3-dev \
  && rm -rf /var/cache/apk/* \
  && rm requirements.txt

ADD wait-for-it-ash.sh /poestat
# Copy the source files for the app
ADD src /poestat

CMD ["/bin/ash"]
