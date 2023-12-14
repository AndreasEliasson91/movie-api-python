FROM python:alpine

WORKDIR /app

COPY .env /app/.env

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN  python3 -m pip install --upgrade pip && \
     python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--reload", "--host=0.0.0.0" ]
