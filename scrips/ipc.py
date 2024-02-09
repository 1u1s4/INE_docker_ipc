from utilsjo import mes_by_ordinal
from INEipc import DatosIPC
from INEreporte import Reporte

mes_datos = 9
anio = 2023

fecha = f"{mes_by_ordinal(mes_datos, abreviado=False).capitalize()} {anio}"
datos = DatosIPC(anio, mes_datos, dbBackup=1)

reporte = Reporte(
    nombre_reporte="Índice de Precios al Consumidor",
    anio=anio,
    mes=mes_datos+1,
    periodo=fecha
)

subcap_data_imputacion = ([
  ('Sep-2022', 4.4351846566584845),
  ('Oct-2022', 5.289202323100628),
  ('Nov-2022', 3.286537608984779),
  ('Dic-2022', 4.28484415137311),
  ('Ene-2023', 3.240628778718259),
  ('Feb-2023', 2.070393374741201),
  ('Mar-2023', 2.8352349686631926),
  ('Abr-2023', 1.61),
  ('May-2023', 1.22),
  ('Jun-2023', 1.10),
  ('Jul-2023', 1.71),
  ('Ago-2023', 1.24),
  ('Sep-2023', 1.65)],
 'El porcentaje de precios imputados en  sepriembre 2023 es de 1.65%. El mayor porcentaje de imputaciones fue en el mes de octubre 2022 con una cantidad de 5.29% y el menor se encuentra en el mes de junio 2023 con una cantidad de 1.10%.')

