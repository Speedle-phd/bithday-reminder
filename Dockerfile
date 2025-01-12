FROM python:3.13.0-slim

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

COPY . .

CMD [ "python", "main.py" ]
