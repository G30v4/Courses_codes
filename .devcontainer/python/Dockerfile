FROM python:3.13-slim

# Install linux deps
RUN apt update && apt install git -y

# Install python libs
COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade --user  -r requirements.txt