FROM tomcat:latest
MAINTAINER anjali anjali_manocha@fosteringlinux.com
COPY --from=build ${WORKSPACE}/test/target/sparkjava-hello-world-1.0.war /usr/local/tomcat/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]
