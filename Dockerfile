# Empezar desde la última imagen de Ubuntu
FROM ubuntu:latest

# Usar la versión más reciente de R
FROM r-base:4.0.0

# Instalar Java 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get clean;

# Configurar el entorno de Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
RUN export JAVA_HOME

# Instalar rtools
RUN apt-get install -y r-cran-devtools

# Instalar XeLaTeX
RUN apt-get install -y texlive-xetex

# Instalar Python 3, pip y Git
RUN apt-get update && \
    apt-get install -y python3 python3-pip git

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install git+https://github.com/1u1s4/funcionesjo.git
RUN pip3 install git+https://github.com/1u1s4/colorimapgt.git

# Iniciar una shell Bash
CMD ["/bin/bash"]
