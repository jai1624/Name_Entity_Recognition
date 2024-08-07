""" Import Libraries """

import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

# Create tokenizer for biomed model
# https://huggingface.co/d4data/biomedical-ner-all?text=asthma
tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")
pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")



def ner(text):
    """
    map the transformer output to gradio hightlight function output
    Args:
        text: input from the user
    Returns: mapped dict output
    """
    raw = pipe(text)
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
        gr.HighlightedText(label="NER", combine_adjacent=True)
    ],
    allow_flagging="never",
)
interface.launch()
