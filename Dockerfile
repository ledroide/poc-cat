FROM python:alpine
# install dependencies
COPY /requirements.txt /
RUN pip3 install -r requirements.txt
# bundle app
COPY /myproject /app

EXPOSE 8080
ENTRYPOINT ["python3", "/app/main.py"]