# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install the required packages
RUN pip install --no-cache-dir Flask pyrad gunicorn

# Copy the Flask app files to the container
COPY app.py .
COPY dictionary .
COPY templates templates
# Expose the port on which the Flask app will run
EXPOSE 5000

# Define the command to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
