from ineipc.datosipc import datosIPC
from funcionesjo import mes_by_ordinal
from reporteine.reporteine import ReporteINE
#pip3 install git+https://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@github.com/1u1s4/reporteine.git
fecha = f"{mes_by_ordinal(5, abreviado=False).capitalize()} {2023}"
datos = datosIPC(2023, 5, dbBackup=1)

reporte = ReporteINE(
    nombre_reporte="Índice de Precios al Consumidor",
    anio=2023,
    mes=6,
    periodo="Mayo 2023"
)

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
  ('Abr-2023', 1.61),
  ('May-2023', 1.22)],
 'El porcentaje de precios imputados en mayo 2023 es de 1.22%. El mayor porcentaje de imputaciones fue en el mes de octubre 2022 con una cantidad de 5.28% y el menor se encuentra en el mes de mqyo 2023 con una cantidad de 1.22%.')

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
# diagramas
reporte.agregar_subcapitulo(
    titulo="Pre-diligenciamiento, recopilación, digitación y crítica (61 personas)",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion="",
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_01.tex",
    opciones_grafico={}
)
reporte.agregar_subcapitulo(
    titulo="Recopilación de precios y pesos por gramo (35 personas)",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion="",
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_02.tex",
    opciones_grafico={}
)
reporte.agregar_subcapitulo(
    titulo="Recopilación de datos por cotización (35 personas)",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion="",
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_03.tex",
    opciones_grafico={}
)
reporte.agregar_subcapitulo(
    titulo="Supervisión de recolección de datos",
    titulo_grafico="",
    descripcion_grafico="",
    descripcion="",
    fuente="INE",
    tipo_grafico="diagrama_tikz",
    data="diagramas/dgrm_ipc_04.tex",
    opciones_grafico={}
)

reporte.set_formulas('formulas_ipc.tex')
reporte.crear_reporte()