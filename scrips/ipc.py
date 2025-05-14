from utilsjo import mes_by_ordinal
from INEipc import DatosIPC
from INEreporte import Reporte

mes_datos = 4
anio = 2025

if (anio == 2024):
    narrower = -(mes_datos + 1)
else:
    narrower = -13

fecha = f"{mes_by_ordinal(mes_datos, abreviado=False).capitalize()} {anio}"
datos = DatosIPC(anio, mes_datos, dbBackup=1)

reporte = Reporte(
    nombre_reporte="Índice de Precios al Consumidor",
    anio = anio + (mes_datos == 12),
    mes= (mes_datos % 12) + 1,
    periodo=fecha
)

subcap_data_imputacion = ([
    ('Abr-2024', 5.79),
    ('May-2024', 4.87),
    ('Jun-2024', 5.12),
    ('Jul-2024', 6.09),
    ('Ago-2024', 6.10),
    ('Sep-2024', 5.94),
    ('Oct-2024', 5.40),
    ('Nov-2024', 8.27),
    ('Dic-2024', 4.21),
    ('Ene-2025', 4.21),
    ('Feb-2025', 3.62),
    ('Mar-2025', 3.27),
    ('Abr-2025', 3.04)],
    'El porcentaje de precios imputados en Abril 2025 es de 3.04%. El mayor porcentaje de imputaciones fue en el mes de Noviembre 2024 con una cantidad de 8.27% y el menor se encuentra en el mes de Abril 2025 con una cantidad de 3.04%.')

# capitulo 1
reporte.presentacion(datos.introduccion())
reporte.agregar_capitulo(
    titulo="Detalle del operativo de campo del IPC"
)
#subcap_data = datos.serie_fuentes()
subcap_data = ([
    ('Abr-2024', 13331),
    ('May-2024', 14161),
    ('Jun-2024', 14755),
    ('Jul-2024', 15136),
    ('Ago-2024', 15694),
    ('Sep-2024', 15816),
    ('Oct-2024', 16177),
    ('Nov-2024', 16346),
    ('Dic-2024', 16790),
    ('Ene-2025', 17016),
    ('Feb-2025', 17240),
    ('Mar-2025', 17424),
    ('Abr-2025', 17627)],
    'En el período actual, se consultaron un total de 17,627 fuentes. Al revisar los registros históricos, se identificó un máximo en el mes de abril 2025, con 17,627 y un mínimo en el mes de abril 2024, con 13,331.')
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
#subcap_data = datos.serie_precios()
subcap_data = ([
    ('Abr-2024', 65179),
    ('May-2024', 71320),
    ('Jun-2024', 76094),
    ('Jul-2024', 79461),
    ('Ago-2024', 82755),
    ('Sep-2024', 85736),
    ('Oct-2024', 87542),
    ('Nov-2024', 89670),
    ('Dic-2024', 86629),
    ('Ene-2025', 88097),
    ('Feb-2025', 90248),
    ('Mar-2025', 91795),
    ('Abr-2025', 93189)],
    'Durante el mes de abril 2025, se recopilaron un total de 93,189 precios. La máxima incidencia se registró en el mes de abril 2025 con 93,189, en contraste con la cifra mínima evidenciada en abril 2024, la cual totalizó 65,179 observaciones.')
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
dummy_text = ' '
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
subcap_data = ([('Abr-2024', 119.249816520776),
    ('May-2024', 120.489158118856),
    ('Jun-2024', 120.99067025564),
    ('Jul-2024', 120.88184059069),
    ('Ago-2024', 121.668127420186),
    ('Sep-2024', 124.589672840668),
    ('Oct-2024', 126.939829507029),
    ('Nov-2024', 127.711988303031),
    ('Dic-2024', 127.409588438044),
    ('Ene-2025', 124.705781876722),
    ('Feb-2025', 126.939829507029),
    ('Mar-2025', 127.069597012416),
    ('Abr-2025', 128.286892336038)],
    'En abril 2025, el índice de precios de los alimentos\\footnote{El índice de precios de los alimentos de la FAO es una medida de la variación mensual de los precios internacionales de una canasta de productos alimenticios. Consiste en el promedio de los índices de precios de cinco grupos de productos, ponderado con las cuotas medias de exportación de cada uno de los grupos para 2002-2004.} de la FAO\\footnote{Organización de las Naciones Unidas para la Alimentación y la Agricultura.} se situó en 128.29 puntos, lo que supone una variación de 7.58% respecto a abril 2024, y del 0.96% respecto a marzo 2025.')
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
#subcap_data = ([('2023-Dic', 71.9),
#    ('2024-Ene', 74.15238095238094),
#    ('2024-Feb', 77.24900000000001),
#    ('2024-Mar', 81.27800000000002),
#    ('2024-Abr', 85.34727272727272),
#    ('2024-May', 80.02454545454546),
#    ('2024-Jun', 79.76736842105262),
#    ('2024-Jul', 81.80045454545454),
#    ('2024-Ago', 76.68318181818182),
#    ('2024-Sep', 70.236),
#    ('2024-Oct', 71.985),
#    ('2024-Nov', 69.95),
#    ('2024-Dic', 70.11809523809525)],
#    'En diciembre 2024, el precio internacional del petróleo\\footnote{Se refiere al crudo West Texas Intermediate (WTI) producido en Texas y el sur de Oklahoma} se situó en un promedio de US$70.12 por barril, reflejando una variación de -2.48% en comparación con diciembre 2023 y de 0.24% en relación con noviembre 2024.')

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
subcap_data = datos.cambio_quetzal()
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

