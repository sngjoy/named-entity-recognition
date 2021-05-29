# named_entity_recognition

## Introduction
This project aims to create an API that will allow users to post news articles and extract the named entities that are identified from within each of the news articles.

The pretrained NLP core model from [spaCy](https://spacy.io/models/en#en_core_web_sm) is used to recognise the entities.


## Usage
#### Step 1:
Clone the repository
```
git clone https://github.com/sngjoy/named_entity_recognition.git
cd named_entity_recognition
```

#### Step 2:
Create environment with the required packages.

```
conda env create -f conda.yml
```

#### Step 3:
Build and run the docker image
```
docker build -t spacy-ner .
docker run -it -p 8000:8000 spacy-ner
```

#### Step 4:
Navigate to URL and run the app!
```
http://127.0.0.1:8000/
```

#### Step 4:
To POST file (.json):
1. Use cURL
```
curl -X 'POST' \
  'http://127.0.0.1:8000/extract' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@<FILENAME>.json; type=application/json'
```
2. Use the Swagger UI directly from browser

Navigate to endpoint `/docs`
```
http://127.0.0.1:8000/docs
```
Upload file and click execute.
<p align="center">
  <img src="media/swaggerUI.png" />
</p>

## About the model
Spacy supports the following entity types:
<p align="center">
  <img src="media/spacy_entities.png" />
</p>

<p align="center">
    Entity recognised by spaCy core model <a href="https://spacy.io/api/data-formats#named-entities">(source)</a>
</p>
