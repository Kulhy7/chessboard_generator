# ==============================================
#  Program: Chessboard
#  Author: Luboš Kulhan | alias: Adam Kaiser
#  Description: Program for generating a chessboard
# ==============================================
import os
def sachovnice(a,b,c,z):
    a = int(a)
    b = int(b)
    c = int(c)
    z = int(z)   # number of squares in an odd row
    sudz = int(z-1)  # number of squares in an even row
    q = 1
    while q <= c:
        q += 1
        i = 0
        y = 1
        x = 1
        p = 1
        while i < b:   # one row of squares - 3

            while x <= z:   # one line
                while y <= a:
                    print("[|]", end = '')
                    y += 1
                while p <= a:
                    print("   ", end = '')
                    p += 1
                x += 1
                y = 1
                p = 1

            print()
            i += 1
            y = 1
            x = 1
            p = 1

        i = 0
        y = 1
        x = 1
        p = 1

        while i < b:   # one row of squares - 2

            while x <= sudz:   # one line
                while p <= a:
                    print("   ", end = '')
                    p += 1
                while y <= a:
                    print("[|]", end = '')
                    y += 1
                x += 1
                y = 1
                p = 1

            print()
            i += 1
            y = 1
            x = 1
            p = 1

while True:
    try:
        os.system('clear')
        print("Welcome to the chessboard generator (hold Enter to exit)\n")
        sirka = input("Enter the width of the rectangle: ")
        vyska = input("Enter the height of the rectangle: ")
        delka = input("Enter the length of the chessboard: ")
        radek = input("Enter the number of rows (rows = rows * 2): ")

        print("Here is the chessboard:\n")
        sachovnice(sirka,vyska,radek,delka)
        input("\nPress any key to restart...")
        os.system('clear')
    except:
        os.system('clear')
        exit()
