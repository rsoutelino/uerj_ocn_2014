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



