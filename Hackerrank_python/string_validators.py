def main(s):
    boolean_list = [False] * 5
    test_list = [[] * 5] 
    test_list = [[x.isalnum() for x in [*s]],
                [x.isalpha() for x in [*s]],
                [x.isdigit() for x in [*s]],
                [x.islower() for x in [*s]],
                [x.isupper() for x in [*s]] 
                ]
    boolean_list = [any(x) for x in test_list]
    for elem in boolean_list:
       print (elem)
        
if __name__ == '__main__':
    s = input()
    main(s)