# capitulo 1
reporte.presentacion(datos.introduccion())
reporte.agregar_capitulo(
    titulo="Detalle del operativo de campo del IPC"
)
subcap_data = datos.serie_fuentes()
reporte.agregar_subcapitulo(
    titulo="Cobertura de fuentes",
    titulo_grafico="Histórico de cobertura de fuentes",
    descripcion_grafico="República de Guatemala, serie histórica, cantidad de fuentes",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico=dict(Q4Etiquetas=True)
)
subcap_data = datos.serie_precios()
reporte.agregar_subcapitulo(
    titulo="Cobertura de precios",
    titulo_grafico="Histórico de cobertura de precios",
    descripcion_grafico="República de Guatemala, serie histórica, cantidad de precios",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico=dict(Q4Etiquetas=True)
)
subcap_data = subcap_data_imputacion
reporte.agregar_subcapitulo(
    titulo="Imputación de precios",
    titulo_grafico="Histórico de imputación de precios",
    descripcion_grafico="República de Guatemala, serie histórica, porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="columna",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.desagregacion_fuentes()
reporte.agregar_subcapitulo(
    titulo="Desagregación de fuentes",
    titulo_grafico="Desagregación de fuentes por tipo",
    descripcion_grafico=f"República de Guatemala, {fecha}, porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="barra",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
# mapas
subcap_data = datos.cobertura_fuentes()
reporte.agregar_subcapitulo(
    titulo="Mapa de cobertura de fuentes",
    titulo_grafico="Cantidad de fuentes diligenciadas",
    descripcion_grafico=f"República de Guatemala, {fecha}, adimensional",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="mapa_colorimetrico",
    data=subcap_data[0],
    opciones_grafico={"precision":0}
)
subcap_data = datos.cobertura_precios()
reporte.agregar_subcapitulo(
    titulo="Mapa de cobertura de precios",
    titulo_grafico="Cantidad de precios diligenciadas",
    descripcion_grafico=f"República de Guatemala, {fecha}, adimensional",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="mapa_colorimetrico",
    data=subcap_data[0],
    opciones_grafico={"precision":0}
)
# diagramas
dummy_text = "texto texto texto texto texto texto texto"
reporte.agregar_subcapitulo(
    titulo="Pre-diligenciamiento, recopilación, digitación y crítica",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion=dummy_text,
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_01.tex",
    opciones_grafico={}
)
reporte.agregar_subcapitulo(
    titulo="Recopilación de precios y pesos por gramo",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion=dummy_text,
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_02.tex",
    opciones_grafico={}
)
reporte.agregar_subcapitulo(
    titulo="Recopilación de datos por cotización",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion=dummy_text,
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_03.tex",
    opciones_grafico={}
)
reporte.agregar_subcapitulo(
    titulo="Supervisión de recolección de datos",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion=dummy_text,
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_04.tex",
    opciones_grafico={}
)
# capitulo 2
reporte.agregar_capitulo(
    titulo="Variables exógenas"
)

#subcap_data = datos.indice_precio_alimentos()
subcap_data = ([('Ago-2022', 137.57955105100112),
  ('Sep-2022', 136.04175202121962),
  ('Oct-2022', 135.37847253330085),
  ('Nov-2022', 134.7375273257023),
  ('Dic-2022', 131.79457812874588),
  ('Ene-2023', 130.20155075969072),
  ('Feb-2023', 129.8141529176985),
  ('Mar-2023', 127.00380138970077),
  ('Abr-2023', 127.72177293775783),
  ('May-2023', 124.14497718909877),
  ('Jun-2023', 122.67510555806449),
  ('Jul-2023', 124.01295381269875),
  ('Ago-2023', 121.39138849777402)],
 'El índice de precios de los alimentos\\footnote{El índice de precios de los alimentos de la FAO es una medida de la variación mensual de los precios internacionales de una canasta de productos alimenticios. Consiste en el promedio de los índices de precios de cinco grupos de productos básicos, ponderado con las cuotas medias de exportación de cada uno de los grupos para 2002-2004.} de la FAO\\footnote{Organización de las Naciones Unidas para la Alimentación y la Agricultura.} registró en agosto 2023 un índice de 121.39, lo que representa una variación de -11.77% respecto a agosto 2022 y de -2.11% respecto a julio 2023.')
reporte.agregar_subcapitulo(
    titulo="Precio internacional de los alimentos",
    titulo_grafico="Índice de precios de los alimentos de la FAO",
    descripcion_grafico="Indicador internacional, serie histórica, adimensional",
    descripcion=subcap_data[1],
    fuente="FAO",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)

subcap_data = datos.petroleo()
reporte.agregar_subcapitulo(
    titulo="Precio del petróleo",
    titulo_grafico="Precio promedio mensual del barril del petróleo",
    descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
    descripcion=subcap_data[1],
    fuente="Federal Reserve Economic Data",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
#subcap_data = datos.cambio_quetzal()
subcap_data = ([('Sep-2022', 7.8004169999999995),
  ('Oct-2022', 7.865183548387096),
  ('Nov-2022', 7.813936),
  ('Dic-2022', 7.868113548387095),
  ('Ene-2023', 7.848967741935484),
  ('Feb-2023', 7.831650357142857),
  ('Mar-2023', 7.804977096774192),
  ('Abr-2023', 7.799317333333334),
  ('May-2023', 7.809260645161289),
  ('Jun-2023', 7.838317999999998),
  ('Jul-2023', 7.849883225806452),
  ('Ago-2023', 7.859662258064516),
  ('Sep-2023', 7.868444444444446)],
 'El tipo de cambio de referencia\\footnote{El tipo de cambio de referencia lo calcula el Banco de Guatemala con la información que las instituciones que constituyen el Mercado Institucional de Divisas le proporcionan, relativa al monto de divisas compradas y al monto de divisas vendidas y sus respectivas equivalencias en moneda nacional.} del quetzal respecto al dólar de los Estados Unidos de América, registró en septiembre 2023 un tipo de cambio promedio de Q7.87 por US$1.00, lo que representa una variación de 0.87% respecto a septiembre 2022 y de 0.11% respecto a agosto 2023.')
reporte.agregar_subcapitulo(
    titulo="Cambio del quetzal",
    titulo_grafico="Tipo de cambio nominal promedio",
    descripcion_grafico="República de Guatemala, serie histórica, en quetzales por dólar estadounidense",
    descripcion=subcap_data[1],
    fuente="Banco de Guatemala",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
#subcap_data = datos.tasa_interes()
subcap_data = ([('Sep-2022', 11.940000000000001),
  ('Oct-2022', 11.84),
  ('Nov-2022', 11.83),
  ('Dic-2022', 11.83),
  ('Ene-2023', 11.89),
  ('Feb-2023', 11.940000000000001),
  ('Mar-2023', 11.93),
  ('Abr-2023', 11.93),
  ('May-2023', 11.98),
  ('Jun-2023', 11.98),
  ('Jul-2023', 11.98),
  ('Ago-2023', 11.959999999999999),
  ('Sep-2023', 11.95)],
 'El promedio ponderado preliminar de la tasa de interés activa\\footnote{Es el porcentaje que las instituciones bancarias, de acuerdo con las condiciones de mercado y las disposiciones del banco central, cobran por los diferentes tipos de servicios de crédito a los usuarios de los mismos.} en moneda nacional se ubicó en septiembre 2023 en 11.95%, representa un aumento de 0.01 puntos porcentuales respecto a septiembre 2022 y una disminución de 0.01 puntos porcentuales respecto a agosto 2023.')
reporte.agregar_subcapitulo(
    titulo="Tasa de interés",
    titulo_grafico="Tasas de interés activa bancaria",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="Banco de Guatemala",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
subcap_data = datos.ipc_usa()
reporte.agregar_subcapitulo(
    titulo="Ritmo inflacionario en EE.UU.",
    titulo_grafico="Ritmo inflacionario de Estados Unidos de América",
    descripcion_grafico="Estados Unidos de América, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="FRED",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
subcap_data = datos.ipc_mex()
reporte.agregar_subcapitulo(
    titulo="Ritmo inflacionario en México",
    titulo_grafico="Ritmo inflacionario de México",
    descripcion_grafico="Estados Unidos Mexicanos, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="FRED",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
#aqui se ingresan los datos que se generan de la funcion inflacion_CA_RD_MEX
subcap_data = ([('País', 'Nov-2022', 'Nov-2023'),
  ('Guatemala', 9.166993592258411, 4.300431241015801),
  ('El Salvador', 7.32425159771275, 2.10765494006111),
  ('Honduras', 10.438356164383578, 5.035971223021574),
  ('Nicaragua', 11.378901619913062, 5.6438453352252616),
  ('Costa Rica', 8.256248963326529, -1.6533381256177537),
  ('Republica Dominicana', 7.5805275421090945, 4.000991981483004),
  ('Panamá', 1.52294331607008, 1.949860724233976),
  ('México', 7.799185517264973, 4.285714285714293)],
 'Para el mes de noviembre 2023, en Centro América, República Dominicana y México, Nicaragua presentó el mayor ritmo inflacionario de 5.64%, mientras que Costa Rica registró el ritmo inflacionario más bajo con un nivel de -1.65%.')
reporte.agregar_subcapitulo(
    titulo="Inflación en Centro América, República Dominicana y México",
    titulo_grafico="Tasa de variación interanual del IPC de los países Centroamericanos, República Dominicana y México",
    descripcion_grafico="Centro América, República Dominicana y México, meses seleccionados, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="tabla",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)

# capitulo 3
reporte.agregar_capitulo(
    titulo="Resultados del IPC"
)
subcap_data = datos.serie_IPC(0)
reporte.agregar_subcapitulo(
    titulo="Evolución del IPC",
    titulo_grafico="IPC, base diciembre del 2010",
    descripcion_grafico="República de Guatemala, serie histórica, adimensional",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
subcap_data = datos.serie_inflacion(0, 'interanual')
reporte.agregar_subcapitulo(
    titulo="Evolución del ritmo inflacionario",
    titulo_grafico="Ritmo inflacionario",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
subcap_data = datos.serie_inflacion(0, 'acumulada')
reporte.agregar_subcapitulo(
    titulo="Evolución de la variación acumulada del IPC",
    titulo_grafico="Variación acumulada del IPC",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="columna",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.serie_inflacion(0, 'intermensual')
reporte.agregar_subcapitulo(
    titulo="Evolución de la variación mensual del IPC",
    titulo_grafico="Variación intermensual del IPC",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
subcap_data = datos.incidencias_divisiones(0)
reporte.agregar_subcapitulo(
    titulo="Incidencias mensuales por división",
    titulo_grafico="Incidencias mensuales",
    descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="barra",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.incidencias_gba(0, True)
reporte.agregar_subcapitulo(
    titulo="Productos con mayor impacto positivo en la variación mensual",
    titulo_grafico="Gastos básicos con mayor incidencia positiva",
    descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="barra",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.incidencias_gba(0, False)
reporte.agregar_subcapitulo(
    titulo="Productos con mayor impacto negativo en la variación mensual",
    titulo_grafico="Gastos básicos con mayor incidencia negativa",
    descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="barra",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.serie_poder_adquisitivo(0)
reporte.agregar_subcapitulo(
    titulo="Valor del Quetzal",
    titulo_grafico="Poder adquisitivo del quetzal",
    descripcion_grafico="República de Guatemala, serie histórica, adimensional",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico={"precision":2, "Q4Etiquetas":True}
)
subcap_data = datos.serie_historica_mensual_inflacion(0, 'intermensual')
reporte.agregar_subcapitulo(
    titulo="Evolución de la variación mensual del IPC",
    titulo_grafico="Variación mensual del IPC",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="columna",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.serie_historica_mensual_inflacion(0, 'interanual')
reporte.agregar_subcapitulo(
    titulo="Evolución del ritmo inflacionario",
    titulo_grafico="Ritmo inflacionario",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="columna",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
# mapas
subcap_data = datos.ipc_regiones()
reporte.agregar_subcapitulo(
    titulo="Mapa de IPC",
    titulo_grafico="Número indice",
    descripcion_grafico=f"República de Guatemala, {fecha}, adimensional",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="mapa_colorimetrico",
    data=subcap_data[0],
    opciones_grafico={}
)
subcap_data = datos.inflacion_interanual_regiones()
reporte.agregar_subcapitulo(
    titulo="Mapa del ritmo inflacionario",
    titulo_grafico="Ritmo inflacionario",
    descripcion_grafico=f"República de Guatemala, {fecha}, adimensional",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="mapa_colorimetrico",
    data=subcap_data[0],
    opciones_grafico={}
)

# capitulos regionales
region = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII'
}
for RegCod in range(1, 9):
    reporte.agregar_capitulo(
        titulo=f"Resultados para la región {region[RegCod]}"
    )
    subcap_data = datos.serie_IPC(RegCod)
    reporte.agregar_subcapitulo(
        titulo=f"Evolución del índice en la región {region[RegCod]}",
        titulo_grafico="Índice de la región, base diciembre del 2010",
        descripcion_grafico=f"Región {region[RegCod]}, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(RegCod, 'interanual', nivel=f'en la región {region[RegCod]}')
    reporte.agregar_subcapitulo(
        titulo=f"Evolución del ritmo inflacionario en la región {region[RegCod]}",
        titulo_grafico="Ritmo inflacionario",
        descripcion_grafico=f"Región {region[RegCod]}, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(RegCod, 'acumulada', nivel=f'en la región {region[RegCod]}')
    reporte.agregar_subcapitulo(
        titulo=f"Evolución de la variación acumulada del índice en la región {region[RegCod]}",
        titulo_grafico="Variación acumulada del índice",
        descripcion_grafico=f"Región {region[RegCod]}, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="columna",
        data=subcap_data[0],
        opciones_grafico={}
    )
    subcap_data = datos.serie_inflacion(RegCod, 'intermensual', nivel=f'en la región {region[RegCod]}')
    reporte.agregar_subcapitulo(
        titulo=f"Evolución de la variación mensual del índice en la región {region[RegCod]}",
        titulo_grafico="Variación intermensual del índice",
        descripcion_grafico=f"Región {region[RegCod]}, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.incidencias_divisiones(RegCod)
    reporte.agregar_subcapitulo(
        titulo="Incidencias mensuales por división de gasto básico",
        titulo_grafico="Incidencias mensuales",
        descripcion_grafico=f"Región {region[RegCod]}, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.incidencias_gba(RegCod, True)
    reporte.agregar_subcapitulo(
        titulo="Gastos básicos con mayor impacto positivo en la variación mensual",
        titulo_grafico="Gastos básicos con mayor incidencia positiva",
        descripcion_grafico=f"Región {region[RegCod]}, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.incidencias_gba(RegCod, False)
    reporte.agregar_subcapitulo(
        titulo="Gastos básicos con mayor impacto negativo en la variación mensual",
        titulo_grafico="Gastos básicos con mayor incidencia negativa",
        descripcion_grafico=f"Región {region[RegCod]}, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )

#capitulo 4
reporte.agregar_capitulo(
    titulo="Anexos",
    anexo=True
)
datos_gba = datos.series_Gba(0)
for Gba in datos_gba:
    nombre = Gba[0]
    datosGba = Gba[1]
    desc = Gba[2]
    reporte.agregar_subcapitulo(
        titulo=f"Evolución del índice del producto {nombre}",
        titulo_grafico="IPC, base diciembre del 2010",
        descripcion_grafico="República de Guatemala, serie histórica, adimensional",
        descripcion=desc,
        fuente="INE",
        tipo_grafico="lineal",
        data=datosGba,
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )

reporte.set_formulas('formulas_ipc.tex')
reporte.crear_reporte()
