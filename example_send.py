from requests_pkcs12 import post

def send_request_with_cert_p12():

  host = 'example'
  
  file_p12 = pathlib.Path().cwd() / 'certs' / 'example@example.ru.p12'
  SERT_PASS = 'example'
  
  data = {}
  data['example'] = 'example'
  
  headers = {}
  headers['authorization'] = f'Bearer example'
  headers['accept'] = 'application/json'
  headers['content-type'] = 'application/json'

  response = post(host, 
                 data=data, 
                 headers=headers, 
                 pkcs12_filename=file_p12, 
                 pkcs12_password=SERT_PASS
                 )
  
  json_response = response.json()
  
  if response.status_code != 200:
      raise Exception(f'status code = {response.status_code}')

  return json_response

def send_request_with_cert_p12_TRC():

  host = 'example'
  
  file_p12 = pathlib.Path().cwd() / 'certs' / 'example@example.ru.p12'
  file_RTC = pathlib.Path().cwd() / 'certs' / 'russian-trusted-cacert.pem'
  SERT_PASS = 'example'
  
  data = {}
  data['example'] = 'example'
  
  headers = {}
  headers['authorization'] = f'Bearer example'
  headers['accept'] = 'application/json'
  headers['content-type'] = 'application/json'

  response = post(host, 
                 data=data, 
                 headers=headers, 
                 pkcs12_filename=file_p12, 
                 pkcs12_password=SERT_PASS,
                 verify=file_RTC
                 )
  
  json_response = response.json()
  
  if response.status_code != 200:
      raise Exception(f'status code = {response.status_code}')

  return json_response
