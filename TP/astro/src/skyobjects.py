class SkyObject:

    def __init__(self, row):
        self.ra = row.RA_ICRS
        self.dec = row.DE_ICRS
        self.mag = row.rmag
        self.emag = row.e_rmag
        self.sprob = row.rs * row.gs

    def isaStar(self):
        return bool(self.sprob)
        
    def isaGalaxy(self):
        return bool(not self.sprob)

class Star(SkyObject):

    def __init__(self,row):
        super().__init__(row)
        self.gmag = row.gmag
        self.egmag = row.e_gmag
        self.color = self.gmag - self.mag

class Galaxy(SkyObject):

    def __init__(self,row):
        super().__init__(row)
        self.dVrad = row.rdVrad
        self.dVell = row.rdVell
        self.PA = row.rPA

