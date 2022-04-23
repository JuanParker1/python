import pandas_datareader as pdr
from datetime import datetime,timedelta
import mplfinance as mpf

def valor(n):
    return n

dias=50
entidad="AMZN"
init_date=datetime.now() - timedelta(days=dias)      #Resto a la fecha actual el periodo de dias que quiero consultar, 
print("Fecha inicio: ",init_date)                   #es decir init_date SERA LA FECHA DESDE LA QUE INICIAREMOS LA RECOGIDA DE DATOS

info= pdr.get_data_yahoo(entidad,start=init_date)    #recupero de yahoo la info desde el dia "init_date" de la cotizacion de la empresa 'AAPL' y la leemos con pdr(panda_reader)


for i in info:                                      # Con esto obtenemos el nombre de todos los campos/columnas de la informacion obtenida
    print(i)

volumen=info["Volume"]                              #Recuperamos los datos de dicha columna en formato "panda.series.Series"    /////////   Para extraerla vale con anadir uno a uno los valores a una lista o convertilo en iterable y construir una lista con este, tal y como se hace acontinuacion

map_volumenes= map(valor,volumen)
volumenes=list(map_volumenes)
print(len(volumenes),volumenes)                     # Si se imprimen menos valores que los dias estipulados es porque no hay mercado los fines de semana


                                                    #info es un dato de tipo <class 'pandas.core.frame.DataFrame>
#print(info)                                         #Muestra toda la info

#print(info.head(10))                                #muestro la informacion de "head" y los 10 ||| primeros ||| datos recogidos. 
#print(info.tail(10))                                #si utilizo    ----------info.tail(10)---------- recogeria los ||| últimos ||| 10 datos recogidos  




                    #Crea un grafico de en este caso velas, segun el valor que tenga en "type"


#mpf.plot(info, type='candle', title=entidad+' prices (Last'+" "+str(dias)+" "+'days)', style='charles',volume=True)


                                                    # style=''  ==> predeterminado a 'no se lo, lo tengo que buscar', no es obligatorio
                                                    # volume=''  ==> predeterminado a False

