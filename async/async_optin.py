from asyncio.locks import Semaphore
import logging
import json
import asyncio
import aiohttp
import time
import requests

BASE_URL_OPTIN = 'https://app3.mktzap.com.br/api/v1/optin'

def handle_optin(contacts, broker_number,company_id, token):
    
    global CONTACTS
    global BROKER_NUMBER
    global COMPANY_ID
    global TOKEN
    global LOG

    CONTACTS = contacts
    BROKER_NUMBER = broker_number
    COMPANY_ID = company_id
    TOKEN = token

    LOG = logging.getLogger()

    start_time = time.time()

    asyncio.run(register_optins())

    end = time.time()
    total_time = end - start_time

    print(f'A execução levou {total_time} segundos para ser concluída.')


def get_tasks(session):
    tasks = []
    for contact in CONTACTS:
        tasks.append(session.post(BASE_URL_OPTIN, data=get_body_params(contact), headers=get_headers(), ssl=False))
    return tasks

async def register_optins():
    log_filename = f'log/{COMPANY_ID}_{time.strftime("%Y%m%d-%H%M%S")}.log'
    logging.basicConfig(filename= log_filename, encoding='utf-8', level=logging.INFO)

    limit = asyncio.Semaphore(2)

    async with limit:
        async with aiohttp.ClientSession() as session: 
            tasks = get_tasks(session)
            try:
                responses = await asyncio.gather(*tasks)
                for response in responses:
                    LOG.info(f'{time.strftime("%H:%M:%S")} - {COMPANY_ID} - body: {await response.json()}, status: {response.status}')
            except Exception as err:
                print(err)

def get_body_params(contact):
    data = {
        "broker_phone": BROKER_NUMBER,
        "contact_phone": contact,
        "company_id": COMPANY_ID
    }

    return json.dumps(data)

def get_headers():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    return headers
