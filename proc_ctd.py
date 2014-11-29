#! -*- coding:utf-8 -*-

# Script para LER dados de CTD, SEPARAR descida, PLOTAR e SALVAR uma figura
# Autor:  varios
# Novembro de 2014

import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='data/ctd_bruto.cnv')
parser.add_argument('-o', '--figname', default='data/perfil_ctd.png')
parser.add_argument('-q', '--quality', default=90)
args = parser.parse_args()

filename = args.filename
figname  = args.figname
quality  = int(args.quality)


def read_ctd(filename):
    f = open(filename)
    lines = f.readlines()

    header = []
    data = []
    isData = False

    for line in lines:
        if not isData:
            header.append(line)
        else:
            data.append(line)

        if "END" in line:
            isData = True

    press = []
    temp1 = []
    temp2 = []

    for line in data:
        press.append( float( line.split()[0] ) * -1 )
        temp1.append( float( line.split()[1] ) )
        temp2.append( float( line.split()[2] ) )

    return press, temp1, temp2, header


def get_downcast():
    pass
#################################################
# Pensamos em fazer um loop que fizesse o que função diff do matlab faz (a 
# diferença entre o valor e seu antecessor). Assim identificariamos quando 
# o CTD estivesse começando a subir porque os valores seriam negativos.

#### Primeira Tentativa

# down=[]
# i=-1
# j=0

# for line in press:
#   i=i+1
#   j=j+1
#   if press[i]<press[j]:
#       down.append(line)

# Ele está dando erro the 'out of range'... achamos que é porque o índice 
# j ultrapassa o tamanho do press

# Além disto, precisamos fazer com que o down salve todas as variáveis não 
# só a pressão


# com o if ele armazena parte dos dados... mas mantem o formato da 
# variável press, mas com menos dados... achamos que acontece devido às 
# oscilações dos dados (que não são sempre crescentes ou descrescentes)
# Por isso pensamos em usar o while

#### Segunda tentativa

# down=[]
# i=0
# j=1

# while press[i]<=press[j]:
#   temp=press[i]
#   down.append(temp)
#   i=i+1
#   j=j+1

# Agora funciona... mas as oscilações cortam logo no começo...
# Pensamos em criar um limite de aceitação...  

### Terceira tentativa

# down=[]
# i=0
# j=1

# while press[j]-press[i]>=-0.2:
#   temp=press[i]
#   down.append(temp)
#   i=i+1
#   j=j+1

# Mas definir o limite está complicado... pois 0.2 só pega o início..
# mas 0.25 já pega todos os dados...

# Talvez usar uma média....
# Mas não conseguimos avançar a partir disto...
# Esperamos que ajude em algo... ao menos o que não fazer...

# Estas foram as nossas tentativas, mas talvez vocês pensem em algo diferente...
# Ana Paula, Bruno, Camila, Talitha
#################################################

def plot(temp, press, filename, sensor):
    plt.plot(temp, press, label=sensor)
    plt.grid('on')
    plt.title('Temp profile of %s' %(filename.split('/')[-1]) )
    plt.xlabel('Temperature')
    plt.ylabel('Pressure')
    plt.legend()


def savefig(figname, quality):
    plt.savefig(figname, dpi=quality)
    print "Figure saved on %s" %(figname)


press, temp1, temp2, header = read_ctd(filename)
# press, temp1, temp2 = get_downcast(press, temp1, temp2)
plot(temp1, press, filename, 'Sensor 1')
plot(temp2, press, filename, 'Sensor 2')
savefig(figname, quality=quality)
plt.show()



