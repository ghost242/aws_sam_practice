FROM python:3.7

# set user root
USER root

# install aws-sam-cli
RUN pip install aws-sam-cli

# connect volumn master directory
RUN mkdir /root/src
VOLUME /root/src
# set cwd to connected dir
WORKDIR /root/src
#
