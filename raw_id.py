#Created by @bericontraster
raw_file = "C:\Windows\System32\lsass.txt"
id = []
f = open("C:\Windows\System32\id_lsass.txt",'w')
f.close()
with open(raw_file, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    data = letter
                    f = open("C:\Windows\System32\id_lsass.txt",'a')
                    f.write(data)
#END
