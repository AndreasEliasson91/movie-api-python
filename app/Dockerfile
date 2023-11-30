FROM python:alpine

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --only-binary :all: -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app:app", "--reload", "--host=0.0.0.0" ]
