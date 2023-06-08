# Define imagen base
FROM ubuntu:22.04

# Establece el modo noninteractive como predeterminado
ENV DEBIAN_FRONTEND noninteractive

# Incorpora fuentes personalizadas al sistema
COPY fuentes/OpenSans-CondBold.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLight.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLightItalic.ttf /usr/share/fonts/
RUN fc-cache -f -v

# Copia archivos de prueba al directorio 'app' del contenedor
COPY data/db_ipc /app/db_b
COPY scrips/ipc_test.py /app/ipc_test.py
COPY scrips/grafica_test.py /app/grafica_test.py

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
    libfribidi-dev

# Establece la versión predeterminada de Java
RUN /usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64

# Define la variable de entorno JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Añade el directorio de la biblioteca libjvm.so a la variable de entorno LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH $JAVA_HOME/jre/lib/amd64/server

# Actualiza la configuración de Java para R
RUN R CMD javareconf

# Instala devtools desde el repositorio especificado
RUN R -e "install.packages('devtools')"

# Usa devtools para instalar la versión especificada de rJava
RUN R -e "devtools::install_version('rJava', version = '1.0.6', repos='http://cran.rstudio.com/')"

# Instala paquetes específicos de R desde GitHub
RUN R -e "devtools::install_github('yihui/tikzDevice', ref = 'v0.12.4')"
RUN R -e "devtools::install_github('1u1s4/funcionesINE@gpt', upgrade='never', INSTALL_opts = '--no-test-load')"

# Instala paquetes Python específicos desde repositorios de GitHub
RUN pip3 install \
    --no-cache-dir \
    git+https://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@github.com/1u1s4/funcionesjo.git \
    git+https://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@github.com/1u1s4/ineipc.git \
    git+https://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@github.com/1u1s4/reporteine.git

# Limpia la caché de paquetes
RUN rm -rf /var/lib/apt/lists/*

# Configura el comando por defecto a ejecutar
CMD ["/bin/bash"]

