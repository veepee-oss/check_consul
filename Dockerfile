FROM vpgrp/alpine:latest

RUN mkdir /project && \
    apk --no-cache add python3 && \
    python3 -m pip install consulate

WORKDIR /project

COPY check_consul_service.py /project

ENTRYPOINT [ "python3", "check_consul_service.py" ]
