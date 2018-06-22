FROM centos:latest
MAINTAINER Mariia Tartachna "mtartachna@gmail.com"

RUN yum update -y
RUN yum clean all & yum makecache
RUN yum install -y epel-release python-setuptools
RUN yum install -y python-pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000


#ENTRYPOINT ["python"]
#CMD ["app.py"]

CMD [“python”, “app.py”]