# Imagen base
FROM ubuntu:20.04

# Asegúrate de que todo se ejecute en modo noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Actualiza la lista de paquetes
RUN apt-get update

# Instala OpenJDK 8, Python, pip y las bibliotecas GDAL
RUN apt-get install -y openjdk-8-jdk python3 python3-pip libgdal-dev

# Instala las bibliotecas necesarias para 'devtools'
RUN apt-get install -y libfontconfig1-dev libfreetype6-dev libharfbuzz-dev libfribidi-dev

# Establece la versión de Java 
RUN /usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64

# Instala R
RUN apt-get update && apt-get install -y r-base

RUN R CMD javareconf

RUN apt-get install -y git

# Instala los paquetes de devtools y rJava en R
RUN R -e "install.packages('devtools', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('rJava', repos='http://cran.rstudio.com/')"

# Instalar paquetes R desde GitHub
RUN R -e "devtools::install_github('yihui/tikzDevice')"
RUN R -e "devtools::install_github('1u1s4/funcionesINE', upgrade='never')"

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install \
    git+https://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@github.com/1u1s4/funcionesjo.git \
    git+https://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@github.com/1u1s4/colorimapgt.git \
    git+https://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@github.com/1u1s4/reporteine@packing \
    git+https://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@github.com/1u1s4/ineipc

# Incluir la fuente personalizada
COPY archivos/OpenSans-CondLight.ttf /usr/share/fonts/
RUN fc-cache -f -v

COPY archivos/db_b /app/db_b
COPY archivos/mapa_test.py /app/mapa_test.py
COPY archivos/reporte_test.py /app/reporte_test.py

# Iniciar una shell Bash
CMD ["/bin/bash"]
