@echo off
FOR /L %%i IN (1,1,100) DO (
    echo Iteracion %%i
    IF NOT EXIST resultado (
        mkdir resultado
    )
    cd resultado
    speedtest-cli --no-upload --json > velocidad_internet_%%i.json
    time docker build --no-cache -t ipc_dev C:\Users\laalvarado\Documents\GitHub\INE_docker_ipc > build_time_%%i.txt 
)
