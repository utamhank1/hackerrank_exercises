def main(query_name, student_marks):
    print("%.2f" %float(sum(student_marks[query_name])/len(student_marks[name])))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    main(query_name, student_marks)
