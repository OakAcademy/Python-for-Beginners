with open ("Chelsea.txt", "r") as Chelsea:
    GK = list()
    Defence = list()
    Midfield = list()
    Forward = list()

    for row in Chelsea:
        row = row[:-1]
        row_Elements = row.split(",")

        if row_Elements[1] == "GK":
            GK.append(row + "\n")
        elif row_Elements[1] == "Defence":
            Defence.append(row + "\n")
        elif row_Elements[1] == "Midfield":
            Midfield.append(row + "\n")
        else:
            Forward.append(row + "\n")

        with open("GK.txt", "w") as GK_F:
            for i in GK:
                GK_F.write(i)

        with open("Defence.txt", "w") as Defence_F:
            for i in Defence:
                Defence_F.write(i)

        with open("Midfield.txt", "w") as Midfield_F:
            for i in Midfield:
                Midfield_F.write(i)

        with open("Forward.txt", "w") as Forward_F:
            for i in Forward:
                Forward_F.write(i)

