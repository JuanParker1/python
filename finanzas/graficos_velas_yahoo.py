import pandas_datareader as pdr
from datetime import datetime,timedelta
import mplfinance as mpf

dias=500
entidad="AMZN"
init_date=datetime.now() - timedelta(days=dias)      #Resto a la fecha actual el periodo de dias que quiero consultar, 
print("Fecha inicio: ",init_date)                   #es decir init_date SERA LA FECHA DESDE LA QUE INICIAREMOS LA RECOGIDA DE DATOS

info= pdr.get_data_yahoo(entidad,start=init_date)    #recupero de yahoo la info desde el dia "init_date" de la cotizacion de la empresa 'AAPL' y la leemos con pdr(panda_reader)
print(type(info))                                   #info es un dato de tipo <class 'pandas.core.frame.DataFrame>
#print(info)                                         #Muestra toda la info

print(info.head(10))                                #muestro la informacion de "head" y los 10 ||| primeros ||| datos recogidos. 
#print(info.tail(10))                               #si utilizo    ----------info.tail(10)---------- recogeria los ||| últimos ||| 10 datos recogidos    

mpf.plot(info, type='candle', title=entidad+' prices (Last'+" "+str(dias)+" "+'days)', style='charles',volume=True)

                                                    # style=''  ==> predeterminado a 'no se lo, lo tengo que buscar', no es obligatorio
                                                    # volume=''  ==> predeterminado a False

