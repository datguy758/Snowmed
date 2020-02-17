import csv
import os

# Global Variables
children = dict()  # dictionary with parent as key and children as values pfc
levels = dict()
sectioning = 1045
newlist = set()
oldlist = set()


def Convert(string, rep):
    li = list(string.split(rep))
    return li


# Print list
def listtocsv(dicin, outfile):
    # For removing old csv files if existing
    try:
        os.remove(outfile)
    except:
        pass

    # Writing to pfc
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in dicin.keys():
            outline = [row]
            array = []
            for i in dicin[row]:
                array.append(i)
            outline.append(array)
            writer.writerow(outline)


# Recursion for level search
def breathFirstrec(lastgen, lev):
    lev = lev + 1
    if lev % sectioning != 0:
        try:
            for i in children[int(lastgen)]:
                if int(levels[int(i)]) < lev:
                    levels[int(i)] = lev
                    breathFirstrec(i, lev)
        except:
            pass
    else:
        newlist.add(lastgen)


def breathFirst(start):
    stack, path = [start], []
    newstack = []
    level = 0
    while stack:
        level += 1
        for i in stack:
            levels[i] = level
            newstack += children[i]
        print(level)
        stack = newstack
        newstack = []

    return path


def filtering():
    global newlist
    txtfile = "sct2_Relationship_Full_US1000124_20190901.txt"
    cfp = "parent.csv"
    pfc = "child.csv"
    leveling = "level.csv"

    parent = dict()  # dictionary with children as key and parents as values cfp

    for i in open(txtfile, "r"):  # iterate through all rows of txtfile
        con = Convert(i, "\t")
        if con[2] != "0" and con[7] == "116680003":

            # for writing to children for pfc
            if int(con[5]) in children:
                children[int(con[5])].append(int(con[4]))
            else:
                children[int(con[5])] = [int(con[4])]

            # For writing to parent for cfp
            if int(con[4]) in parent:
                parent[int(con[4])].append(int(con[5]))
            else:
                parent[int(con[4])] = [int(con[5])]
                levels[int(con[4])] = 0

    # For removing old csv files if existing
    try:
        os.remove(leveling)
    except:
        pass

    # Writing to pfc
    listtocsv(children, pfc)

    # Writing to parent
    listtocsv(parent, cfp)

    # Starts recursion search
    breathFirstrec(138875005, 0)
    count = 0
    while len(newlist) != 0:
        count +=1
        oldlist = newlist
        newlist = set()
        for i in oldlist:
            breathFirstrec(i, count*sectioning)
        print(count)
    # Writing to leveling
    level = sorted(levels.items(), key=lambda x: x[1], reverse=False)
    with open(leveling, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in level:
            writer.writerow(row)

    return levels, children, parent


if __name__ == '__main__':
    filtering()
