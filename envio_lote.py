
import pywhatkit
import sys
import keyboard
import time
import mes
from random import randrange
from list_customer import get_clientes
from datetime import datetime, date

waittime = 15

def main(tipo):
    clientes = get_clientes()
    print("Seleccionando los clientes de fuente de datos")

    selected = list(x for x in clientes if x["estado_ultimo_pago"] == "FALSE")
    
    print(f"Existen {len(selected)} clientes para proceso")

    try:
        for item in selected:
            print(f"Iniciando proceso para {item['nombre']}")
            now = datetime.now()
            hora = int(now.strftime("%H"))
            minuto = int(now.strftime("%M")) + 1
            today = date.today()
    
            if minuto == 60:
                hora += 1
                minuto = 0
               
            saludo, emoticon = {}, {}
            saludo[0] = "Hola Sr."
            saludo[1] = "Buen dia"
            saludo[2] = "Saludos cordiales"
            saludo[3] = "Estimad@"
            saludo[4] = "Estimado"
            
            emoticon[0] = "♫"
            emoticon[1] = "💘"
            emoticon[2] = "😙"
            emoticon[3] = ":cupid"   
            emoticon[4] = "💥"   
            emoticon[5] = "⛽"
            emoticon[6] = "🎸"   
            emoticon[7] = "✈"   
      
            
            
            msgs = {}
            msgs["1"] = "Lo saludamos desde Noretel sus servidores y atentamente le recordamos realizar el pago de su servicio."
            msgs["2"] = "Lo saludamos desde Noretel. Se le recuerda el pago de servicio de internet ya que la fecha de vencimiento del servicio ya transcurrió."
            msgs["3"] = "Enviamos un amable saludo. Por favor cancele su servicio para evitar el corte y el costo de reconexión."

            mother_text =  f"{saludo[randrange(len(saludo))]} {item['nombre']}, {msgs[tipo]}. Su recibo vencido del mes de {mes.get_sp_previous_month(today)} tiene {item['dias_vencido']} dias vencido. {emoticon[0]}"

            print("Current Time =", now)
            print("Cliente", item["id"], "telefono", item["telefono"], "mensaje", msgs[tipo])
            pywhatkit.sendwhatmsg( f"+{item['telefono']}", mother_text  , hora, minuto, waittime, True, 8)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    tipo = sys.argv[1]
    main(tipo)
