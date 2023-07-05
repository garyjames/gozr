# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Update the package lists and install Python 3 and SQLite
RUN apt-get update && apt-get install -y python3-pip sqlite3 libsqlite3-dev

# Set the working directory
WORKDIR /app

# Copy your application files to the container's working directory
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Start the application
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

