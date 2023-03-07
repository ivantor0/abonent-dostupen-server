FROM python:3.8-alpine

RUN apk update && apk add python3-dev \
                          gcc \
                          git \
                          libc-dev \
                          libffi-dev

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "run.py"]
