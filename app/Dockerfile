FROM python:alpine

WORKDIR /app

ARG MONGODB_URL
ARG DB_NAME

ENV MONGODB_URL=$db_url
ENV DB_NAME=$db_name

COPY .env /app/.env

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN  python3 -m pip install --upgrade pip && \
     python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app:app", "--reload", "--host=0.0.0.0" ]
