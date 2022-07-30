FROM python:3.8
ENV TZ=America/Sao_Paulo
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip
RUN pip install Flask