import math
def kalkulator():
    def jumlah():
        print('Penjumlahan')
        a = int(input())
        b = int(input())
        print(a+b)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            jumlah()
        else:
            kalkulator()
    def kurang():
        print('Pengurangan')
        a = int(input())
        b = int(input())
        print(a-b)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            kurang()
        else:
            kalkulator()
    def kali():
        print('Perkalian')
        a = int(input())
        b = int(input())
        print(a*b)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            kali()
        else:
            kalkulator()
    def bagi():
        print('Pembagian')
        a = int(input())
        b = int(input())
        print(a/b)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            bagi()
        else:
            kalkulator()
    def pangkat():
        print('Perpangkatan')
        a = int(input())
        b = int(input())
        print(a**b)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            pangkat()
        else:
            kalkulator()
    def akar2():
        print('Pengakar2an')
        a = int(input())
        a = math.sqrt(a)
        print(a)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            akar()
        else:
            kalkulator()
    def modulo():
        print('Pencarian sisa bagi')
        a = int(input())
        b = int(input())
        print(a%b)
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            modulo()
        else:
            kalkulator()
    print('Pilih operasi')
    print('1. Jumlah       (+)\n2. Kurang       (-)\n3. Kali         (*)\n4. Bagi         (/)\n5. Pangkat      (**)\n6. Akar kuadrat (sqrt)\n7. Modulo       (%)')
    ops=int(input('1/2/3/4/5/6/7: '))
    if ops == 1:
        jumlah()
    elif ops == 2:
        kurang()
    elif ops == 3:
        kali()
    elif ops == 4:
        bagi()  
    elif ops == 5:
        pangkat() 
    elif ops == 6:
        akar2()
    elif ops == 7:
        modulo()   
    else:
       kalkulator()
kalkulator()
