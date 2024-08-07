FROM python:3.10.10-slim
LABEL description="Bio Med Ner"
COPY ../bio_medical_ner/bio_medical_ner_pre-trained_model /bio_medical_ner_pre-trained_model
WORKDIR /bio_medical_ner_pre-trained_model
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip
EXPOSE 7000
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python",  "bio_ner_pt_filter.py"]
