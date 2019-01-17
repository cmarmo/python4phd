from astroquery.vizier import Vizier
from astropy import coordinates as coords
import pandas as pd
from matplotlib import pyplot as pl

from skyobjects import SkyObject, Star, Galaxy
import starproc
import galaxyproc

def main():

    catalog_list = Vizier.find_catalogs('V/147')
    print({k:v.description for k,v in catalog_list.items()})

    co = coords.SkyCoord('0h8m05.63s +14d50m23.3s')
    v = Vizier(columns=['RA_ICRS','DE_ICRS','gmag','e_gmag','rmag',
                        'e_rmag','rdVrad','rdVell','rPA','rs','gs'],
               catalog='V/147')
    v.ROW_LIMIT = -1
    result = v.query_region(co, radius='0.1deg', catalog='V/147')
    result_df = result['V/147/sdss12'].to_pandas()

    star_cat = []
    galaxy_cat = []

    for i in range(0,len(result_df)):
        row = result_df.loc[i]
        myObject = SkyObject(row)
        if (myObject.isaStar()):
            myStar = Star(row)
            star_cat.append(myStar)
        if (myObject.isaGalaxy()):
            myGalaxy = Galaxy(row)
            galaxy_cat.append(myGalaxy)

    starproc.main(star_cat)
    galaxyproc.main(galaxy_cat)

if __name__ == "__main__":
    main()
