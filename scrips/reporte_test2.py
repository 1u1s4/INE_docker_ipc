from reporteine.reporteine import ReporteINE

mes = 5
anio = 2023
reporte = ReporteINE("Hechos Delictivos", anio, mes)

# capitulo 1
reporte.presentacion("")
reporte.agregar_capitulo(
    titulo="Detalle del operativo de campo del IPC"
)

reporte.agregar_subcapitulo(
    titulo="Víctimas según causa",
    titulo_grafico="Víctimas de hechos delictivos en el primer trimestre 2014",
    descripcion_grafico="República de Guatemala, primer trimestre 2023, distribución porcentual por tipo de causa",
    descripcion="La distribución de víctimas por hechos delictivos según el tipo de delito, muestra que 2,407 fueron víctimas de delitos contra el patrimonio que representa el 44.64% del total de víctimas.",
    fuente="INE, con datos de la Policía Nacional Civil",
    tipo_grafico="barra",
    data=[('Contra el patrimonio', 44.64), ('Otras causas', 19.36), ('Lesiones', 12.54), ('Homicidios', 12.5), ('Contra la libertad', 10.96)],
    opciones_grafico=dict(Q4Etiquetas=True)
)

reporte.crear_reporte()
reporte.compilar_reporte()
reporte.compilar_reporte()