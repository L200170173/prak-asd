def kabisat(x):
    if (x % 4) == 0:
        if (x % 100) == 0:
            if (x % 400) == 0:
                print ("Tahun Kabisat")
            else:
                print ("Bukan Tahun Kabisat")
        else:
            print ("Tahun Kabisat")
    else:
        print ("Bukan Tahun Kabisat")

kabisat(2019)
