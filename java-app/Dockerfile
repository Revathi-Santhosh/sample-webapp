FROM maven:3.9.6 as build
ARG VERSION=1.0.0
ARG SONAR_URL
ARG SONAR_TOKEN
WORKDIR app
COPY app/ .
RUN  mvn test
# RUN mvn sonar:sonar -Dsonar.host.url=$SONAR_URL -Dsonar.login=$SONAR_TOKEN -Dsonar.qualitygate.wait=true
RUN  mvn package

FROM openjdk:11
COPY --from=build /app/target/my-spring-boot-app.jar /usr/app/my-spring-boot-app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/app/my-spring-boot-app.jar"]
