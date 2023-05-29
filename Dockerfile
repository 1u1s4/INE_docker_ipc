# Empezar desde una imagen específica de Ubuntu
FROM ubuntu:20.04

# Configurar DEBIAN_FRONTEND en noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Actualizar lista de paquetes
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common

# Instalar OpenJDK 8
RUN add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk

# Instalar todas las dependencias necesarias
RUN apt-get install -y \
    r-base \
    r-base-dev \
    build-essential \
    fortran77-compiler \
    libssl-dev \
    libpcre++-dev \
    liblzma-dev \
    texlive-xetex \
    python3 \
    python3-pip \
    git \
    libgdal-dev && \
    rm -rf /var/lib/apt/lists/*

# Establecer la versión GDAL
RUN echo "GDAL_VERSION=$(gdal-config --version)" >> /etc/environment

# Establecer el repositorio de CRAN
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"))' >> /usr/lib/R/etc/Rprofile.site

# Instalar devtools y rJava en R
RUN R -e "install.packages(c('devtools', 'rJava'))"

# Instalar paquetes R desde GitHub
RUN R -e "devtools::install_github('yihui/tikzDevice')"
RUN R -e "devtools::install_github('1u1s4/funcionesINE', upgrade='never')"

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install \
    git+https://github.com/1u1s4/funcionesjo.git \
    git+https://github.com/1u1s4/colorimapgt.git \
    git+https://github.com/1u1s4/reporteine@packing \
    git+https://github.com/1u1s4/ineipc

# Incluir la fuente personalizada
COPY archivos/OpenSans-CondLight.ttf /usr/share/fonts/
RUN fc-cache -f -v

COPY archivos/db_b /app/db_b
COPY archivos/mapa_test.py /app/mapa_test.py
COPY archivos/reporte_test.py /app/reporte_test.py

# Iniciar una shell Bash
CMD ["/bin/bash"]
