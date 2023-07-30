def swap_case(s):
    s_list = [*s]
    for i in range(0, len(s_list)):
        # If character is uppercase.
        if s_list[i] == s_list[i].upper():
            s_list[i] = s_list[i].lower()
        # Check if character is lowercase.
        elif s_list[i] == s_list[i].lower():
            s_list[i] = s_list[i].upper()
        else:
            pass
        
    return "".join(s_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)