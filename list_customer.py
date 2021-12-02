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
    sheet = spreadsheet.get_worksheet(2)

    # Extract and print all of the values
    clientes = sheet.get_all_records()
    #print(list_of_videos)
    nrows = len(clientes)
    return clientes

# def next_available_row(worksheet):
#     str_list = list(filter(None, worksheet.col_values(1)))
#     return len(str_list)+1
#
# index = next_available_row(sheet)
# row = ["Row", index, "inserted"]
# sheet.insert_row(row, index)

if __name__ == "__main__":
    clientes = get_clientes()
    for c in clientes:
        print(c["fecha"])
