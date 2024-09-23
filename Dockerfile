# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the Python libraries required
RUN pip install python-barcode Pillow

# Run the Python script when the container launches
CMD ["python", "barcode_generator.py"]

