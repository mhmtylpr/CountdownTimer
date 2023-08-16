import time

while True:
    try :
        sayac = input("Geri sayılacak süreyi yazınız: ")
        sayac = int(sayac)
        break
    except:
        print("lütfen sayı giriniz.")
while sayac >0:
    print(f"Son {sayac} saniye kaldı.")
    time.sleep(1)
    sayac -= 1

print("Süre doldu")