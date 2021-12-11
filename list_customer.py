import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_clientes():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('drivedata_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    spreadsheet = client.open("shared_lists")
    sheet = spreadsheet.get_worksheet(3)

    # Extract and print all of the values
    clientes = sheet.get_all_records()
    
    print("Listado de clientes")
    print(len(clientes))
    #for c in clientes:
    #    print(c["nombre"])
    return clientes


if __name__ == "__main__":
    clientes = get_clientes()
    for c in clientes:
        print(c["nombre"], c["estado_ultimo_pago"])
