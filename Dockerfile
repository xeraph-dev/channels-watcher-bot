FROM python:3.10.7-alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY prisma .
RUN prisma generate

COPY locales .
COPY lib .
COPY main.py .

CMD ["python", "main.py"]
