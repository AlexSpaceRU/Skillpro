print("o-x-o-x-o-x-o-x-o-x-o- крестики нолики -o-x-o-x-o-x-o-x-o-x-o")
line = "  1 2 3"
p1 = [1, "-", "-", "-"]
p2 = [2, "-", "-", "-"]
p3 = [3, "-", "-", "-"]
list_1 = [p1, p2, p3]

def change_win():
    if p1[1] == p1[2] == p1[3] != "-" or p2[1] == p2[2] == p2[3] != "-" or p3[1] == p3[2] == p3[3] != "-" or p1[1] == p2[1] == p3[1] != "-" or p1[2] == p2[2] == p3[2] != "-" or p1[3] == p2[3] == p3[3] != "-" or p1[1] == p2[2] == p3[3] != "-" or p1[3] == p2[2] == p3[1] != "-":
        return True

def select():
    s = input("Введите (1) если хотите играть крестиками,  (2) если ноликами: ")
    g = ""
    if s == "1":
        g = "x"
        print("Вы выбрали крестики ( x )")
        return g
    elif s == "2":
        g = "o"
        print("Вы выбрали нолики ( o )")
        return g
    else:
        print("Ошибка ввода, повторите...")
        select()

a = select()
if a == "x":
    b = "o"
else:
    b, a = "x", "o"
print("GO ! " * 3)

def ii():
    while True:
        con = 0
        if p1[1] == p1[2] != "-":
            if p1[3] == "-":
                p1[3] = b
                con += 1
                break
        if p1[2] == p1[3] != "-":
            if p1[1] == "-":
                p1[1] = b
                con += 1
                break
        if p1[1] == p1[3] != "-":
            if p1[2] == "-":
                p1[2] = b
                con += 1
                break
        if p2[1] == p2[2] != "-":
            if p2[3] == "-":
                p2[3] = b
                con += 1
                break
        if p2[2] == p2[3] != "-":
            if p2[1] == "-":
                p2[1] = b
                con += 1
                break
        if p2[1] == p2[3] != "-":
            if p2[2] == "-":
                p2[2] = b
                con += 1
                break
        if p3[1] == p3[2] != "-":
            if p3[3] == "-":
                p3[3] = b
                con += 1
                break
        if p3[2] == p3[3] != "-":
            if p3[1] == "-":
                p3[1] = b
                con += 1
                break
        if p3[1] == p3[3] != "-":
            if p3[2] == "-":
                p3[2] = b
                con += 1
                break
        if p1[1] == p2[1] != "-":
            if p3[1] == "-":
                p3[1] = b
                con += 1
                break
        if p2[1] == p3[1] != "-":
            if p1[1] == "-":
                p1[1] = b
                con += 1
                break
        if p1[1] == p3[1] != "-":
            if p2[1] == "-":
                p2[1] = b
                con += 1
                break
        if p1[2] == p2[2] != "-":
            if p3[2] == "-":
                p3[2] = b
                con += 1
                break
        if p2[2] == p3[2] != "-":
            if p1[2] == "-":
                p1[2] = b
                con += 1
                break
        if p1[2] == p3[2] != "-":
            if p2[2] == "-":
                p2[2] = b
                con += 1
                break
        if p1[3] == p2[3] != "-":
            if p3[3] == "-":
                p3[3] = b
                con += 1
                break
        if p2[3] == p3[3] != "-":
            if p1[3] == "-":
                p1[3] = b
                con += 1
                break
        if p1[3] == p3[3] != "-":
            if p2[3] == "-":
                p2[3] = b
                con += 1
                break
        if p1[1] == p2[2] != "-":
            if p3[3] == "-":
                p3[3] = b
                con += 1
                break
        if p2[2] == p3[3] != "-":
            if p1[1] == "-":
                p1[1] = b
                con += 1
                break
        if p1[1] == p3[3] != "-":
            if p2[2] == "-":
                p2[2] = b
                con += 1
                break
        if p1[3] == p2[2] != "-":
            if p3[1] == "-":
                p3[1] = b
                con += 1
                break
        if p2[2] == p3[1] != "-":
            if p1[3] == "-":
                p1[3] = b
                con += 1
                break
        if p1[3] == p3[1] != "-":
            if p2[2] == "-":
                p2[2] = b
                con += 1
                break

        for u in list_1:
            for h, f in enumerate(u):
                if f == "-":
                    u[h] = b
                    con += 1
                    break
            if con != 0:
                break
        break

def field():
    print(line)
    print(*p1)
    print(*p2)
    print(*p3)

def hod():
    result = change_win()
    if result:
        print("You're win ")
        return False
    else:
        comp = input("нажмите любую клавишу для хода ПК... ")
        ii()
        field()
        if result:
            print("computer win")
            return True
        else:
            return False

field()

if a == "o":
    print("Сначала ходят крестики, вы - нолики.. и потому...")
    w = input("нажмите любую клавишу для хода ПК: " )
    p2[2] = "x"
    field()

def change_s():
    ch_str = input("Введите строку(1-3): ")
    if ch_str != "1" and ch_str != "2" and ch_str != "3":
        print("Ошибка ввода, повторите...")
        return change_s()
    else:
        return int(ch_str)

def change_c():
    ch_col = input("Введите столбец(1-3): ")
    if ch_col != "1" and ch_col != "2" and ch_col != "3":
        print("Ошибка ввода, повторите...")
        return change_c()
    else:
        return int(ch_col)

def youare():
    change_str = int(change_s())
    change_col = int(change_c())
    for i in list_1:
        if change_str in i:
            if i[change_col] != "-":
                print("занято")
                youare()
            else:
                i[change_col] = a

while "-" in p1 or "-" in p2 or "-" in p3:

    result2 = change_win()
    if result2:
        print("STOP ИГРА!!!")
        break
    print("Ваш ход...")
    youare()
    field()
    hod()

if "-" not in p1 and "-" not in p2 and "-" not in p3:
    print("ничья")
