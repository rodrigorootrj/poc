import configparser

# Cria um objeto de configuração
config = configparser.ConfigParser()

# Lê o arquivo my.cnf
config.read('python.conf')

# Extrai o valor da porta do cabeçalho client
port = config.get('admin', 'port')
print(port)
