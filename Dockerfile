FROM python:3.10
WORKDIR /bookshelf_app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt