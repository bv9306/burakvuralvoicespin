INSTALLATION STEPS

Assuming that docker and docker-compose installed on Ubuntu and enabled,running state
(Otherwise follow the instructions in https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=94798094)

1-) Download repository "git clone https://github.com/bv9306/burakvuralvoicespin.git"
2-) In order to build new image please follow instructions in "docker-image-build-instructions.txt"

NOTE : This cannot be required because latest image have already been pushed to dockerhub so
if you run only projects please make next step only

3-) In order to run already pushed image you can follow "docker-compose-run-instructions"



WORKING PRINCIPLES OF PROJECT

1-) Project have been written with Python Django Rest Framework
2-) Best operating system is to run project on Docker is Ubuntu
3-) These project contains postgresql in order to satisfy background tasks for heavy operations(imitation with sleep method) and redis
to cache requests and return end-user with response as soon as possible
4-) Gunicorn has been chosen as run-server for this project in order to create "worker-processes"
5-) Redis supports flexible data structures,simple to use,satisfy high availability ,also supports cache mechanism which is called celery in django so 
all of these reasons can explain why redis have been chosen at this project