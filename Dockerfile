FROM python:3.8

WORKDIR /workspace
ADD requirements.txt /workspace/requirements.txt

RUN pip install -r requirements.txt
#RUN python -m spacy download en_core_web_sm

ADD app.py /workspace/

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

CMD [ "python3" , "/workspace/app.py" ]