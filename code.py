
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl
import pandas as pd
import astropy.units as u
from astropy.coordinates import SkyCoord

#Reading the Data in csv format
data_exoplanet = pd.read_csv('exoplanet_list.csv')
data_supernova = pd.read_csv('supernova.csv')

#Galactic Latitude is similar to Right Ascension
#Galactic Longitude is similar to Declination

#Use 'Panda' to read the array of data 
#"SkyCoord" is used to convert the data to galactic coordinate
#Exoplanets Data
x_exoplanet = np.array(data_exoplanet.iloc[:,2])
y_exoplanet = np.array(data_exoplanet.iloc[:,1])
eq1 = SkyCoord(x_exoplanet[:], y_exoplanet[:], frame='galactic', unit=u.deg)
gal1 = eq1.galactic
#Supernova Data
x_supernova = np.array(data_supernova.iloc[:,1])
y_supernova = np.array(data_supernova.iloc[:,2])
eq2 = SkyCoord(x_supernova[:], y_supernova[:], frame='galactic', unit=u.deg)
gal2 = eq2.galactic

#Plotting
titlefont = {'fontname':'Arial'}
mpl.figure(figsize=(100,100))
fig = mpl.figure()
ax = fig.add_subplot(111, projection="aitoff")
ax.set_xlabel("Galactic Longitude/Declination", x=0.6)
ax.set_ylabel("Galactic Latitude/Right Ascension")
mpl.grid(True)
mpl.scatter(gal1.l.wrap_at('180d').radian, gal1.b.radian, s=0.1, color='red')
mpl.scatter(gal2.l.wrap_at('180d').radian, gal2.b.radian, s=0.1, color='blue')
mpl.title(label="Distribution of Supernova and Exoplanet \n in \n Galactic Coordinate System", fontsize=15, y=1.1, **titlefont)
mpl.legend(["Exoplanet","Supernova"], bbox_to_anchor=(1, 0.9), markerscale=25)
mpl.tight_layout()
fig.show()
mpl.savefig('DistributionSnEx.png', dpi=1200)



