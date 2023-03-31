FROM tomcat:latest
MAINTAINER anjali anjali_manocha@fosteringlinux.com
COPY $JENKINS_HOME/workspace/my-jobname/target/*.war /usr/local/tomcat/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]
