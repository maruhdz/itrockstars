from urllib.request import urlopen
from urllib.parse import quote
import json
import sshtunnel
import mysql.connector

_host = 'irock.enroute.xyz'
_ssh_port = 22
_username = 'mhernandez'
_password = 'm4r14H3rn4nd3z!'


_remote_bind_address = 'localhost'
_local_mysql_port = 9990
_local_bind_address = '127.0.0.1'

_remote_mysql_port = 3306

_db_user = 'mhernandez'
_db_password = 'm4r14H3rn4nd3z!'
_db_name = 'mhernandez'


f=[]
url='https://maps.googleapis.com/maps/api/geocode/json?address=seville'
g=[]
with open('dir.txt') as file:
    for i in file:
        g.append(i)
        f.append(url+quote(i))

jsn=[]
respons=[]
for i,j in enumerate(f):
    print(i)
    respons.append(urlopen(j).read().decode('utf-8'))
    jsn.append(json.JSONDecoder().decode(respons[i]))


good=open(input('file name (.txt):'),'a')
print('Address','|',)
wrong=open(input('file name (.txt): '),'a')
for i in range(len(f)):
    if jsn[i]['status'] == 'OK':
        print(g[i], jsn[i]['status'],
              jsn[i]['results'][0]['geometry']['location']['lat'],
              jsn[i]['results'][0]['geometry']['location']['lng'],
                   sep='|',file=good)
    else:
        print(g[i], jsn[i]['status'],sep='|',file=wrong)


    _SQL = """insert into results(formated_address, latitud, longitud) values str("""+'"'+jsn[i]['results'][0]['formatted_address']+'"'+',"'+jsn[i]['results'][0]['geometry']['location']['lat']+'"'+',"'+jsn[i]['results'][0]['geometry']['location']['lng']+'")'
    with sshtunnel.SSHTunnelForwarder(
        (_host, _ssh_port),
        ssh_username=_username,
        ssh_password=_password,
        remote_bind_address=(_remote_bind_address, _remote_mysql_port),
        local_bind_address=(_local_bind_address, _local_mysql_port)
        ) as tunnel:
        conn = mysql.connector.connect(
        user=_db_user,
        password=_db_password,
        host=_local_bind_address,
        database=_db_name,
        port=_local_mysql_port)

    cursor = conn.cursor()
    conn.commit()
    cursor.close()
    conn.close()



good.close()
wrong.close()
