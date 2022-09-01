
import zipfile


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


bannr = """"
[[red]]    ____             __ [[green]] _____   _     [[white]]
[[red]]   / __ \____  _____/ /_[[green]]/__  /  (_)___ [[white]]
[[red]]  / /_/ / __ \/ ___/ //_/[[green]] / /  / / __ \[[white]]
[[red]] / _, _/ /_/ / /__/ ,<  [[green]] / /__/ / /_/ /[[white]]
[[red]]/_/ |_|\____/\___/_/|_| [[green]]/____/_/ .___/ [[white]]
[[red]]                             [[green]] /_/      [[white]]

"""
banner = colorText(bannr)


fail = "[[red]]Failed[[white]]"
failed = colorText(fail)

succes = "[[green]][+] Password found:[[white]]"
succsesfull = colorText(succes)


oki = "[[white]] => [[white]]"
ok = colorText(oki)

print(banner)
 
zip_file = input("Your zip file : ")
x = input("Wanna use our wordlist? Y/n: ")




#1

def crack_password1(password_list, obj):
    # tracking line no. at which password is found
    idx = 0
 
    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print(succsesfull+ ok+word.decode())
                    return True
                except:
                    continue
    return False
 
password_list = "wordlist.txt"
 
# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)
 
# count of number of words present in file


#2

def crack_password2(password_list, obj):
    # tracking line no. at which password is found
    idx = 0
 
    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print(succsesfull+ ok+word.decode())
                    return True
                except:
                    continue
    return False
 


# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)
 





if x == "y":
	password_list1 = "wordlist.txt"
	cnt = len(list(open(password_list, "rb")))
 
	print("There are total", cnt,
      "number of passwords to test")
 

	if crack_password1(password_list1 , obj) == False:
   	 	print("Password not found in this file")
 
elif x == "n":
	z = input("Your worlist url: ")
	password_list = z
	cnt = len(list(open(password_list, "rb")))

	print("There are total", cnt,
      "number of passwords to test")
 
	if crack_password2(password_list , obj) == False:
   	 	print("Password not found in this file")

else:
	password_list1 = "wordlist.txt"
	cnt = len(list(open(password_list1, "rb")))

	print("There are total", cnt,
      "number of passwords to test")
 
	if crack_password1(password_list1 , obj) == False:
   	 	print("Password not found in this file")
 




















