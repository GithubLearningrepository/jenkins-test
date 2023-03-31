FROM tomcat:latest
MAINTAINER anjali anjali_manocha@fosteringlinux.com
COPY /var/lib/jenkins/workspace/test/target/*.war /usr/local/tomcat/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]
