#! -*- coding:utf-8 -*-

# Script para LER dados de CTD, SEPARAR descida, PLOTAR e SALVAR uma figura
# Autor:  varios
# Novembro de 2014

# Importando os pacotes que serão utilizados
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

# Lendo o arquivo do CTD, separando o cabeçalho dos dados
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


def get_downcast(press, temp):
    dlim = press.index(min(press)) # depth limit before upcast
    temp = temp[0:dlim]
    new_press = press[0:dlim]
    
    return new_press, temp


def binage(var, depth, window):
	dD = window
	binned_data = []

	depth = np.round(depth)
	d0 = depth[0] # initial depth

	for k in range(len(depth)):
		try:
			di = np.where(depth == d0)[0][0]
			df = np.where(depth == depth[di] + dD)[0][0]
			binned_data.append( np.mean( var[di:df] ) )
			
			d0 += dD
		except: IndexError

	return binned_data		

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
new_press, temp1 = get_downcast(press, temp1)
new_press, temp2 = get_downcast(press, temp2)
plot(temp1, new_press, filename, 'Sensor 1')
plot(temp2, new_press, filename, 'Sensor 2')
savefig(figname, quality=quality)
plt.show()



