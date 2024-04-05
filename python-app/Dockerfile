FROM python:3.11
ARG version=1.0.0
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR app
COPY src/app.py .

EXPOSE 8000
CMD ["python", "app.py"]
