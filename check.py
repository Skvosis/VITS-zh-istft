from text.symbols import symbols

files = ["F:/Dev/MB-iSTFT-VITS-main/filelists/miki_train.txt.cleaned",
         "F:/Dev/MB-iSTFT-VITS-main/filelists/miki_test.txt.cleaned",]

symbols += '\n'

for file in files:

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    f.close()

    '''with open(file, 'w', encoding='utf-8') as f:
        for line in lines :
            write_p = True
            for word in line[14:]:
                if word not in symbols:
                    write_p = False
                    
            if write_p == True:
                f.write(line)
    f.close()'''

    with open(file, 'r', encoding='utf-8') as f:
        for line in lines :
            write_p = True
            for word in line[14:]:
                if word not in symbols:
                    write_p = False
                    print(word)
                    
                    
            if write_p == False:
                print(line)
    f.close()