# Sample app

The repo has three applciatoon on is rabbit mq server running on docker and another is python app using stomp to send messages to mq
and other java app

Got the source code form github for smaple python app java app wont work as have used some sample  pom.xml and smaple code


# each of the fodlers have thier opwn docker files and versions

## rabbit mq:
docker file uses condfig that can comuncate over stomp


```
cd rabbitmq
docker build . -t mq_stomp_server
docker container run -it -d --name rabbitmq-stomp1 -p 15672:15672 -p 5672:5672 -p 61613:61613 mq_stomp_server
```


## Python app

The app is build on  Flask and uses stomp package  to send messages  to mq
The STOMP_HOST and STOMP_PORT are passed as env vars

```
cd python-app
docker build . -t python_app
docker container run -it -d -e STOMP_HOST=host -e STOMP_PORT=port  --name python_app -p 8000:8000  python_app
```



# Java app
The app is build using springboot and maven as build tool

The app uses multi stage dockerfile to b uild the jar and jar is used in final docker stage the port is exposed on 8080

The build stage include unit tests and sonarqube assuming we have sonarqube for coide quaklity checks the sonarqube url and token can be passed as build arg and if build succesful then only image will created


```
cd java-app
docker build . -t java_app
docker container run -it -d  --name java_app -p 8080:8080  java_app
```
