import logging
import json
import requests  
import time
#from requests.exceptions import HTTPError


BASE_URL_OPTIN = 'https://app3.mktzap.com.br/api/v1/optin'

def register_optin(contacts, broker_number,company_id, token):

    global CONTACTS
    global BROKER_NUMBER
    global COMPANY_ID
    global TOKEN
   
    CONTACTS = contacts
    BROKER_NUMBER = broker_number
    COMPANY_ID = company_id
    TOKEN = token

    start_time = time.time()

    print(f"\nIniciando inclusão...")

    log = []
    with requests.Session() as session:

        log_filename = f'log/{company_id}_{time.strftime("%Y%m%d-%H%M%S")}.log'
        logging.basicConfig(filename= log_filename, encoding='utf-8', level=logging.INFO)

        for contact in CONTACTS:
            try:
                body_params = get_body_params(contact)
                response = session.post(BASE_URL_OPTIN, data=body_params, headers=get_headers())
                
                logging.info(f'{time.strftime("%H:%M:%S")} - {COMPANY_ID} - {contact}: {json.loads(response.content)}')
            except Exception as err:
                print(err)
                exit()
    end_time = time.time() - start_time
    print(f'\nInclusão da lista de Optin finalizada em {end_time} segundos')

def get_body_params(number):
    data = {
        "broker_phone": BROKER_NUMBER,
        "contact_phone": number,
        "company_id": COMPANY_ID
    }

    return json.dumps(data)

def get_headers():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    return headers

