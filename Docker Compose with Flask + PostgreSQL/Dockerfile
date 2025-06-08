from python:3.11
# Set the working directory
WORKDIR /app.
# Copy the requirements file into the container
COPY requirements.txt .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container    
COPY . .
# Expose the port the app runs on
EXPOSE 5000
# Set the environment variable for Flask
ENV FLASK_APP=app.py
# Set the environment variable for Flask to run in development mode   
CMD ["flask", "run", "--host=0.0.0.0"]











