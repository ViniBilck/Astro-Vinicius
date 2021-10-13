import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import make_lupton_rgb
from matplotlib.colors import LogNorm
from astropy.wcs import WCS


db_open = [fits.open('mapGalMer.fits'),
           fits.open('mapGalMer (1).fits'),
           fits.open('mapGalMer (2).fits'),
           fits.open('mapGalMer (3).fits'),
           fits.open('mapGalMer (4).fits'),
           fits.open('mapGalMer (5).fits')]


class Glx(object):

    def __init__(self, d):
        self.g1 = d[0]
        self.g2 = d[1]
        self.g3 = d[2]
        self.g4 = d[3]
        self.g5 = d[4]
        self.g6 = d[5]

    def Img_1_cor(self, data, nome):
        fig, (ax0) = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(18, 8))
        img = ax0.imshow(data, origin='lower', vmin=0.0001, vmax=0.6, extent=[0, -8.56e-5, 0, 8.56e-5], cmap='viridis')
        fig.colorbar(img)
        ax0.set_title('Galmer')
        plt.show()

def main(db):
    galaxia = Glx(db)
    print(WCS(galaxia.g1[0].header))
    galaxia.Img_1_cor(galaxia.g1[0].data,'gal1')






if __name__ == '__main__':
    main(db=db_open)
