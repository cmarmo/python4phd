from astroquery.vizier import Vizier
from astropy import coordinates as coords
import pandas as pd
from matplotlib import pyplot as pl

from skyobjects import SkyObject

def main():

    catalog_list = Vizier.find_catalogs('V/147')
    print({k:v.description for k,v in catalog_list.items()})

    co = coords.SkyCoord('0h8m05.63s +14d50m23.3s')
    Vizier.ROW_LIMIT = 1000
    v = Vizier(columns=['RA_ICRS','DE_ICRS','gmag','e_gmag','rmag','e_rmag','rdVrad','rdVell','rPA','rs','gs'],
               catalog='V/147')
    result = v.query_region(co, radius='0.1deg', catalog='V/147')
    result_df = result['V/147/sdss12'].to_pandas()
    #print(result_df.columns)

    star_cat = []
    galaxy_cat = []

    for i in range(0,len(result_df)):
        myObject = SkyObject(result_df[i])
        if (myObject.isaStar()):
            star_cat.append(myObject)
        if (myOject.isaGalaxy()):
            galaxy_cat.append(myObject)

    print(type(galaxy_cat))

if __name__ == "__main__":
    main()
