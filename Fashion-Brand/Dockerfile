FROM python:3.10.10-slim
LABEL description="Fashion Ner"
COPY . /bio_medical_ner/Fashion-Brand
WORKDIR /bio_medical_ner/Fashion-Brand
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip
EXPOSE 7001
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python",  "app_brand.py"]