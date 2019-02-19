from ubuntu

run apt-get update \
    && apt-get install mysql-client -y \
    && apt-get install python -y

run apt-get install mysql-client

run apt-get install -y \
    python-pip \
    python-dev \
    build-essential
run pip install --upgrade pip
run pip install mysql-connector-python

workdir workspace
copy app.py .

entrypoint ["python", "app.py"]
