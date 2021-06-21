import os
from async_optin import handle_optin

def main():
    company_id = get_company_id()
    csv_filename = get_csv_filename()
    boker_number = get_broker_number()
    token = get_token()

    if file_exists(f'csv/{csv_filename}'):
        filepath = get_filepath(csv_filename)
        contacts = csv_to_array(filepath)
        handle_optin(contacts, boker_number, company_id, token)
    else:
        print('Arquivo não existe\n')
        
def get_company_id():
    company_id = input('Qual o id da filial?\n')
    try:
        company_id = int(company_id)
        return company_id
    except ValueError:
        print("Somente numeros sao aceitos. Tente novamente.\n")
        exit()

def get_broker_number():
    return input('Qual o número do broker?\n')

def get_token():
    return input('Qual o token da empresa?\n')

def get_csv_filename():
    filename = input('Qual o nome do arquivo .CSV?\n')
    return filename + '.csv'

def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False
    
def get_filepath(file):
    filepath = os.path.abspath(f'csv/{file}')
    return filepath

def csv_to_array(csvFilePath):
    file = open(csvFilePath, "r")
    optins = []

    for line in file:
        optins.append(line.rstrip())

    file.close()

    return optins

if __name__ == '__main__':
    main()
