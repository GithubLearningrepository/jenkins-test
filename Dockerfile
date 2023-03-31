FROM tomcat:latest
MAINTAINER anjali anjali_manocha@fosteringlinux.com
COPY ./sample.war /usr/local/tomcat/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]
