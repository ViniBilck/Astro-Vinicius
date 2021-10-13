import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import make_lupton_rgb
from matplotlib.colors import LogNorm
from astropy.wcs import WCS
import numpy as np


db_open = [fits.open('frame-g-006793-1-0130.fits'),
           fits.open('frame-i-006793-1-0130.fits'),
           fits.open('frame-r-006793-1-0130.fits'),
           fits.open('frame-u-006793-1-0130.fits'),
           fits.open('frame-z-006793-1-0130.fits')]


class Glx(object):

    def __init__(self, d):
        self.g = d[0]
        self.i = d[1]
        self.r = d[2]
        self.u = d[3]
        self.z = d[4]

    def img_rgb(self, nome='Galáxia'):
        ## rgb = make_lupton_rgb(self.i[0].data[8:1396,::], self.r[0].data[0:1388,::], self.g[0].data[12:1400,::], stretch=1, Q=10)
        rgb = make_lupton_rgb(self.i[0].data, self.g[0].data, self.u[0].data, stretch=1, Q=10)
        plt.imshow(rgb, origin='lower')
        plt.title(nome)
        plt.show()

    def Log_Norm(self):
        plt.imshow(self.r[0].data, cmap='gray', origin='lower', norm=LogNorm())
        plt.show()

    def Img_1_cor(self):
        fig, ((ax0, ax1, ax2), (ax3, ax4, ax5)) = plt.subplots(nrows=2, ncols=3, sharex=True, figsize=(18, 8))

        ax0.imshow(self.i[0].data, origin='lower', vmin=0.0001, vmax=0.6, cmap='RdBu')
        ax0.set_title('Filtro I')
        ax1.imshow(self.g[0].data, origin='lower', vmin=0.0001, vmax=0.6, cmap='RdBu')
        ax1.set_title('Filtro G')
        ax3.imshow(self.r[0].data, origin='lower', vmin=0.0001, vmax=0.6, cmap='RdBu')
        ax3.set_title('Filtro R')
        ax4.imshow(self.z[0].data, origin='lower', vmin=0.0001, vmax=0.6, cmap='RdBu')
        ax4.set_title('Filtro Z')
        ax5.imshow(self.u[0].data, origin='lower', vmin=0.0001, vmax=0.6, cmap='RdBu')
        ax5.set_title('Filtro U')

        fig.delaxes(ax=ax2)


        plt.show()

    def pl(self):
        g = self.g[0].data
        print(g.shape)
        print(g.min())
        print(g.max())
        print(g.mean())
        print(np.percentile(g.flatten(),3))
        print(np.percentile(g.flatten(), 97))


        fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharex=True, figsize=(18, 8))
        ax0.imshow(g, vmin=0.1, vmax=6, origin='lower', cmap='viridis')
        ax1.imshow(g, vmin=np.percentile(g.flatten(),5), vmax=np.percentile(g.flatten(), 95), origin='lower', cmap='viridis')
        plt.show()




def main(db):
    galaxia = Glx(db)
    galaxia.pl()






if __name__ == '__main__':
    main(db=db_open)
