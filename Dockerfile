# Imagen base
FROM ubuntu:22.04

# Asegúrate de que todo se ejecute en modo noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Actualiza la lista de paquetes
RUN apt-get update

# Instala Python 3.11, pip3, OpenJDK 8, git, las bibliotecas GDAL y texlive-xetex
RUN apt-get install -y \
    python3.11 \
    python3-pip \
    openjdk-8-jdk \
    git \
    libgdal-dev \
    texlive-xetex \
    texlive-science

# Python, pip, las bibliotecas GDAL y texlive-xetex
# RUN apt-get install -y openjdk-8-jdk python3 python3-pip libgdal-dev texlive-xetex texlive-science

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

# Instala devtools
# Instala las bibliotecas necesarias para 'devtools'
RUN apt-get install -y libfontconfig1-dev libfreetype6-dev libharfbuzz-dev libfribidi-dev
RUN R -e "install.packages('devtools', repos='http://cran.rstudio.com/')"

# Usa devtools para instalar rJava (versión 1.0.6)
RUN R -e "devtools::install_version('rJava', version = '1.0.6', repos='http://cran.rstudio.com/')"

# Instalar paquetes R desde GitHub
RUN R -e "devtools::install_github('yihui/tikzDevice', ref = 'v0.12.4')"
RUN R -e "devtools::install_github('1u1s4/funcionesINE@gpt', upgrade='never', INSTALL_opts = '--no-test-load')"

# Instalar el paquete Python desde el repositorio Git
RUN pip3 install \
    git+https://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@github.com/1u1s4/funcionesjo.git \
    git+https://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@github.com/1u1s4/ineipc.git \
    git+https://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@github.com/1u1s4/reporteine

# Incluir la fuente personalizada
COPY fuentes/OpenSans-CondBold.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLight.ttf /usr/share/fonts/
COPY fuentes/OpenSans-CondLightItalic.ttf /usr/share/fonts/
# Actualizar la caché de fuentes
RUN fc-cache -f -v

# Copiar diccionario tikz
COPY dict/tikzMetricsDictionary /Dictionary/tikzMetricsDictionary

# tests
COPY data/db_ipc /app/db_b
COPY scrips/ipc_test2.py /app/ipc_test.py
COPY scrips/grafica_test.py /app/grafica_test.py

# Iniciar una shell Bash
CMD ["/bin/bash"]
