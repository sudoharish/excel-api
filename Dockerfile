FROM python:3.11.3-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py app.py
COPY data.xlsx data.xlsx
EXPOSE 5000
CMD ["python", "app.py"]
