
import pywhatkit
import sys
import keyboard
import time
import mes
from list_customer import get_clientes
from datetime import datetime, date



msgs = {}
msgs["1"] = "Lo saludamos desde Noretel sus servidores y atentamente le recordamos realizar el pago de su servicio"
msgs["2"] = "Se le recuerda la fecha de vencimiento del servicio ya transcurrió"
msgs["3"] = "Por favor cancele su servicio para evitar el corte y el costo de reconexión"

waittime = 15

def main(tipo):
    clientes = get_clientes()
    selected = (x for x in clientes if x["estado_ultimo_pago"] == "FALSE")


    for item in selected:
        now = datetime.now()
        hora = int(now.strftime("%H"))
        minuto = int(now.strftime("%M")) + 1
        today = date.today()

        if minuto == 60:
            hora += 1
            minuto = 0

        print("Current Time =", now)
        print("Cliente", item["id"], "telefono", item["telefono"], "mensaje", msgs[tipo])
        pywhatkit.sendwhatmsg(f"+{item['telefono']}", f"Estimad@ {item['nombre']}, {msgs[tipo]}. Su recibo vencido del mes de {mes.get_sp_previous_month(today)} tiene {item['dias_vencido']} dias vencido."  , hora, minuto, waittime, True, 8)


if __name__ == '__main__':
    tipo = sys.argv[1]
    main(tipo)
