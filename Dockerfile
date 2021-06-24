FROM python:3.9.5-slim

WORKDIR /opt

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY . /opt/

CMD ["python", "/opt/app.py"]