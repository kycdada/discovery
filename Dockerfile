FROM ubuntu
MAINTAINER koyama

# setup bin
RUN apt-get update && apt-get install -y \
    wget\
    python:2.7\
    curl\
    git\
    vim\
    #openjdk-8-jdk\
    rsyslog.d\
    auditd\
    sudo

# install pip 
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

# ADD Requirements
ADD ./requirements.txt .
RUN pip install -r requirements.txt

# ADD Crawler
#ADD ./crawler_2.1.5_all.deb .
#RUN dpkg -i crawler_2.1.5_all.deb

# ADD mysql-connectorj
#ADD ./mysql-connector-java_8.0.14-1ubuntu18.10_all.deb /opt/ibm/crawler/connectorFramework/crawler-connector-framework-0.1.18/lib/java/database

ADD rsystest.conf /etc/rsyslog.d

RUN touch \ 
    /var/log/yesy.log\
    /var/log/user.log\
    /var/log/kern.log\
    /var/log/daemon.log\
    /var/log/mail.log\
    /var/log/lpr.log\
    /var/log/syslog.log

#COPY . .

