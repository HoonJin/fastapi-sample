#FROM python:3.8.2-slim
#RUN apt-get -y upgrade
#RUN apt-get -y update
#RUN apt-get -y install default-libmysqlclient-dev
FROM python:3.8.2
COPY ./ ./app
WORKDIR /app/
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
# docker build -t <image_tag> .
# docker run -p 8000:8000 -v $(pwd):/app:ro <image_tag>
