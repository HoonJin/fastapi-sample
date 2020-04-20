FROM python:3.8.2
COPY ./ ./app
WORKDIR /app/
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
