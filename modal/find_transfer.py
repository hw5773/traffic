import sys

tr_seq = 3
end_type = 9

def usage():
    print ("Find the records with end_type == 4")
    print ("python3 find_transfer.py <input file> <transfer records>")
    exit(1)

def main():
    if len(sys.argv) != 3:
        usage()

    f = open(sys.argv[1], "r")
    g = open(sys.argv[2], "w")

    f.readline()
    for line in f:
        tmp = line.split("\t")
        if int(tmp[end_type]) == 4:
            print ("%s: %s" % (tmp[tr_seq], tmp[end_type]))
            g.write(line)

    f.close()
    g.close()

if __name__ == "__main__":
    main()
