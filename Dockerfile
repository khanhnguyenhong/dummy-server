# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Create the data directory (so permission errors don't happen when saving files)
RUN mkdir -p /app/data

# Expose the port to Docker
EXPOSE 8000

# COMMAND: Start the server
# --host 0.0.0.0 is CRITICAL. If you use 127.0.0.1, it will not work on AWS.
# --reload is optional (useful for dev, remove for production if you want)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]