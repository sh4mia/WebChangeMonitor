FROM python:3.8

WORKDIR /app

COPY check_web.py .

RUN pip install requests

CMD ["python", "-u", "check_web.py"]
