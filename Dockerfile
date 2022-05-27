FROM alpine

RUN apk update && \ 
    apk add openjdk17-jdk python3 py3-pip gcc g++ py3-wheel py3-setuptools python3-dev

RUN python3 -m ensurepip

RUN pip install --upgrade pip setuptools

RUN pip install jaydebeapi prometheus_client
    
RUN mkdir /projeto

WORKDIR /projeto

COPY database/ database/
COPY network/ network/
COPY main.py .
COPY ./entrypoint.sh /projeto/

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
ENV PATH=$PATH:$JAVA_HOME/bin

ENTRYPOINT ["/projeto/entrypoint.sh"]
