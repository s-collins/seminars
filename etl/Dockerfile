FROM ubuntu

RUN apt-get update && apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install pipenv

RUN pip3 install bs4
RUN pip3 install selenium
RUN pip3 install datetime_glob
RUN pip3 install sqlalchemy

RUN apt-get install wget -y

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar xvsf geckodriver-v0.24.0-linux64.tar.gz
RUN mv geckodriver /usr/local/bin/

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

RUN pip3 install python-dateutil

WORKDIR etl
