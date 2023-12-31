FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -yq curl wget

WORKDIR /app
# скачиваем модель, что бы не хранить в гит репозитории такой объем (45 Мб)
RUN wget -O pytorch_model.bin https://huggingface.co/cointegrated/rubert-tiny-toxicity/resolve/main/pytorch_model.bin?download=true
RUN mkdir /app/model && mv pytorch_model.bin /app/model/

COPY ./requirements.txt /app

COPY ./model /app/model
COPY ./tokenizer /app/tokenizer
COPY ./app.py /app

RUN pip install --no-cache-dir torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]