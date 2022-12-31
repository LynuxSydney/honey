#fname = input("Enter file name: ")
raw_file = "C:\pwsh.txt"
id = []
f = open("C:\id_lsass.txt",'w')
f.close()
with open(raw_file, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    data = letter
                    f = open("C:\id_lsass.txt",'a')
                    f.write(data)
