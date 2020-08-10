FROM python:slim-stretch

WORKDIR /srv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make

ADD . /srv

ADD requirements.txt /srv/

RUN pip install -U pip && pip install -r requirements.txt

ENTRYPOINT ["bash", "app.sh"]