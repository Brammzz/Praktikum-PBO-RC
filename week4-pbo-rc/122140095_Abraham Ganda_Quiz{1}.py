import random

class Minesweeper:
    def __init__(self, size = 3):
        self.size = size
        self.matrik = [['?' for _ in range(size)] for _ in range (size)]
        self.baris_matrik = random.randint(0,2)
        self.kolom_matrik = random.randint(0,2)
        self.winner = True

    def matriks(self):
        for baris in self.matrik:
            print(' '.join(baris))
        print()

    def letak_bomb(self):
        self.matrik[self.baris_matrik][self.kolom_matrik] = 'X'

    def isi_matriks(self, baris, kolom):
        if self.matrik[baris][kolom] == 'X':
            self.winner = False
            print('Kamu kalah karena terkena bom')

        self.matrik[baris][kolom] = 'X'
        if self.cek():
            self.winner = True
            print('Anda memenangkan game ini')

    def cek(self):
        for baris in self.matrik:
            if '?' in baris:
                return False
        return True

mulai_game = Minesweeper()
mulai_game.letak_bomb()
mulai_game.matriks()

while mulai_game.winner:
    baris = int(input('Masukkan baris dari (0-2):'))
    kolom = int(input('Masukkan kolom dari (0-2):'))
    mulai_game.isi_matriks(baris, kolom)
    mulai_game.matriks()
