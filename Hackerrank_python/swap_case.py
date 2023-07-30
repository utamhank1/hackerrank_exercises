def swap_case(s):
    s_list = [*s]
    s_out = [x.upper() if x == x.lower() else x.lower() for x in s_list]
        
    return "".join(s_out)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)