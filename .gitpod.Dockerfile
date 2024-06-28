# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /workspace

# Copy the current directory contents into the container at /workspace
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make directories for input and output images
RUN mkdir -p /workspace/input_images
RUN mkdir -p /workspace/output_images

# Expose port 80 to allow access to the web server if needed
EXPOSE 80

# CMD ["python", "main.py"]