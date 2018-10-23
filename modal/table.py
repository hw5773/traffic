import sys

def usage():
    print ("Make final table")
    print ("python3 table.py <input trip file> <household file> <member file> <output file>")
    exit(1)

def main():
    if len(sys.argv) != 5:
        usage()

    trip = open(sys.argv[1], "r")
    house = open(sys.argv[2], "r")
    member = open(sys.argv[3], "r")
    of = open(sys.argv[4], "w")
    ef = open("error.log", "w")

    s = "trip no., start zcode, end zcode, trip distance, trip cost, trip time, observed time, house rate of origin, house rate of destination, income, number of members, car, driver license, subway station, bus stop, alternatives, answer\n"
    of.write(s)

    trip.readline()

    house.readline()
    line = house.readline()
    htmp = line.strip().split("\t")
    hsheet_code = htmp[0].strip()

    member.readline()
    line = member.readline()
    mtmp = line.strip().split("\t")
    msheet_code = mtmp[0].strip()
    mseq = int(mtmp[2].strip())

    cnt = 0
    ecnt = 0
    for line in trip:
        cnt += 1
        ttmp = line.strip().split(",")
        sheet_code = ttmp[0].strip()
        seq = int(ttmp[1].strip())
        
        while (sheet_code != hsheet_code):
            hline = house.readline()
            htmp = hline.strip().split("\t")
            hsheet_code = htmp[0].strip()

        while (sheet_code != msheet_code) or (seq != mseq):
            mline = member.readline()
            mtmp = mline.strip().split("\t")
            msheet_code = mtmp[0].strip()
            mseq = int(mtmp[2].strip())

        for i in range(1, 6):
            try:
                a = int(htmp[15])
                s = "%d, %s, %s, , , , %s, , , %d, %d, %d, %d, %d, %d, %d, %d\n" % (cnt, ttmp[2], ttmp[4], ttmp[6], int(htmp[15]), int(htmp[2]), int(htmp[4]), int(mtmp[6]), int(htmp[16]), int(htmp[17]), i, int(ttmp[7]))
                of.write(s)
            except ValueError:
                ecnt += 1
                ef.write(line)

    print ("Total: %d" % (cnt))
    print ("Success: %d" % (cnt - ecnt))
    print ("Errors: %d" % (ecnt))
    trip.close()
    house.close()
    member.close()
    of.close()
    ef.close()

if __name__ == "__main__":
    main()
