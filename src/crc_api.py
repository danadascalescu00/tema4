import struct
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Scrieti aici numele voastre
    '''
    return "CRC API de la echipa XYXYYXY!"

def xor(a, b): 
   
    # initializam rezultatul
    result = [] 

    # pentru fiecare bit in range-ul dat de lungimea polinomului
    for i in range(1, len(b)): 
        if a[i] == b[i]: # daca sunt egali rezultatul e 0
            result.append('0') 
        else: # daca sunt diferiti, rezultatul e 1
            result.append('1') 

    return ''.join(result) 


def calculeaza_CRC(polinom, date):
    '''
    TODO: de implementat
    '''
    CRC = b''
    return CRC


@app.route('/crc', methods=['POST'])
def post_method():
    '''
    TODO: implementati aici un endpoint care calculeaza CRC
    '''
    #struct.unpack(....)
    #CRC = calculeaza_CRC()
    return request.data
    #return CRC


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
