# lightweight python image
FROM python:3.9-slim

# Setting working directory in the container
WORKDIR /app

# Copy current directory contents into container
COPY . .

# Installing required python packages
RUN pip install -r requirements.txt

# Exposing port
EXPOSE 5000

# Command to run the flask app
CMD ["python", "app.py"]

