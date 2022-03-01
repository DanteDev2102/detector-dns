'''
Registros MX, registros de intercambio de correo, definen el nombre de dominio del servidor de correo;
Registro CNAME, se refiere al registro de alias, que realiza el mapeo entre nombres de dominio;
Registros NS, servidores de nombres de dominio y subdominios autorizados del área marcada;
Registro PTR, análisis inverso, contrario al registro A, convertir IP en nombre de host;
Registro SOA, marca SOA, la definición de una zona de autorización inicial
A = Registro de Host
NS = Registro de Servidores
'''

import dns.resolver

def main(domain,type):
    analist = dns.resolver.query( domain, type )
    try:
        if type == 'CNAME':
            for i in analist.response.answer:
                for j in i.items:
                    print (j.to_text())
        elif type == 'A':
            for i in analist.response.answer:
                for j in i.items:
                    print( j.address )
        elif type == 'MX':
            for i in analist:
                print( f'MX preference = {i.preference}\nmail exchanger = {i.exchange}' )
        else:
            for query in analist:
                print( query )
    except:
        print('no se pudo encontrar la dns')
        if __name__ == '__name__':
            try:
                main( domain, type )
            except KeyboardInterrupt:
                exit( 1 )

print(_name_)
domain = input('Enter to domain: ')
type = input('Enter type query: ')

main(domain,type)

