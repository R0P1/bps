import ccrypt

cf = input("Enter the ccrypt file name : ")
wf = input("Enter the wordlist file name: ")

with open(wf, 'r') as w:
    for line in w:
        password = line.strip()  
      
        try:
            ccrypt.decrypt(cf, password)
            print(f"Password found: {password}")
            break

        except ccrypt.CCryptError:
            continue

    else:
        print("Password not found in wordlist file.")
