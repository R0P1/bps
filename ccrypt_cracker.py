import ccrypt

fc = input("Masukkan nama file ccrypt: ")
fw = input("Masukkan nama file wordlist: ")

with open(fw, 'r') as w:
    for baris in w:
        kata_sandi = baris.strip()  
      
        try:
            ccrypt.decrypt(fc, kata_sandi)
            print(f"Kata sandi ditemukan: {kata_sandi}")
            break

        except ccrypt.CCryptError:
            continue

    else:
        print("Kata sandi tidak ditemukan dalam file wordlist.")