subcap_data = datos.tasa_interes()

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
#subcap_data = datos.ipc_mex()
subcap_data = ([
    ('Mar-2024', 4.44),
    ('Abr-2024', 4.63),
    ('May-2024', 4.68),
    ('Jun-2024', 4.98),
    ('Jul-2024', 5.59),
    ('Ago-2024', 5.03),
    ('Sep-2024', 4.60),
    ('Oct-2024', 4.77),
    ('Nov-2024', 4.58),
    ('Dic-2024', 4.19),
    ('Ene-2025', 3.58),
    ('Feb-2025', 3.78),
    ('Mar-2025', 3.80)],
    'Durante el período comprendido entre marzo 2024 y marzo 2025, México\\footnote{Para mayor información sobre el índice de precios al consumidor en México, visite \\url{http://www.inegi.org.mx}.} experimentó un cambio en su ritmo inflacionario, de un 4.44% a un 3.80%, lo que representa una desaceleración en 0.64 puntos.')

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

subcap_data = datos.inflacion_CA_RD_MEX()

#subcap_data = ([('País', 'Nov-2023', 'Nov-2024'),
#  ('Guatemala', 4.301973478124688, 1.6518169986985631),
#  ('El Salvador', 2.10765494006111, -0.29926335174953467),
#  ('Honduras', 5.035971223021574, 3.944260746339179),
#  ('Nicaragua', 5.6438453352252616, 3.7238507773412532),
#  ('Costa Rica', -1.6533381256177537, -0.0913659205116546),
#  ('Republica Dominicana', 4.000991981483004, 3.179397504172954),
#  ('Panamá', 1.949860724233976, -0.2641165755919772),
#  ('México', 4.285714285714293, 4.584474885844747)],
# 'Para el mes de noviembre 2024, en Centro América, República Dominicana y México, México presentó el mayor ritmo inflacionario de 4.58%, mientras que El Salvador registró el ritmo inflacionario más bajo con un nivel de -0.30%.')

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
    titulo_grafico="IPC base año 2024",
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
#subcap_data = ([('Ene-2012', 0.09416195856872811),
#  ('Ene-2013', 0.49153468050247007),
#  ('Ene-2014', 0.2528775723753096),
#  ('Ene-2015', -0.3557513128917611),
#  ('Ene-2016', 0.9122287968441833),
#  ('Ene-2017', 0.5203816131829964),
#  ('Ene-2018', -0.39543385809148734),
#  ('Ene-2019', 1.34908481003424),
#  ('Ene-2020', -0.2397743300423083),
#  ('Ene-2021', 0.15473627556514824),
#  ('Ene-2022', -0.03916449086163176),
#  ('Ene-2023', 0.3764565282342369),
#  ('Ene-2024', -1.143304021041902),
#  ('Ene-2025', 0.5014633313252803)],
# 'La variación acumulada en enero 2025 fue de 0.50%, marcando un aumento respecto al valor alcanzado en enero 2024, que fue del -1.14%. Dentro del período de enero 2012 a enero 2025 se observaron fluctuaciones, con el punto más bajo en enero 2024 (-1.14%) y el más alto en enero 2019 (1.35%).')

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
    titulo="Productos con mayor incidencia positiva en la variación mensual",
    titulo_grafico="Productos con mayor incidencia positiva",
    descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="barra",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
subcap_data = datos.incidencias_gba(0, False)
reporte.agregar_subcapitulo(
    titulo="Productos con mayor incidencia negativa en la variación mensual",
    titulo_grafico="Productos con mayor incidencia negativa",
    descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="barra",
    data=subcap_data[0],
    opciones_grafico={"precision":2}
)
#subcap_data = datos.serie_poder_adquisitivo(0)
subcap_data = ([
#    ('Dic-2023', 1),
#    ('Ene-2024', 0.999736009709276),
#    ('Feb-2024', 0.998343159675634),
#    ('Mar-2024', 0.995271831777801),
    ('Abr-2024', 0.992333539940821),
    ('May-2024', 0.9920509304358347),
    ('Jun-2024', 0.992050930435833),
    ('Jul-2024', 0.982038033350994),
    ('Ago-2024', 0.9826504082812246),
    ('Sep-2024', 0.986369601096231),
    ('Oct-2024', 0.98313472989565),
    ('Nov-2024', 0.98480400650177),
    ('Dic-2024', 0.983256565319603),
    ('Ene-2025', 0.978350496328685),
    ('Feb-2025', 0.9807881766776107),
    ('Mar-2025', 0.9798549408432344),
    ('Abr-2025', 0.9779525333020441)],
    'El quetzal experimentó una pérdida de 0.02 centavos en su poder adquisitivo en comparación con diciembre de 2023, lo que significa que un quetzal de abril de 2025 equivale a 0.98 centavos en diciembre 2023. En la base año 2024 se continua usando el mes de diciembre 2023 como referencia para el poder adquisitivo.')

reporte.agregar_subcapitulo(
    titulo="Poder aquisitivo del Quetzal",
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
        titulo_grafico="Índice de la región, base año 2024",
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
        titulo="Incidencias mensuales por división de gastos",
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
        titulo="Productos con mayor incidencia positiva en la variación mensual",
        titulo_grafico="Productos con mayor incidencia positiva",
        descripcion_grafico=f"Región {region[RegCod]}, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.incidencias_gba(RegCod, False)
    reporte.agregar_subcapitulo(
        titulo="Productos con mayor incidencia negativa en la variación mensual",
        titulo_grafico="Productos con mayor incidencia negativa",
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
        titulo_grafico="IPC, base año 2024",
        descripcion_grafico="República de Guatemala, serie histórica, adimensional",
        descripcion=desc,
        fuente="INE",
        tipo_grafico="lineal",
        data=datosGba,
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
        #opciones_grafico={"precision":2}
    )
reporte.set_formulas('formulas_ipc.tex')
reporte.crear_reporte()
