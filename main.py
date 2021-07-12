from optin import register_optin
from file import *


def main():
    company_id = get_company_id()
    boker_number = get_broker_number()
    token = get_token()
    csv_filename = get_csv_filename()

    if file_exists(f'csv/{csv_filename}'):
        filepath = get_csv_filepath(csv_filename)
        contacts = csv_to_array(filepath)
        register_optin(contacts, boker_number, company_id, token)
    else:
        return 'Arquivo não existe\n'
    
    return True
        
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

def csv_to_array(csv_file_path):
    file = open(csv_file_path, "r")
    optins = []

    for line in file:
        optins.append(line.rstrip())

    file.close()

    return optins

if __name__ == '__main__':
     main()
