FROM ubuntu

RUN apt-get update && apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN pip3 install pipenv
RUN pip3 install bs4
RUN pip3 install selenium
RUN pip3 install datetime_glob
RUN pip3 install sqlalchemy
RUN pip3 install sqlalchemy-utils
RUN pip3 install python-dateutil
RUN pip3 install PyMySQL

RUN apt-get install wget -y

RUN apt-get install unzip
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

RUN apt-get install curl -y
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

WORKDIR etl
