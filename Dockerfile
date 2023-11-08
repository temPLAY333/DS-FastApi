FROM python:3-alpine

RUN apk update
RUN apk add git
RUN git clone https://github.com/temPLAY333/DS-FastApi.git

WORKDIR /DS-FastApi
COPY run.py /run.py
RUN pip install -r requirements.txt \
    && 

ENTRYPOINT ["/run.py"]
