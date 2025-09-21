# Python image to use.
FROM python:3.12-alpine

# Set the working directory to /app
WORKDIR /usr/src/app

# copy the requirements file used for dependencies
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir  -r requirements.txt

EXPOSE 8080

ENV FLASK_APP=app.py

  # Run the Gunicorn server when the container launches
    CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
