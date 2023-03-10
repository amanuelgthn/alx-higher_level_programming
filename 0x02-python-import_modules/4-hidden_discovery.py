#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    list_data = []
    j = 0
    len_list = len(list)
    for i in range(0, len_list):
        str = list[i]
        if (str[0] != "__"):
            list_data.append(list[i])
            print(list_data[j])
            j= j + 1
