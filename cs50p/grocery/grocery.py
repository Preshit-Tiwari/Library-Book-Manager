def main():
    g_list = {}

    while(True):
        try:
            item = input()
            key = item.upper()
            if key not in g_list:
                g_list[key] = 1
            else:
                g_list[key] += 1
        except EOFError:
            break
    g_list = dict(sorted(g_list.items()))
    print()
    for i in g_list:
        print(g_list[i], i)
main()
