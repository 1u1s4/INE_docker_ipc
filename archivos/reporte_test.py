from ineipc.datosipc import datosIPC
from funcionesjo import mes_by_ordinal
from reporteine.reporteine import ReporteINE

mes = 4
anio = 2023
mes_ = mes_by_ordinal(mes, abreviado=False).capitalize()
fecha = f"{mes_} {anio}"
datos = datosIPC(anio, mes, dbBackup=1)
reporte = ReporteINE("Índice de Precios al Consumidor", anio, mes)