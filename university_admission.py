dept_exams = {'Biotech': [2, 3], 'Chemistry': [3],
              'Engineering': [4, 5], 'Mathematics': [4], 'Physics': [2, 4]}

def reading_aplicants():
    applicants_file = open('applicants.txt', 'r')
    # the empty element will hold the score average
    aplicants = [(aplicant.split() + ['']) for aplicant in applicants_file]
    applicants_file.close()
    return aplicants

# write each department members into file
def write_file(dept, dept_members):
    dept_file = open(f'{dept}.txt', 'w', encoding='utf-8')
    dept_members = [f"{member[0]} {member[1]} {member[-1]}\n"
                    for member in dept_members]
    dept_file.writelines(dept_members)


#  setting the best score in the last element
def best_score(aplicant):
    if int(aplicant[6]) > aplicant[-1]:
        aplicant[-1] = int(aplicant[6]) / 1  # divide to get float return


# calculate max score and assign it to the last empty element
def best_score(aplicant, i):
    exams_indexs = dept_exams[aplicant[i]]
    scores = [int(aplicant[i]) for i in exams_indexs]
    scores_avg = sum(scores) / len(scores)
    aplicant[-1] = max(scores_avg, int(aplicant[6]))
    return aplicant[-1]




# sort aplicants by priority , score average and name
def sort_apps(apps, i):
    apps.sort(key=lambda x: (x[i], -best_score(x, i), x[0], x[1]))


def dept_ability(dept, n):  # chick if department has empty place
    return len(dept_members[dept]) < n


# adding member department
def add_aplicant(dept_members, aplicant, aplicants, i):
    dept_members[aplicant[i]].append(aplicant)
    aplicants.remove(aplicant)


# match members to convenient department
def accept_aplicant(dept_members, aplicants, aplicant, n, i):
    if dept_ability(aplicant[i], n):
        add_aplicant(dept_members, aplicant, aplicants, i)


acciptance_number = int(input())  # numbers of members in each department

aplicants = reading_aplicants()
dept_members = {'Biotech': [], 'Chemistry': [],
                'Engineering': [], 'Mathematics': [], 'Physics': []}
for i in range(7, 10):
    sort_apps(aplicants, i)
    for aplicant in aplicants[:]:
        accept_aplicant(dept_members, aplicants, aplicant, acciptance_number, i)
for dept, members in dept_members.items():
    dept_exam_index = dept_exams[dept]
    dept_members[dept].sort(
        key=lambda x: (-x[-1], x[0], x[1]))
    write_file(dept, members)
