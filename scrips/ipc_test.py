from ineipc.datosipc import datosIPC

from funcionesjo import mes_by_ordinal
from reporteine.reporteine import ReporteINE

fecha = f"{mes_by_ordinal(5, abreviado=False).capitalize()} {2023}"
datos = datosIPC(2023, 5, dbBackup=1)
reporte = ReporteINE("Índice de Precios al Consumidor", 2023, 5)

subcap_data_imputacion = ([('May-2022', 3.3731644580470808),
  ('Jun-2022', 3.4859976662777132),
  ('Jul-2022', 4.3942410340748435),
  ('Ago-2022', 3.0303989867004435),
  ('Sep-2022', 4.4351846566584845),
  ('Oct-2022', 5.289202323100628),
  ('Nov-2022', 3.286537608984779),
  ('Dic-2022', 4.28484415137311),
  ('Ene-2023', 3.240628778718259),
  ('Feb-2023', 2.070393374741201),
  ('Mar-2023', 2.8352349686631926),
  ('Abr-2023', 1.6),
  ('May-2023', 1.2)],
 'El porcentaje de precios imputados en mayo 2023 es de 1.22%. El mayor porcentaje de imputaciones fue en el mes de octubre 2022 con una cantidad de 5.28% y el menor se encuentra en el mes de mqyo 2023 con una cantidad de 1.22%.')


subcap_data_fuentes = ([('May-2022', 6020),
  ('Jun-2022', 6733),
  ('Jul-2022', 7114),
  ('Ago-2022', 6089),
  ('Sep-2022', 6776),
  ('Oct-2022', 6992),
  ('Nov-2022', 7149),
  ('Dic-2022', 7691),
  ('Ene-2023', 8618),
  ('Feb-2023', 8047),
  ('Mar-2023', 8529),
  ('Abr-2023', 8680),
  ('May-2023', 8049)],
 'La cantidad de fuentes consultadas en mayo 2023 es de 8,049. La mayor cantidad de fuentes consultadas fue en el mes de abril 2023 con una cantidad de 8,680 y la menor se encuentra en el mes de mayo 2022 con una cantidad de 6,020.')


subcap_data_precios = ([('May-2022', 31533),
  ('Jun-2022', 34240),
  ('Jul-2022', 34900),
  ('Ago-2022', 32350),
  ('Sep-2022', 35368),
  ('Oct-2022', 35877),
  ('Nov-2022', 38182),
  ('Dic-2022', 41434),
  ('Ene-2023', 44643),
  ('Feb-2023', 44050),
  ('Mar-2023', 46046),
  ('Abr-2023', 46252),
  ('May-2023', 45403)],
 'La cantidad de precios diligenciados en mayo 2023 es de 45,403. La mayor cantidad de precios diligenciados fue en el mes de abril 2023 con una cantidad de 46,252 y la menor se encuentra en el mes de mayo 2022 con una cantidad de 31,533.')


# capitulo 1
reporte.presentacion(datos.introduccion())
reporte.agregar_capitulo(
    titulo="Detalle del operativo de campo del IPC"
)
subcap_data = subcap_data_fuentes
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
subcap_data = subcap_data_precios
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
    opciones_grafico={"precision":1}
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
    opciones_grafico={"precision":1}
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
    titulo="Evolución del cambio anual del IPC (Ritmo Inflacionario)",
    titulo_grafico="Variación interanual del IPC",
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
    opciones_grafico={}
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
    titulo="Incidencias mensuales por división de gasto básico",
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
    titulo="Gastos básicos con mayor impacto positivo en la variación mensual",
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
    titulo="Gastos básicos con mayor impacto negativo en la variación mensual",
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
subcap_data = datos.serie_historica("mensual")
reporte.agregar_subcapitulo(
    titulo="Serie histórica del la variación mensual",
    titulo_grafico="Variación intermensual del IPC",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico=dict(Q4Etiquetas=True, etiquetaCadaSeis=True)
)
subcap_data = datos.serie_historica("anual")
reporte.agregar_subcapitulo(
    titulo="Serie histórica del ritmo inflacionario",
    titulo_grafico="Variación interanual del IPC",
    descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
    descripcion=subcap_data[1],
    fuente="INE",
    tipo_grafico="lineal",
    data=subcap_data[0],
    opciones_grafico=dict(Q4Etiquetas=True, etiquetaCadaSeis=True)
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
        descripcion_grafico=f"Region {region[RegCod]}, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(RegCod, 'interanual', nivel=f'en la región {region[RegCod]}')
    reporte.agregar_subcapitulo(
        titulo=f"Evolución de la variación interanual del índice en la región {region[RegCod]}",
        titulo_grafico="Variación interanual del índice",
        descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
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
        descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
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
        descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
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
        descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
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
        descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
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
        descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
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
        titulo=f"Evolución del índice del gasto básico {nombre}",
        titulo_grafico="IPC, base diciembre del 2010",
        descripcion_grafico="República de Guatemala, serie histórica, adimensional",
        descripcion=desc,
        fuente="INE",
        tipo_grafico="lineal",
        data=datosGba,
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )

reporte.crear_reporte()
reporte.compilar_reporte()
reporte.compilar_reporte()