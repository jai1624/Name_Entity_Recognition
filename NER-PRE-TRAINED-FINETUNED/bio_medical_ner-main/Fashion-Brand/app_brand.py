""" Import Libraries """

import gradio as gr
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
# Create tokenizer for custom trained transformer model, pipeline
tokenizer = AutoTokenizer.from_pretrained("C:\\Users\\JaiGatiri\\Documents\\Disease-NER-Custom-Train\\Fashion-BRAND-NER\\model", model_max_length=128)
model = AutoModelForTokenClassification.from_pretrained("C:\\Users\\JaiGatiri\\Documents\\Disease-NER-Custom-Train\\Fashion-BRAND-NER\\model")
nlp=pipeline(task='ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")


def ner(text):
    '''

    Args:
        text:  input from the user

    Returns:
        map the transformer output to gradio hightlight function output
        ner_content: parameter returns dictionary output to the front end'''

    raw = nlp(text)
    ner_content = {
        "text": text,
        "entities": [
            {
                "entity": x["entity_group"],
                "word": x["word"],
                "score": x["score"],
                "start": x["start"],
                "end": x["end"],
            }
            for x in raw
        ],
    }
    return ner_content

# UI PART OF GRADIO for text boxes (input,output)
# inputs : input text
# outputs : output highlighted labels

interface = gr.Interface(
    ner,
    inputs=gr.Textbox(label="Note text", value=""),
    outputs=[
        gr.HighlightedText(label="NER", combine_adjacent=True),
    ],
    allow_flagging="never",
)
interface.launch()
