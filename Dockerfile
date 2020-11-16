FROM python:3.6-slim-stretch
COPY requirements.txt /opt/requirements.txt
RUN pip3 install --no-cache-dir -r /opt/requirements.txt
COPY . /opt/
WORKDIR /opt
ENTRYPOINT ["./entrypoint.sh"]