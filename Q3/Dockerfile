FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

WORKDIR /code

# COPY requirements.txt /code/
# RUN pip install -r requirements.txt

COPY . /code/

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 9999

# Start the HTTP server when the container launches
CMD [ "python", "Server.py" ]