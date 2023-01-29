import configparser

# Cria um objeto de configuração
config = configparser.ConfigParser()

# Lê o arquivo my.cnf
config.read('python.conf')

#Ler todas as sessões(cabeçalhos) do arquivo.
debug_sectopn = config.sections()
print(debug_sectopn)
#Validar se uma sessão existe dentro do arquivo.
debug_validar = 'client' in config
print(debug_validar)
