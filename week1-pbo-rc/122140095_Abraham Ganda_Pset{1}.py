class Robot:
  
    def __init__(self, nama, darah, serangan):
        self.nama = nama
        self.darah = darah
        self.serangan = serangan

    def attack(self, musuh, pilihan_robot, pilihan_musuh):
        print(f'{self.nama} Menyerang dengan {self.serangan} Kerusakaan pada {musuh.nama}')
        if pilihan_robot == 2 or pilihan_musuh == 2:
            pass
        else:
            musuh.darah -= self.serangan
            if musuh.darah <= 0:
                print(f'{musuh.nama} Mati')

    def defense(self, musuh, pilihan_robot, pilihan_musuh): 
        print(f'{self.nama} Berhasil Defense')
        self.darah -= musuh.serangan/2
        if self.darah <= 0:
            print(f'{self.nama} Mati')

    def life(self):
        return self.darah > 0

class Game:

    def __init__(self, robot, musuh):
        self.robot = robot
        self.musuh = musuh
        self.ronde = 0

    def play(self): 
        print('Games Start !!!\n')
        print('# Games Rules : ')
        print('# Opsi Attack digunakan untuk Menyerang lawan dengan power serangan saat ini')
        print('# Opsi Defense berfungsi untuk menahan serangan lawan sebesar 50% power serangan saat ini')
        print('# Opsi Give Up digunakan untuk pemain menyerah dari pertandingan')
        print('# Opsi Regen HP berfungsi untuk menambahkan darah sebesar 15% dari darah terbaru')
        print('# Opsi Increase Attack berfungsi untuk menambahkan Attack sebesar 10% dari Attack saat ini')

        while self.robot.life() and self.musuh.life():

            self.ronde += 1
            print(f"\nRound {self.ronde}")
            print(f'\n{self.robot.nama} vs {self.musuh.nama}')
            print(f'{self.robot.nama} HP: {self.robot.darah} -> Attack Power: {self.robot.serangan}')
            print(f'{self.musuh.nama} HP: {self.musuh.darah} -> Attack Power: {self.musuh.serangan}')

            print(f'\n1. Attack     2. Defense     3. Give Up     4. Regen HP     5. Increase Attack')
            pilihan_robot = int(input(f'{self.robot.nama}, Memilih opsi:'))
            print(f'\n1. Attack     2. Defense     3. Give Up     4. Regen HP     5. Increase Attack')
            pilihan_musuh = int(input(f'{self.musuh.nama}, Memilih opsi:'))
            print('')
            
            if pilihan_robot == 3 and pilihan_musuh == 3:
                print(f'Pertandingan seri, {self.robot.nama} dan {self.musuh.nama} Menyerah')
                break
            
            if pilihan_robot == 2 and pilihan_musuh == 2:
                print(f'Keduanya melakukan Defense')

            else:
                if pilihan_robot == 1:
                    self.robot.attack(self.musuh, pilihan_robot, pilihan_musuh)
                elif pilihan_robot == 2:
                    self.robot.defense(self.musuh, pilihan_robot, pilihan_musuh)
                elif pilihan_robot == 3:
                    print(f'{self.robot.nama} Menyerah')
                    print(f'{self.musuh.nama} Menang!!')
                    break
                elif pilihan_robot == 4:
                    self.robot.darah += (15/100) * self.robot.darah
                    print(f'{self.robot.nama} Menambah HP')
                elif pilihan_robot == 5:
                    self.robot.serangan += (10/100) *self.robot.serangan
                    print(f'{self.robot.nama} Menambah Attack Power')
                else:
                    print('Pilihan tidak valid')

                if pilihan_musuh == 1:
                    self.musuh.attack(self.robot, pilihan_robot, pilihan_musuh)
                elif pilihan_musuh == 2:
                    self.musuh.defense(self.robot, pilihan_robot, pilihan_musuh)
                elif pilihan_musuh == 3:
                    print(f'{self.musuh.nama} Menyerah')
                    print(f'{self.robot.nama} Menang!!')
                    break  
                elif pilihan_musuh == 4:
                    self.musuh.darah += (15/100) * self.musuh.darah
                    print(f'{self.musuh.nama} Menambah HP')
                elif pilihan_musuh == 5:
                    self.musuh.serangan += (10/100) * self.musuh.serangan
                    print(f'{self.musuh.nama} Menambah Attack Power')
                else:
                    print('Pilihan tidak valid')

robot = Robot('BumbleBee', 150, 40)
musuh = Robot('Megatron', 200, 20)
game = Game(robot, musuh)
game.play()
