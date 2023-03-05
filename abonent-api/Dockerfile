FROM python:3.8-alpine

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apk add git
COPY git_requirements.txt .
RUN pip3 install --no-cache-dir -r git_requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p", "7000"]
