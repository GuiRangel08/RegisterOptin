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