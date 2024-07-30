import datetime
gozine = int(input("1_ vard kardan saat be sort destiny va 2_ be sort kodkhar"))

time = int(input("slam Sara saat chande"))
while(time not in range(0,25)):
    print("Sara lotfan adadi bain 0 ta 24 vard kon")
    time=input("slam Sara saat chande")

if time<6 and time> 0:
    print("nime shab bekheyr!")

elif time< 12 and time> 6:
    print("sobh bekheyr!")

elif time< 18 and time> 12:
    print("badazohr bekheyr!")

elif time< 24 and time> 18:
    print("shab bekheyr!")