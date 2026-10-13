import json

PRECIOS = {
    "corte_cabello": 500,
    "corte_infantil": 400,
    "recorte_barba": 250,
    "corte_barba": 700,
    "afeitado_navaja": 350,
    "perfilado_cejas": 150,
    "limpieza_facial": 600,
    "lavado_cabello": 200,
    "corte_vip": 1000
}

AGENDA = {
    "09:00": None,
    "10:00": "Rambo",
    "11:00": None,
    "12:00": "Silvester Stallone",
    "13:00": None,
    "14:00": "Chuck Norris",
    "15:00": None,
    "16:00": None,
    "17:00": None,
    "18:00": None,

}

def _error(mensaje, **extra):
    return json.dumps({"error": mensaje, **extra}, ensure_ascii=False)

def horas_libres():
    #return [hora for hora, cliente in AGENDA.items() if cliente is None] se puede simplificar con esta linea o hacer normal
    libres = []
    for hora, cliente in AGENDA.items():
        if cliente is None:
            libres.append(hora)
    return libres

#-------------------Tipo CONSULTAR-------------------

def consultar(tipo_consulta):

    if tipo_consulta == "precios":

        precios = { servicio: precio for servicio, precio in PRECIOS.items() if precio is not None}
        return json.dumps({"precios" : precios}, ensure_ascii=False)

    elif tipo_consulta == "horas_libres":
        return json.dumps({"horas_libres" : horas_libres()}, ensure_ascii=False)

    elif tipo_consulta == "reservaciones":

        reservaciones = { hora: cliente for hora, cliente in AGENDA.items() if cliente is not None}
        return json.dumps({"reservaciones" : reservaciones}, ensure_ascii=False)

    else:
        return json.dumps({"error" : "Consulta no disponible"}, ensure_ascii=False)



if __name__ == "__main__":
    print(consultar("precios"))
    # print(consultar("horas_libres"))
    # print(consultar("reservaciones"))