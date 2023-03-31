FROM tomcat:latest
MAINTAINER anjali anjali_manocha@fosteringlinux.com
COPY $JENKINS_HOME/jobs/${jobName}/${buildNumber}/artifact/target/sparkjava-hello-world-1.0.war /usr/local/tomcat/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]
