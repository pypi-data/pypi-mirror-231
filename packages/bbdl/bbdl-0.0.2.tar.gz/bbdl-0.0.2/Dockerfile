FROM python:3-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY /src/bbdl/bbdl.py .
VOLUME /usr/src/app/data
CMD [ "python", "/usr/src/app/bbdl.py" ]