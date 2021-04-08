FROM python:3.8-alpine
WORKDIR /usr/myapp
COPY . .
CMD ["python3","traingle.py"]