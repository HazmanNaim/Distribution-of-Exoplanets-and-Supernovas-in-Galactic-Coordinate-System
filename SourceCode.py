'''

Distribution of Exoplanets and Supernovas in Galactic Coordinate System
Exoplanets data are obtained from Kepler Space Telescope.
Supernova data are obtained from Asiago Astrophysical Observatory

'''
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl
import pandas as pd
import astropy.units as u
from astropy.coordinates import SkyCoord

#Reading the Data in csv format
#Each of the data has their own respective csv file
#Supernova data is in icrs coordinate system while exoplanet is in galactic coordinate system
data_supernova = pd.read_csv('supernova.csv')
data_exoplanet = pd.read_csv('exoplanet_list.csv')

#Assign supernova data to array
x_supernova = np.array(data_supernova.iloc[:,1]) #ra
y_supernova = np.array(data_supernova.iloc[:,2]) #dec
#Assign exoplanet data to array
x_exoplanet = np.array(data_exoplanet.iloc[:,2]) #glong
y_exoplanet = np.array(data_exoplanet.iloc[:,1]) #glat

#l for Galactic longitude and b for Galactic latitude
sn = SkyCoord(x_supernova[:], y_supernova[:], frame='icrs', unit=u.deg)
ex = SkyCoord(x_exoplanet[:], y_exoplanet[:], frame='galactic', unit=u.deg)


#Supernova data is in ICRS, must be converted to Galactic
#No need to convert Exoplanet data because it is already in Galactic
sn_galactic = sn.galactic
ex_galactic = ex.galactic

#plotting
fig = mpl.figure(figsize=(8,5))
ax = fig.add_subplot(1,1,1, aspect='equal')
ax.scatter(sn_galactic.l.degree, sn_galactic.b.degree, s=0.1, color='blue', alpha=1)
ax.scatter(ex_galactic.l.degree, ex_galactic.b.degree, s=0.1, color='red', alpha=1)
ax.set_xlim(360., 0.)
ax.set_ylim(-90., 90.)
ax.set_xlabel("Galactic Longitude")
ax.set_ylabel("Galactic Latitude")
fig.show()

#Converting to Aitoff Projection
#Supernova
sn_l_rad = sn_galactic.l.radian
sn_l_rad[sn_l_rad > np.pi] -= 2. * np.pi
sn_b_rad = sn_galactic.b.radian
#Exoplanet
ex_l_rad = ex_galactic.l.radian
ex_l_rad[ex_l_rad > np.pi] -= 2. * np.pi
ex_b_rad = ex_galactic.b.radian

#Plotting in Aitoff Projection
fig = mpl.figure(figsize=(8,5))
ax = fig.add_subplot(1,1,1, projection='aitoff')
ax.scatter(-sn_l_rad, sn_b_rad, s=0.1, color='blue', alpha=1) #The reason why negative for galactic longitude
ax.scatter(-ex_l_rad, ex_b_rad, s=0.1, color='red', alpha=1) #is because "mapping from inside issue
ax.grid()
# Renaming Galactic Longitude Axis to conventional format
mpl.xticks(ticks=np.radians([-150, -120, -90, -60, -30, 0, \
                             30, 60, 90, 120, 150]),
           labels=['150°', '120°', '90°', '60°', '30°', '0°', \
                   '330°', '300°', '270°', '240°', '210°'])

#Settings for Plot
titlefont = {'fontname':'Arial'}
mpl.title(label="Distribution of Supernova and Exoplanet \n in \n Galactic Coordinate System", fontsize=15, y=1.1, **titlefont)
mpl.legend(["Supernova","Exoplanet"], bbox_to_anchor=(1, 0.9), markerscale=25)
ax.set_xlabel("Galactic Longitude, l", x=0.6)
ax.set_ylabel("Galactic Latitude, b")
fig.show()

mpl.tight_layout()
mpl.savefig('DistributionSnEx.png', dpi=1000)
