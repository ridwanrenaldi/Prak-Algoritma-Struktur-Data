#Author     : Ridwan Renaldi
#Kelas/ NIM : B / L200160026
#Python 3.6

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self, data):
        self.items.append(data)


def DesimalToBiner():
    print ("\n===[Mengubah Desimal ke Biner]===")
    desimal = int(input("[] Masukan angka desimal : "))
    des = desimal
    
    f = Stack()
    if desimal == 0:
        f.push(0)
        
    while desimal != 0:
        sisa = desimal%2
        desimal = desimal//2
        f.push(sisa)
        
    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
    print ("[] "+str(des)+" Desimal = "+str(st)+" Biner")
    print ("=================================\n\n")


def BinerToDesimal():
    print ("\n===[Mengubah Biner ke Desimal]===")
    biner = input("[] Masukan angka biner : ")
    
    stack = Stack()
    for x in biner:
        stack.push(x)

    nilai = 0
    for i in range(len(stack)):
        if stack.pop() == '1':
            nilai += 2**int(i)
    print ("[] "+str(biner)+" Biner = "+str(nilai)+" Desimal")
    print ("=================================\n\n")



def DesimalToHexa():
    print ("\n===[Mengubah Desimal ke Hexa]===")
    desimal = int(input("[] Masukan angka desimal : "))
    des = desimal
    
    f = Stack()
    if desimal == 0:
        f.push(0)
    while desimal != 0:
        sisa = desimal%16
        if sisa == 10:
            f.push('A')
            desimal = desimal//16
        elif sisa == 11:
            f.push('B')
            desimal = desimal//16
        elif sisa == 12:
            f.push('C')
            desimal = desimal//16
        elif sisa == 13:
            f.push('D')
            desimal = desimal//16
        elif sisa == 14:
            f.push('E')
            desimal = desimal//16
        elif sisa == 15:
            f.push('F')
            desimal = desimal//16
        else:
            f.push(sisa)
            desimal = desimal//16

    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
        
    print ("[] "+str(des)+" Desimal = "+str(st)+" Hexa")
    print ("=================================\n\n")



def HexaToDesimal():
    print ("\n===[Mengubah Hexa ke Desimal]===")
    hexa = input("[] Masukan angka hexa : ")
    
    stack = Stack()
    for i in range(1, len(hexa)+1):
        stack.push(hexa[-i].upper())

    hasil = 0
    for i in range(len(stack)):
        if stack.items[i] == 'A':
            hasil += 10*(16**i)

        elif stack.items[i] == 'B':
            hasil += 11*(16**i)

        elif stack.items[i] == 'C':
            hasil += 12*(16**i)

        elif stack.items[i] == 'D':
            hasil += 13*(16**i)

        elif stack.items[i] == 'E':
            hasil += 14*(16**i)

        elif stack.items[i] == 'F':
            hasil += 15*(16**i)

        else:
            hasil += int(stack.items[i])*(16**i)
            
    print ("[] "+str(hexa)+" Hexa = "+str(hasil)+" Desimal")
    print ("=================================\n\n")


tampilan = "[]=====[CONVERT ANGKA]=====[]\
            \n 1. Desimal To Biner\
            \n 2. Biner To Desimal\
            \n 3. Desimal To Hexa\
            \n 4. Hexa To Desimal\
            \n\
            \n 0. Exit\
            \n[]=========================[]\n"

while True:
    print (tampilan)
    pilihan = input("Masukkan Pilihan Anda : ")

    if pilihan == '1':
        DesimalToBiner()
        
    elif pilihan == '2':
        BinerToDesimal()
        
    elif pilihan == '3':
        DesimalToHexa()
        
    elif pilihan == '4':
        HexaToDesimal()
        
    elif pilihan == '0':
        print ("Good Bye :)")
        break
    else:
        print ("Pilihan anda tidak terdapat dalam daftar!")








    
