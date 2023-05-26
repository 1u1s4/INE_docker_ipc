# Empezar desde la última imagen de OpenJDK 8
FROM openjdk:8-jdk

# Instalar R base
RUN apt-get update && \
    apt-get install -y r-base

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

COPY db_b /app/db_b

# Iniciar una shell Bash
CMD ["/bin/bash"]
