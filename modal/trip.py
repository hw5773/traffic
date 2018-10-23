import sys

def usage():
    print ("Extract intended trips")
    print ("python3 trip.py <input file> <output file>")
    exit(1)

def gu_dict():
    g = {}
    g["001"] = "종로구"
    g["002"] = "중구"
    g["003"] = "용산구"
    g["004"] = "성동구"
    g["005"] = "광진구"
    g["006"] = "동대문구"
    g["007"] = "중랑구"
    g["008"] = "성북구"
    g["009"] = "강북구"
    g["010"] = "도봉구"
    g["011"] = "노원구"
    g["012"] = "은평구"
    g["013"] = "서대문구"
    g["014"] = "마포구"
    g["015"] = "양천구"
    g["016"] = "강서구"
    g["017"] = "구로구"
    g["018"] = "금천구"
    g["019"] = "영등포구"
    g["020"] = "동작구"
    g["021"] = "관악구"
    g["022"] = "서초구"
    g["023"] = "강남구"
    g["024"] = "송파구"
    g["025"] = "강동구"

    return g

def calc_time(t1, t2):
    h1 = int(t1[0:2])
    m1 = int(t1[2:4])
    h2 = int(t2[0:2])
    m2 = int(t2[2:4])

    return (h1 * 60 + m1) - (h2 * 60 + m2)

def main():
    if len(sys.argv) != 3:
        usage()

    f = open(sys.argv[1], "r")
    g = open(sys.argv[2], "w")

    f.readline()
    s = "sheet_code, seq, start_zcode, start_name, end_zcode, end_name, time, alternative\n"
    g.write(s)

    gu = gu_dict()

    for line in f:
        tmp = line.strip().split("\t")
        scity = tmp[7].split("-")[0]
        ecity = tmp[10].split("-")[0]

        if scity != "01" or ecity != "01":
            continue

        stype = int(tmp[6])
        etype = int(tmp[9])

        if stype != 1 and stype != 2:
            continue

        if etype != 1 and etype != 2:
            continue

        sdistrict = tmp[7].split("-")[1]
        sname = gu[sdistrict]
        edistrict = tmp[10].split("-")[1]
        ename = gu[edistrict]
        s = "%s, %s, %s, %s, %s, %s, %d, %s\n" % (tmp[0], tmp[2], sdistrict, sname, edistrict, ename, calc_time(tmp[11], tmp[8]), tmp[5])
        g.write(s)

    f.close()
    g.close()

if __name__ == "__main__":
    main()
