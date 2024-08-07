FROM python:3.10.10-slim
LABEL description="spacy resume Ner"
COPY . /bio_medical_ner/Spacy-CV-NER/UI-APP-SPACY
WORKDIR /bio_medical_ner/Spacy-CV-NER/UI-APP-SPACY
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip
EXPOSE 7004
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python",  "app_spacy.py"]