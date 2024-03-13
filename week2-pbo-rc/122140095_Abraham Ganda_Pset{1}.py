import random

class ayah:
    def __init__(self, gol_darah):
        self.gol_darah = gol_darah

class ibu:
    def __init__(self, gol_darah):
        self.gol_darah = gol_darah

class anak(ayah, ibu):
    def __init__(self, ayah, ibu):
        self.ayah = ayah
        self.ibu = ibu
        super().__init__(ayah.gol_darah) 
        self.gol_darah_ibu = ibu.gol_darah

    def cari_gol_darah_anak(self):
        alel = [self.gol_darah, self.gol_darah_ibu]
        alel_anak = random.choice(alel)
        print(f'Alel Anak adalah {alel_anak}')

        if alel_anak == 'AA':
            print('Golongan Darah Anak adalah A')
        elif alel_anak == 'AO' or alel_anak == 'OA':
            print('Golongan Darah Anak adalah A')
        elif alel_anak == 'AB' or alel_anak == 'BA':
            print('Golongan Darah Anak adalah AB')
        elif alel_anak == 'BB':
            print('Golongan Darah Anak adalah B')
        elif alel_anak == 'BO' or alel_anak == 'OB':
            print('Golongan Darah Anak adalah B')
        elif alel_anak == 'OO':
            print('Golongan Darah Anak adalah O')

print('Alel = AA, AO, AB, BB, BO, OO')
gol_darah_ayah = input("Input Alel Ayah: ").upper()
gol_darah_ibu = input("Input Alel Ibu: ").upper()

ayah = ayah(gol_darah_ayah)
ibu = ibu(gol_darah_ibu)

anak = anak(ayah, ibu)
anak.cari_gol_darah_anak()
