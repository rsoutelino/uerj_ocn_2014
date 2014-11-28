#! -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import glob
from ctd_tools import EstacaoCTD
from mpl_toolkits.basemap import Basemap
import numpy as np
from matplotlib.mlab import griddata



filelist = glob.glob('dados_OSEII/*.cnv')
filelist.sort()


prof = -200

lon, lat, lonfull, latfull, temp, F = [], [], [], [], [], []

for filename in filelist:
	estacao = EstacaoCTD(filename)
	# estacao.remover_subida()
	# estacao.bin_average()
	# estacao.filter()

	print estacao.filename

	if estacao.PROF.min() < prof:
		f = np.where(estacao.PROF < prof)
		t = estacao.TEMP[:f[0][0]].mean()

		print "    Temp media nos primeiros %s m = %s" %(-prof, t)

		temp.append( t )
		F.append( f[0][0] )

		lon.append(estacao.lon)
		lat.append(estacao.lat)

	lonfull.append(estacao.lon)
	latfull.append(estacao.lat)


temp = np.array(temp)
lon = np.array(lon)
lat = np.array(lat)

xg = np.linspace(lon.min(), lon.max(), 100)
yg = np.linspace(lat.min(), lat.max(), 80)
xg, yg = np.meshgrid(xg, yg)

tg = griddata(lon, lat, temp, xg, yg)

m = Basemap(projection='cyl', resolution='i', llcrnrlat=-30.6,
	        llcrnrlon=-49.51, urcrnrlat=-18.16, urcrnrlon=-27.03)


m.fillcontinents()
# m.plot(lonfull, latfull, 'bo')
m.contourf(xg, yg, tg, 40)
cbar = plt.colorbar()
cbar.set_label('$^\circ C$')
plt.scatter(lon, lat, s=30, c=temp)
plt.savefig("temp_media_primeiros_%sm.png" %(-prof))
plt.show()









