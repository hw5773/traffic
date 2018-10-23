import sys

def usage():
    print ("Count frequency per alternative")
    print ("python3 count.py <input file> <output file>")
    exit(1)

def alternatives():
    a = {}
    a[1] = "도보"
    a[2] = "승용차 직접"
    a[3] = "승용차 다른 사람"
    a[4] = "시내 버스"
    a[5] = "시외 버스"
    a[6] = "마을 버스"
    a[7] = "광역 버스"
    a[8] = "고속 버스"
    a[9] = "기타 버스"
    a[10] = "지하철"
    a[11] = "일반 철도"
    a[12] = "고속 철도"
    a[13] = "택시"
    a[14] = "소형 화물차"
    a[15] = "중대형 화물차"
    a[16] = "오토바이"
    a[17] = "자전거"
    a[18] = "기타(항공, 선박 등)"

    return a

def main():
    if len(sys.argv) != 3:
        usage()

    f = open(sys.argv[1], "r")
    g = open(sys.argv[2], "w")

    a = alternatives()
    freq = {}
    for i in range(1, 19):
        freq[i] = 0

    cnt = 0
    f.readline()
    for line in f:
        cnt += 1
        alt = int(line.strip().split(",")[-1])
        freq[alt] += 1

    s = "번호, 수단, 개수, 비율\n"
    g.write(s)

    for i in range(1, 19):
        s = "%d, %s, %d, %f\n" % (i, a[i], freq[i], float(freq[i]) / cnt)
        print (s)
        g.write(s)

    f.close()
    g.close()

if __name__ == "__main__":
    main()
