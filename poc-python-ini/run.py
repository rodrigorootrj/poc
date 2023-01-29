import configparser

# Cria um objeto de configuração
config = configparser.ConfigParser()

# Lê o arquivo my.cnf
config.read('conf/python.conf')

# Extrai o valor da porta do cabeçalho client
#port = config.get('client', 'port')
valor = config['client']['port']
print(valor)
valor = config['admin']['port']
print(valor)
valor = config.sections()
print(valor)
valor = 'client' in config
print(valor)
# Exibe o valor da porta
