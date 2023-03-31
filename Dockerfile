FROM tomcat:latest
MAINTAINER anjali anjali_manocha@fosteringlinux.com
COPY /var/jenkins_home/workspace/test-pipeline/target/*.war /usr/local/tomcat/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]
