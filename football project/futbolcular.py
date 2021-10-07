with open("Futbolcular.txt","r") as file:
    fenerbahce11 = list()
    galatasaray11 = list()
    besiktas11 = list()
    for satir in file:
        satir = satir[:-1]
        liste = satir.split(",")
        takim = liste[1]
        isim = liste[0]
        if (takim == "Fenerbahçe"):
            fenerbahce11.append(isim + "\n")
        elif (takim == "Galatasaray"):
            galatasaray11.append(isim + "\n")
        else:
            besiktas11.append(isim + "\n")

    with open("Galatasaray.txt","w",encoding= "utf-8") as file1:
        for i in galatasaray11:
            file1.write(i)
    with open("Fenerbahce.txt","w",encoding= "utf-8") as file2:
        for i in fenerbahce11:
            file2.write(i)
    with open("Besiktas.txt","w",encoding= "utf-8") as file3:
        for i in besiktas11:
            file3.write(i)
