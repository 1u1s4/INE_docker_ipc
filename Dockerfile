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

# Instalar libgdal-dev
RUN apt-get install -y libgdal-dev

# Establecer la versión GDAL
RUN echo "GDAL_VERSION=$(gdal-config --version)" >> /etc/environment

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install git+https://github.com/1u1s4/funcionesjo.git
RUN pip3 install git+https://github.com/1u1s4/colorimapgt.git
RUN pip3 install git+https://github.com/1u1s4/reporteine@packing

# Incluir la fuente personalizada
COPY archivos/OpenSans-CondLight.ttf /usr/share/fonts/
RUN fc-cache -f -v

COPY archivos/db_b /app/db_b
COPY archivos/mapa_test.py /app/mapa_test.py

# Iniciar una shell Bash
CMD ["/bin/bash"]
