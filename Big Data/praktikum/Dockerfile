FROM openjdk:8-jdk-slim

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install PySpark
RUN pip3 install pyspark pandas jupyter matplotlib

# Set up working directory
WORKDIR /workspace

# Expose Jupyter Notebook port
EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
