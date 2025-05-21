# Python base image
FROM python:3.10-slim

# Set working directory in container. This is the default folder!
WORKDIR /app

# Copy project to /app in container
COPY . .

# Install dependencies (if you have requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Tell Docker this container will listen on port 8080
EXPOSE 8080

# Command to run your application
CMD ["python", "main.py"]
