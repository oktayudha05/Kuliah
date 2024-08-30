FROM openjdk:8-jdk-slim

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip wget

# Install PySpark, pandas, Jupyter, and matplotlib
RUN pip3 install pyspark pandas jupyter matplotlib

# Install Hadoop
ENV HADOOP_VERSION=3.3.6
RUN wget https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzvf hadoop-$HADOOP_VERSION.tar.gz && \
    mv hadoop-$HADOOP_VERSION /usr/local/hadoop && \
    rm hadoop-$HADOOP_VERSION.tar.gz

# Set environment variables for Hadoop
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

# Detect JAVA_HOME dynamically and set it
RUN JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java)))) && \
    export JAVA_HOME && \
    $HADOOP_HOME/bin/hdfs namenode -format

# Set up working directory
WORKDIR /workspace

# Expose Jupyter Notebook port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
