import datetime

meses = {}
meses["1"]= "Enero"
meses["2"]= "Febrero"
meses["3"] = "Marzo"
meses["4"]= "Abril"
meses["5"]= "Mayo"
meses["6"] = "Junio"
meses["7"]= "Julio"
meses["8"]= "Agosto"
meses["9"] = "Setiembre"
meses["10"]= "Octubre"
meses["11"]= "Noviembre"
meses["12"] = "Diciembre"

def get_sp_previous_month(input):
    first = input.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    result = meses[lastMonth.strftime("%m")]
    return  result

if __name__ == '__main__':
    today = datetime.date.today()
    print(get_sp_month(today))
