FROM python:latest

MAINTANER Jin Malm "jin_foong@hotmail.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
