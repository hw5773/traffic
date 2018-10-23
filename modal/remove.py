import sys

def usage():
    print ("Remove exceptions")
    print ("python3 remove.py <input file> <output fie>")
    exit(1)

def main():
    if len(sys.argv) != 3:
        usage()

    f = open(sys.argv[1], "r")
    g = open(sys.argv[2], "w")

    lst = [1, 2, 4, 10, 13]
    line = f.readline()
    g.write(line)

    for line in f:
        alt = int(line.strip().split(",")[-1])
        if alt in lst:
            g.write(line)

    f.close()
    g.close()

if __name__ == "__main__":
    main()
