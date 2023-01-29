import configparser
import json
# Cria um objeto de configuração
config = configparser.ConfigParser()

# Lê o arquivo my.cnf
config.read('conf/python.conf')

#debug
valor = config.get('system','array')
valor = json.loads(valor)
print(valor)
print(type(valor))