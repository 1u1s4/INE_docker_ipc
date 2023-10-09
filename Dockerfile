# Define imagen base
FROM ubuntu:22.04

# Establece el modo noninteractive como predeterminado
ENV DEBIAN_FRONTEND noninteractive

# Incorpora fuentes personalizadas al sistema
COPY fuentes/*.ttf /usr/share/fonts/

# Actualiza lista de paquetes e instala dependencias
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    openjdk-8-jdk \
    r-base \
    git \
    libgdal-dev \
    texlive-xetex \
    texlive-science \
    libfontconfig1-dev \
    libfreetype6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
&& rm -rf /var/lib/apt/lists/*

# Establece la versión predeterminada de Java
RUN /usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64 \
    && fc-cache -f -v \
    && R CMD javareconf \
    && R -e "install.packages('devtools')" \
    && R -e "devtools::install_version('rJava', version = '1.0.6', repos='http://cran.rstudio.com/')" \
    && R -e "devtools::install_github('yihui/tikzDevice', ref = 'v0.12.4')" \
    && R -e "devtools::install_github('1u1s4/funcionesINE@gpt', upgrade='never', INSTALL_opts = '--no-test-load')"

# Define la variable de entorno JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Añade el directorio de la biblioteca libjvm.so a la variable de entorno LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH $JAVA_HOME/jre/lib/amd64/server

# Copia archivos que cambian menos frecuentemente
COPY key.key /app/
COPY data/db_ipc /app/db_b
COPY data/diagramas_ipc /app/diagramas
COPY data/*.tex /app/
COPY data/*.xlsx /app/

RUN pip3 install --upgrade setuptools wheel
# Instala paquetes Python específicos desde repositorios de GitHub
ENV GITHUB_TOKEN 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
RUN pip3 install \
    --no-cache-dir \
    git+https://${GITHUB_TOKEN}@github.com/1u1s4/INEipc.git \
    git+https://${GITHUB_TOKEN}@github.com/1u1s4/INEcba.git \
    git+https://${GITHUB_TOKEN}@github.com/1u1s4/INEreporte.git

# Copia archivos que cambian más frecuentemente
COPY scrips/ipc.py /app/main.py

# Configura el comando por defecto a ejecutar
CMD ["/bin/bash"]
