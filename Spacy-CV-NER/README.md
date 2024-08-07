# Resume Parser Spacy Version 3

A Resume Parser Model is a specialized machine learning model that is designed to extract relevant information from resumes or CVs (curriculum vitae) in a structured format. It is a type of Natural Language Processing (NLP) model that uses various techniques to analyze and interpret the content of resumes and extract specific data points such: 'Awards', 'Name','Degree', 'Skills', 'College Name', 'Email Address', 'Designation', 'Companies worked at', 'LANGUAGE', 'Graduation Year','Years of Experience', 'Location','Certificate','Worked As','University','LINKEDNIN LINK','CONTACT'


## Additional Requirements For UI Part
gradio==3.35.2
pdfminer.six==20221105
spacy==3.5.2

## Training

``` Training part requirement and codes details are in the Spacy_CV_PARSER.ipynb

## Evaluation Results with roberta-base model using spacy-transformer.

### roberta-base

|        E       |         ENTS_F                  ENTS_P               ENTS_R              SCORE
|----------------|:-----------------------:|:--------------------:|:----------------:|:----------------:|
|      1200      |          51.05          |         62.19        |       43.30      |       0.51


Output:
json
{
  "entities": [
    {
      "entity": "Name",
      "start": 3,
      "end": 19,
      "text": "Ayush Srivastava"
    },
    {
      "entity": "Designation",
      "start": 22,
      "end": 35,
      "text": "Web Developer"
    },
    {
      "entity": "Degree",
      "start": 50,
      "end": 56,
      "text": "B.Tech"
    },
    {
      "entity": "Years of Experience",
      "start": 72,
      "end": 73,
      "text": "3"
    },
    {
      "entity": "College Name",
      "start": 937,
      "end": 943,
      "text": "JSSATE"
    },
    {
      "entity": "Degree",
      "start": 955,
      "end": 961,
      "text": "B.Tech"
    },
    {
      "entity": "Graduation Year",
      "start": 964,
      "end": 968,
      "text": "2016"
    },
    {
      "entity": "Skills",
      "start": 1188,
      "end": 1219,
      "text": "○ Designing (UI/UX & Photoshop)"
    },
    {
      "entity": "Skills",
      "start": 1221,
      "end": 1251,
      "text": "○ Web Development (HTML & CSS)"
    },
    {
      "entity": "Skills",
      "start": 1287,
      "end": 1323,
      "text": "ReactJS, Gatsby, jQuery, JavaScript,"
    },
    {
      "entity": "Skills",
      "start": 1326,
      "end": 1360,
      "text": "HTML, CSS, Materialize, Bootstrap,"
    },
    {
      "entity": "Skills",
      "start": 1373,
      "end": 1378,
      "text": "Flask"
    },
    {
      "entity": "Skills",
      "start": 1402,
      "end": 1416,
      "text": "D3, Matplotlib"
    },
    {
      "entity": "Skills",
      "start": 1433,
      "end": 1454,
      "text": "Google Cloud Platform"
    },
    {
      "entity": "Skills",
      "start": 1481,
      "end": 1488,
      "text": "C++, C,"
    },
    {
      "entity": "Skills",
      "start": 1491,
      "end": 1497,
      "text": "Python"
    },
    {
      "entity": "Skills",
      "start": 1511,
      "end": 1521,
      "text": "Oracle SQL"
    }
  ]
}
