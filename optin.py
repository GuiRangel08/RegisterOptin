import logging
import json
import requests  
import time
#from requests.exceptions import HTTPError

BASE_URL_OPTIN = 'https://app3.mktzap.com.br/api/v1/optin'

def register_optin(contacts, broker_number,company_id, token):
    log = []
    with requests.Session() as session:

        log_filename = f'log/{company_id}_{time.strftime("%Y%m%d-%H%M%S")}.log'
        logging.basicConfig(filename= log_filename, encoding='utf-8', level=logging.INFO)

        for contact in contacts:
            try:
                body_params = get_body_params(contact, broker_number,company_id)
                response = session.post(BASE_URL_OPTIN, data=body_params, headers=get_headers(token))
                
                logging.info(f'{time.strftime("%H:%M:%S")} - {company_id} - {contact}: {json.loads(response.content)}')
            except Exception as err:
                print(err)
                exit()

def get_body_params(number, broker_number, company_id):
    data = {
        "broker_phone": broker_number,
        "contact_phone": number,
        "company_id": company_id
    }

    return json.dumps(data)

def get_headers(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return headers

