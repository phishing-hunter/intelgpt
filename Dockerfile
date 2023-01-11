FROM python:3-bullseye

RUN apt-get update && apt-get install -y dnsutils iputils-ping net-tools whois

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /src /app
COPY *.sh /

ENTRYPOINT ["/entrypoint.sh"]
