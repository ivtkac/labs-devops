
+ 19
− 0
FROM python:3.11.14-slim-bookworm AS builder
WORKDIR /usr/src/app
COPY requirements.txt ./

FROM builder AS prod
RUN pip install -r requirements.txt
RUN <<EOF
    groupadd -r flask
    useradd -r -g flask flask
    chown -R flask:flask /usr/src/app
EOF

USER flask

COPY --chown=flask:flask ./ .

EXPOSE 5000

CMD ["python", "./start.py"]