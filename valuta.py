import requests
import os
from dotenv import load_dotenv, set_key
import sys

ENV_FILE = '.env'

if '--key' in sys.argv:
    key_index = sys.argv.index('--key') + 1
    api_key = sys.argv[key_index]
    set_key(ENV_FILE, 'API_KEY', api_key)
    print('API key saved!')

load_dotenv()
key = os.getenv('API_KEY')

if not key:
    print('No API key found. Go: python3 valuta.py --key YOUR_API_KEY')
    sys.exit(1)


print('Write first currency')
firstValuta = input()

print('Write second currency')
secondValuta = input()

print('Write how much you want to exchange')
amount = input()


URL = f'https://v6.exchangerate-api.com/v6/{key}/pair/{firstValuta}/{secondValuta}/{amount}'

res = requests.get(URL)

data = res.json()




if str(data['result']) == 'error':
    if str(data['error-type']) == 'invalid-key':
        print('Wrong API key')
        print('Start program with python3 valuta.py --key DEN_RIGTIGE_NØGLE')
        sys.exit(1)
    else:
        print('There happened an error')
        print('Be sure that ypu write the correct currency')
        print('Example: euro = eur og dollars = usd')
        sys.exit()

print('Currency rate: ' + str(data['conversion_rate']))
print('Your exchange comes to: ' + str(data['conversion_result']) + ' ' + str(data['target_code']))

