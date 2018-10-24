# Use an official Python runtime as a parent image
FROM python:3.6-alpine

# Set the working directory to /app
WORKDIR /docker_study

# Copy the current directory contents into the container at /app
ADD . /docker_study

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME docker_study


# Run docker_study.py when the container launches
CMD ["python", "docker_study.py"]