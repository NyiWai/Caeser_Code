def Caesar_En():
    String = ""
    space = ord(" ")
    Str = input("Enter letter to encrypt : ").lower()
    for I in Str:
        if I == "a":
            a = 0
            a = str(a + 3)
            String += (a + " ")
        elif I == "b":
            b = 1
            b = str(1 + 3)
            String += (b + " ")
        elif I == "c":
            c = 2
            c = str(c + 3)
            String += (c + " ")
        elif I == "d":
            d = 3
            d = str(d + 3)
            String += (d + " ")
        elif I == "e":
            e = 4
            e = str(e + 3)
            String += (e + " ")
        elif I == "f":
            f = 5
            f = str(f + 3)
            String += (f + " ")
        elif I == "g":
            g = 6
            g = str(g + 3)
            String += (g + " ")
        elif I == "h":
            h = 7
            h = str(h + 3)
            String += (h + " ")
        elif I == "i":
            i = 8
            i = str(i+ 3)
            String += (i + " ")
        elif I == "j":
            j = 9
            j= str(j + 3)
            String += (j + " ")
        elif I == "k":
            k = 10
            k = str(k + 3)
            String += (k + " ")
        elif I == "l":
            l = 11
            l = str(l + 3)
            String += (l + " ")
        elif I == "m":
            m = 12
            m = str(m + 3)
            String += (m + " ")
        elif I == "n":
            n = 13
            n = str(n + 3)
            String += (n + " ")
        elif I == "o":
            o = 14
            o = str(o + 3)
            String += (o + " ")
        elif I == "p":
            p = 15
            p = str(p + 3)
            String += (p + " ")
        elif I == "q":
            q = 16
            q = str(q + 3)
            String += (q + " ")
        elif I == "r":
            r = 17
            r = str(r + 3)
            String += (r + " ")
        elif I == "s":
            s = 18
            s = str(s + 3)
            String += (s + " ")
        elif I == "t":
            t = 19
            t = str(t + 3)
            String += (t + " ")
        elif I == "u":
            u = 20
            u = str(u + 3)
            String += (u + " ")
        elif I == "v":
            v = 21
            v = str(v + 3)
            String += (v + " ")
        elif I == "w":
            w = 22
            w = str(w + 3)
            String += (w + " ")
        elif I == "x":
            x = 23
            x = str(x + 3)
            String += (x + " ")
        elif I == "y":
            y = 24
            y = str(y + 3)
            String += (y + " ")
        elif I == "z":
            z = 25
            z = str(z + 3)
            String += (z + " ")
        elif I == 32:
            String += " "
    print(String)

def Caesar_De():
    String = ""
    Str = str(input("Enter letter to Decrypt : ")).lower()
    Str = Str.split(" ")
    for I in Str:
        if I == " ":
            I = "1"
        I = int(I)
        Af_Sub = I - 3
        if Af_Sub == 0:
            a = 'a'
            String += (a + " ")
        elif Af_Sub == 1:
            b = 'b'
            String += (b + " ")
        elif Af_Sub == 2:
            c = 'c'
            String += (c + " ")
        elif Af_Sub == 3:
            d = 'd'
            String += (d + " ")
        elif Af_Sub == 4:
            e = 'e'
            String += (e + " ")
        elif Af_Sub == 5:
            f = 'f'
            String += (f + " ")
        elif Af_Sub == 6:
            g = 'g'
            String += (g + " ")
        elif Af_Sub == 7:
            h = 'h'
            String += (h + " ")
        elif Af_Sub == 8:
            i = 'i'
            String += (i + " ")
        elif Af_Sub == 9:
            j = 'j'
            String += (j + " ")
        elif Af_Sub == 10:
            k = 'k'
            String += (k + " ")
        elif Af_Sub == 11:
            l = 'l'
            String += (l + " ")
        elif Af_Sub == 12:
            m = 'm'
            String += (m + " ")
        elif Af_Sub == 13:
            n = 'n'
            String += (n + " ")
        elif Af_Sub == 14:
            o = 'o'
            String += (o + " ")
        elif Af_Sub == 15:
            p = 'p'
            String += (p + " ")
        elif Af_Sub == 16:
            q = 'q'
            String += (q + " ")
        elif Af_Sub == 17:
            r = 'r'
            String += (r + " ")
        elif Af_Sub == 18:
            s = 's'
            String += (s + " ")
        elif Af_Sub == 19:
            t = 't'
            String += (t + " ")
        elif Af_Sub == 20:
            u = 'u'
            String += (u + " ")
        elif Af_Sub == 21:
            v = 'v'
            String += (v + " ")
        elif Af_Sub == 22:
            w = 'w'
            String += (w + " ")
        elif Af_Sub == 23:
            x = 'x'
            String += (x + " ")
        elif Af_Sub == 24:
            y = 'y'
            String += (y + " ")
        elif Af_Sub == 25:
            z = 'z'
            String += (z + " ")
    print(String)

if __name__ == "__main__":
    while True:
        Choice = input("Enter 1 for encrypt\n      2 for decrypt - ")
        if Choice == "1":
            Caesar_En()
        elif Choice == "2":
            Caesar_De()
        else:
            print("Valid are 1/2!!!")
