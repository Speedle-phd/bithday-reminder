FROM python:3.13.0-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

# Ensure log directory exists
RUN mkdir -p log

CMD [ "python3", "main.py" ]
