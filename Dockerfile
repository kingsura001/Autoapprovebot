# Use official Python 3.11 base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (if needed — optional)
EXPOSE 8000

# Command to run your bot
CMD ["python", "main.py"]
