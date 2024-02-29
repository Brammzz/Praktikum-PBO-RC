key = int(input("Key : "))
Grade = {}
for i in range(key):
  name = input("Name " + str(i+1) + " : ")
  grade = int(input("Grade " + str(i+1) + " : "))
  Grade.update({name:grade})
print("Grade : " + str(Grade))
