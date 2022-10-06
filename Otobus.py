"""Asim Aydin 20217170002"""
class Otobus:
    plaka:str = ''
    nereden:str = ''
    nereye:str = ''
    koltuk:int = 0
    
    def __init__(self,plaka,nereden,nereye,koltuk):
        self.plaka = plaka
        self.nereden = nereden
        self.nereye = nereye
        self.koltuk = koltuk
        
        

    

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        dolu = self.koltuk +1
        return dolu

        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        bos = self.koltuk - 1
        return bos
        

    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("{},{},{},{},{}".format(self.nereden,self.nereye,self.plaka,self.bilet_iade(),self.bilet_sat()))

        


