# Empezar desde la última imagen de Ubuntu
FROM ubuntu:latest

# Actualizar lista de paquetes
RUN apt-get update

# Instalar OpenJDK 8
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk

# Configurar DEBIAN_FRONTEND en noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Instalar R base
RUN apt-get install -y r-base

# Instalar libssl-dev
RUN apt-get install -y libssl-dev

# Instalar libpcre++-dev y liblzma-dev para rJava
RUN apt-get install -y libpcre++-dev liblzma-dev

# Instalar devtools en R
RUN R -e "install.packages('devtools', repos='http://cran.rstudio.com/')"

# Instalar rtools
RUN apt-get install -y r-cran-devtools

# Instalar rJava
RUN R -e "install.packages('rJava', repos='http://cran.rstudio.com/')"

# Instalar paquetes R desde GitHub
RUN R -e "devtools::install_github('yihui/tikzDevice')"
RUN R -e "devtools::install_github('1u1s4/funcionesINE', upgrade='never')"

# Instalar XeLaTeX
RUN apt-get install -y texlive-xetex

# Instalar Python 3, pip y Git
RUN apt-get install -y python3 python3-pip git

# Instalar libgdal-dev
RUN apt-get install -y libgdal-dev

# Establecer la versión GDAL
RUN echo "GDAL_VERSION=$(gdal-config --version)" >> /etc/environment

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install git+https://github.com/1u1s4/funcionesjo.git
RUN pip3 install git+https://github.com/1u1s4/colorimapgt.git
RUN pip3 install git+https://github.com/1u1s4/reporteine@packing
RUN pip3 install git+https://github.com/1u1s4/ineipc

# Incluir la fuente personalizada
COPY archivos/OpenSans-CondLight.ttf /usr/share/fonts/
RUN fc-cache -f -v

COPY archivos/db_b /app/db_b
COPY archivos/mapa_test.py /app/mapa_test.py
COPY archivos/reporte_test.py /app/reporte_test.py

# Iniciar una shell Bash
CMD ["/bin/bash"]
