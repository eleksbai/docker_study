# Use an official Python runtime as a parent image
FROM markadams/chromium-xvfb-py3

# Set the working directory to /app
WORKDIR /docker_study

# Copy the current directory contents into the container at /app
ADD . /docker_study

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run docker_study.py when the container launches
CMD ["python3", "docker_study.py"]