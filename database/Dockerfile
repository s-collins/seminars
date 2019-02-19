from ubuntu

run apt-get update \
    && apt-get install mysql-client -y \
    && apt-get install python3 -y

run apt-get install mysql-client

run apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential
run pip3 install --upgrade pip
run pip3 install mysql-connector-python
run pip3 install SQLAlchemy

workdir workspace
copy app.py .

entrypoint ["python3", "app.py"]
