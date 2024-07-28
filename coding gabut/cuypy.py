import random

nama = "GAME TEBAK TIKUS"
niali_masuk = random.randint(1, 5)

print("=============================")
print(f"***** {nama} ******")
print("=============================")

nama_user = input("nama kamu: ")
print(f''' 
      selamat datang dan besenanglah untuk memenangkan game tebak tikus goa ini {nama_user}
      coba perhatikan goa goa di bawah ini dan tebaklah untuk menang:
      
      |_| |_| |_| |_| |_|
      ''')

pilihan_user = int(input("pililah lobang mana yang benar emang tukus itu berada? [1 / 2 / 3 / 4 / 5 /]: "))

if pilihan_user == niali_masuk:
    print(f"selamat jawaban anda benar dan menang {nama_user} dan tikus itu berada di goa {niali_masuk} dan kamu memilih jawaban yang benar yaitu di lobang {pilihan_user}")
else:
    print("yaahhhh... anda kalah sayang sekali...")


