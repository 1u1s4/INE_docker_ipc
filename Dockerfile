# Imagen base
FROM ubuntu:22.04

# Asegúrate de que todo se ejecute en modo noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Actualiza la lista de paquetes
RUN apt-get update

# Instala OpenJDK 8, Python, pip, las bibliotecas GDAL y texlive-xetex
RUN apt-get install -y openjdk-8-jdk python3 python3-pip libgdal-dev texlive-xetex texlive-science

# Instala las bibliotecas necesarias para 'devtools'
RUN apt-get install -y libfontconfig1-dev libfreetype6-dev libharfbuzz-dev libfribidi-dev

# Establece la versión de Java 
RUN /usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64

# Define el directorio de instalación de Java como variable de entorno JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Añade el directorio donde se encuentra libjvm.so a LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH $JAVA_HOME/jre/lib/amd64/server

# Instala R
RUN apt-get update && apt-get install -y r-base

# Actualiza la configuración de Java para R
RUN R CMD javareconf

# Instala los paquetes de devtools y rJava en R
RUN R -e "install.packages('devtools', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('rJava', repos='http://cran.rstudio.com/')"

RUN apt-get install -y git

# Instalar paquetes R desde GitHub
RUN R -e "devtools::install_github('yihui/tikzDevice')"
RUN R -e "devtools::install_github('1u1s4/funcionesINE', upgrade='never', INSTALL_opts = '--no-test-load')"

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install \
    git+https://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@github.com/1u1s4/funcionesjo.git \
    git+https://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@github.com/1u1s4/colorimapgt.git \
    git+https://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@github.com/1u1s4/reporteine \
    git+https://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@github.com/1u1s4/ineipc

# Incluir la fuente personalizada
COPY fuentes/OpenSans-CondBold.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLight.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLightItalic.ttf /usr/share/fonts/
RUN fc-cache -f -v

COPY data/db_ipc /app/db_b
COPY scrips/mapa_test.py /app/mapa_test.py
COPY scrips/reporte_test.py /app/reporte_test2.py

# Iniciar una shell Bash
CMD ["/bin/bash"]
