
def read_data():
    list =[]
    with open("1111.txt","r") as f:
        for a in f.readlines():
            b = a[1:-2]
            list.append(b)
    return list


if __name__ == '__main__':
    print(read_data())