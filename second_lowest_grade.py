if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted({s[1] for s in students})
    second_lowest_score = scores[1]

    second_lowest_students = [s[0]
                              for s in students if s[1] == second_lowest_score]
    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)