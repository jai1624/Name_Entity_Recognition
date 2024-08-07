import gradio as gr
from collections import defaultdict

# Create tokenizer for biomed model
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
# https://huggingface.co/d4data/biomedical-ner-all?text=asthma
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")
pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def group_by_entity(raw):
    out = defaultdict(int)
    for ent in raw:
        out[ent["entity_group"]] += 1
    return out

def ner(text):
    raw = pipe(text)
    print("start",raw)
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

    #Added filter to change the label based on the requirement
    filtered_d = [d for d in ner_content['entities'] if d['entity'] in 'Diagnostic_procedure']
    ner_filter = dict({'text': text, 'entities': filtered_d})
    return (ner_filter)

def main():
    interface = gr.Interface(
        ner,
        inputs=gr.Textbox(label="Note text", value=""),
        outputs=[
            gr.HighlightedText(label="NER", combine_adjacent=True)
            #gr.JSON(label="Entity Counts"),
        ],
        allow_flagging="never"

    )
    interface.launch(server_name="0.0.0.0", server_port=7000)
    interface.launch(enable_queue=True)

if __name__ == '__main__':
	main()
# interface.launch(enable_queue=True, share=True,
#            server_name="0.0.0.0", server_port=7860)