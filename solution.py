def main():
    files = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
    for file in files:
        data = open(file, 'r')
        line = data.readline()
        M = int(line.split(" ")[0])
        typesS = data.readline().split(" ")
        types = []
        for i in typesS:
            types.append(int(i))


        sol(M, types)


def sol(M, types):
    

if __name__ == '__main__':
    main()