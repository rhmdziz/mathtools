import math
def kalkulator():
    def jumlah():
        print('Penjumlahan')
        a = int(input())
        b = int(input())
        print(a+b)
    def kurang():
        print('Pengurangan')
        a = int(input())
        b = int(input())
        print(a-b)
    def kali():
        print('Perkalian')
        a = int(input())
        b = int(input())
        print(a*b)
    def bagi():
        print('Pembagian')
        a = int(input())
        b = int(input())
        print(a/b)
    def pangkat():
        print('Perpangkatan')
        a = int(input())
        b = int(input())
        print(a**b)
    def akar2():
        print('Pengakar2an')
        a = int(input())
        a = math.sqrt(a)
        print(a)
    def modulo():
        print('Pencarian sisa bagi')
        a = int(input())
        b = int(input())
        print(a%b)
    print('Pilih operasi')
    print('1. Jumlah       (+)\n2. Kurang       (-)\n3. Kali         (*)\n4. Bagi         (/)\n5. Pangkat      (**)\n6. Akar kuadrat (sqrt)\n7. Modulo       (%)')
    ops=int(input('1/2/3/4/5/6/7: '))
    if ops == 1:
        jumlah()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            jumlah()
        else:
            kalkulator()
    elif ops == 2:
        kurang()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            kurang()
        else:
            kalkulator()
    elif ops == 3:
        kali()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            kali()
        else:
            kalkulator()
    elif ops == 4:
        bagi()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            bagi()
        else:
            kalkulator()
    elif ops == 5:
        pangkat()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            pangkat()
        else:
            kalkulator()
    elif ops == 6:
        akar2()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            akar()
        else:
            kalkulator()
    elif ops == 7:
        modulo()
        loop = input('lagi? y/n: ')
        if loop == 'y' or loop == 'Y':
            modulo()
        else:
            kalkulator()
    else:
       kalkulator()
kalkulator()
