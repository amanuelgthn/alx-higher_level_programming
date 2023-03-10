#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    list_data = []
    len_list = len(list)
    for i in range(0, len_list):
        if ((list[i])[0] != "__"):
            list_data.append(list[i])
    list_data.sort()
    n = len(list_data)
    for i in range(0, n):
        print("{}.format(list_data[i]))
