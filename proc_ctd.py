# Script para LER dados de CTD, REMOVER spikes, PLOTAR e SALVAR os dados limpos
# Autor:  varios
# Novembro de 2014
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='ctd_bruto.cnv')
parser.add_argument('-o', '--output', default='ctd_tratado.txt')
args = parser.parse_args()

filename = args.filename
output = args.output
print "filename = %s" %filename
print "output = %s" %output


def read_ctd():
    pass 


def remove_spike():
    pass


def plot():
    pass


def export_data():
    pass