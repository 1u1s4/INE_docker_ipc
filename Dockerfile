# Imagen base
FROM ubuntu:22.04

# Asegúrate de que todo se ejecute en modo noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Incluir la fuente personalizada
COPY fuentes/OpenSans-CondBold.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLight.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLightItalic.ttf /usr/share/fonts/

# Copiar diccionario tikz
# COPY dict/tikzMetricsDictionary /Dictionary/tikzMetricsDictionary

# tests
COPY data/db_ipc /app/db_b
COPY scrips/ipc_test.py /app/ipc_test.py
COPY scrips/grafica_test.py /app/grafica_test.py

# Actualiza la lista de paquetes e instala los necesarios
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.11 \
    python3-pip \
    openjdk-8-jdk \
    git \
    libgdal-dev \
    texlive-xetex \
    texlive-science \
    r-base \
    libfontconfig1-dev \
    libfreetype6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    && /usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64 \
    && R CMD javareconf \
    && R -e "install.packages('devtools', repos='http://cran.rstudio.com/');" \
    && R -e "devtools::install_version('rJava', version = '1.0.6', repos='http://cran.rstudio.com/');" \
    && R -e "devtools::install_github('yihui/tikzDevice', ref = 'v0.12.4');" \
    && R -e "devtools::install_github('1u1s4/funcionesINE@gpt', upgrade='never', INSTALL_opts = '--no-test-load');" \
    && pip3 install --no-cache-dir \
    git+https://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@github.com/1u1s4/funcionesjo.git \
    git+https://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@github.com/1u1s4/ineipc.git \
    git+https://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@github.com/1u1s4/reporteine.git \
    && fc-cache -f -v \
    && rm -rf /var/lib/apt/lists/*

# Define el directorio de instalación de Java como variable de entorno JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Añade el directorio donde se encuentra libjvm.so a LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH $JAVA_HOME/jre/lib/amd64/server

# Iniciar una shell Bash
CMD ["/bin/bash"]
