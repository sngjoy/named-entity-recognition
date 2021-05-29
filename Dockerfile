# Base image
FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y g++

USER root
WORKDIR /home

COPY conda.yml .
RUN conda env update -n base -f conda.yml && rm conda.yml

COPY src /home/src

EXPOSE 8000
USER 1000

CMD ["uvicorn", "src.app_ner:app", "--host", "0.0.0.0"]
