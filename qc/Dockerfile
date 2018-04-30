FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install gunicorn3 -y

COPY . /QuantifyingCorruption
WORKDIR /QuantifyingCorruption


RUN pip3 install -r requirements.txt
ENTRYPOINT ["gunicorn3"]
CMD ["--bind", "0.0.0.0:8000", "qc.wsgi:application"]

