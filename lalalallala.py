print("вітайемо програмі перевіркі паролю на надійність")
print("рекомендацї")
print("1.довжина пароля має складати 8 символів та більше")
print("2.в паролі має пристсвовати 5 та більше цифр")
print("3.в пароли має приствувати заглавна літера")
print("4.в паролі майть присувусти спеціальні символи")
pasvord=input("ведіть пароль:")
erors={
    1:"недостатня довжина паролю",
    2:"немає великої літери",
    3:"недостатно літер",
    4:"немає цифер",
    5:"недостатня цифер",
    6:"немає спец символів"
}
if len(pasvord)>8:
    del erors[1]
if pasvord.lower()!=pasvord:
    del erors[2]
if pasvord.upper!=pasvord:
    del erors[3]
if '*' in pasvord or '#' in pasvord or '%' in pasvord:
    del erors[6]

cauntnamber=0
for x in  pasvord:
    if x .isdigit():
        cauntnamber+=1
    if cauntnamber==5:
        del erors[4]
        del erors[5]
        break
if len(erors)==0:
    print("пароль бомба")
else:
    print("пароль не надійний")
    for x in erors.values():
        print(x)