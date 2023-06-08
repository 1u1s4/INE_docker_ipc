@echo off
FOR /L %%i IN (1,1,100) DO (
    mkdir resultado_%%i
    cd resultado_%%i
    speedtest-cli --no-upload --json > velocidad_internet.json
    docker build --no-cache -t ipc_dev C:\Users\laalvarado\Documents\GitHub\INE_docker_ipc > build_time.txt 
    cd ..
)
