FROM alpine:3.4

RUN apk --update add --no-cache python3 && \
    rm -f /var/cache/apk/APKINDEX*

RUN python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN mkdir /euler

COPY requirements.txt /euler

WORKDIR /euler

RUN pip install -r requirements.txt

COPY ./ /euler/

CMD nosetests
