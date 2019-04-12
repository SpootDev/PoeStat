# Download base image
FROM poestat/poestatbase38py3

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
  py3-psycopg2 \
  #py3-service_identity \
  #py3-requests \
  #py3-setuptools \
  && pip3 install --trusted-host ${PIPMIRROR} -i https://${PIPMIRROR}/simple -r requirements.txt \
  && apk del \
  alpine-sdk \
  && rm -rf /var/cache/apk/* \
  && rm requirements.txt

ADD wait-for-it-ash.sh /poestat
# Copy the source files for the app
ADD src /poestat

CMD ["/bin/ash"]
