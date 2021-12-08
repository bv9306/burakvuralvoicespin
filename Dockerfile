FROM python:3.9.1

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=task_burak_vural.settings

MAINTAINER Burak Vural <burakvural93>
EXPOSE 7000

COPY ./burakvuralvoicespin /burakvuralvoicespin-test/
WORKDIR /burakvuralvoicespin-test
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "init_task_voicespin.sh"]
RUN apt-get update && \
    apt-get install dos2unix
RUN dos2unix init_task_voicespin.sh
ENTRYPOINT ["/bin/sh", "-c" , "init_task_voicespin.sh"]