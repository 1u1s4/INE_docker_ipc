@echo off
FOR /L %%i IN (1,1,100) DO (
    mkdir resultados
    cd resultado
    speedtest-cli --no-upload --json > velocidad_internet_%%i.json
    docker build --no-cache -t ipc_dev C:\Users\laalvarado\Documents\GitHub\INE_docker_ipc > build_time_%%i.txt 
    cd ..
)
