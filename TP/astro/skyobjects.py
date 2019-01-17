def SkyObject(row):

    def __init__(self, row):
        self.ra = row.RA_ICRS
        self.dec = row.DE_ICRS
        self.mag = row.rmag
        self.emag = row.e_rmag
