""" Import Libraries """

import gradio as gr
from pdfminer.high_level import extract_text
import spacy

# to load the spacy trained model
nlp = spacy.load("C:/Users/JaiGatiri/Documents/Disease-NER-Custom-Train/Resume-NER-master/model-best")

def predict_api(file_obj):

    """

    Args:
        file_obj: pdf input

    Returns: Returns the json output to the front-end

    """
    text = extract_text(file_obj.name)
    text = text.replace("\n", " ")
    text = text.replace("\f", " ")
    doc = nlp(text)
# doc :variable holds spacy model output
# loop through ent to get the ent.text,ent.label_ & append to list
# case_list: holds the list of dictionary output with text,labels
    case_list = []
    for ent in doc.ents:
        case = {'text': ent.text, 'label': ent.label_}
        case_list.append(case)
    return case_list


# UI FOR PDF UPLOAD AND JSON OUTPUT
# file_input : input pdf interface
# iface : output interface, json output

DESCRIPTION = """A demo for a CV parser."""
ARTICLE = "Resume Parser"
file_input = gr.inputs.File(file_count="single", type="file", label="Upload a CV: .PDF Or .TXT", optional=False)
iface = gr.Interface(fn=predict_api, inputs=file_input, outputs="json", allow_flagging="never",
                     allow_screenshot=False, title="CV Parser", theme="seafoam", description=DESCRIPTION,
                     article=ARTICLE)

iface.launch()
