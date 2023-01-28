import time
from datetime import datetime
import redis
import os



def start():
    ctime = datetime.now()
    ts = int(round(ctime.timestamp()))
# Criando uma conexão com o banco Redis
    print('Iniciando inserção de dados no redis')
    REDIS_MASTER_NAME = os.environ.get('REDIS_MASTER_NAME')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    REDIS_ENDPOINTS = os.environ.get('REDIS_ENDPOINTS')

    print(type(ts))
    r = redis.Redis(host=REDIS_ENDPOINTS, port=6379, db=0)
    r.set(ts,'Rodrigo,{}'.format(ts))

if __name__ == "__main__":
    while True:
        start()
        time.sleep(1)