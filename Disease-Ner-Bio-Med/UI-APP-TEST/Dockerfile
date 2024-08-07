FROM python:3.10.10-slim
LABEL description="Disease Ner"
COPY . /UI-APP-TEST
WORKDIR /UI-APP-TEST
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip
EXPOSE 7001
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python",  "inference.py"]