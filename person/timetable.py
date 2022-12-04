import json

with open('person.json', 'r') as file:
    data = json.load(file)

for group in data:
    # dictionary with teacher number and their subject
    teacherSubjects = data['teacherSubjects']
    # dictionary with teacher number and their amount of periods
    teacherPeriods = data['teacherPeriods']
    # dictionary with teacher number and their used periods
    teacherUsedPeriods = data['teacherUsedPeriods']
    # array made of six dictionaries representing which teacher a class has for a certain subject
    teachersForClass = data['teachersForClass']
    # array made of six dictionaries representing which teacher a class has for a certain period
    schedule = data['schedule']

# numOfTeachers = input("How many teachers are there? ")
# for t in range(1, int(numOfTeachers) + 1):
#     currentSubject = input("Enter the subject for Teacher " + str(t) + ": ")
#     teacherSubjects[t] = currentSubject
#
#     currentPeriods = input("Now enter the max number of periods for Teacher " + str(t) + ": ")
#     teacherPeriods[t] = int(currentPeriods)
#     teacherUsedPeriods[t] = 0

currentClass = 0
currentPeriod = 1
not_possible = False
counter = 0


def print_timetable():
    print()
    period_number = 1
    class_number = 1
    for classSchedule in schedule:
        print("Class " + str(class_number) + ": ")
        print("Periods 1-4 in order")
        for day in range(1, 6):
            print("Day " + str(day) + " | "
                  + " " + teacherSubjects[classSchedule[period_number]] + "-T" + str(classSchedule[period_number]) +
                  ", "
                  + " " + teacherSubjects[classSchedule[period_number + 1]] + "-T" + str(
                classSchedule[period_number + 1]) + ", "
                  + " " + teacherSubjects[classSchedule[period_number + 2]] + "-T" + str(
                classSchedule[period_number + 2]) + ", "
                  + " " + teacherSubjects[classSchedule[period_number + 3]] + "-T" + str(
                classSchedule[period_number + 3]))
            period_number = period_number + 4
        print()
        period_number = 1
        class_number = class_number + 1


while True:
    if not_possible:
        print("Schedule not possible")
        break

    if currentClass == 6:
        print_timetable()
        break

    for teacher in teacherSubjects:
        if currentPeriod == 21:
            currentPeriod = 1
            currentClass = currentClass + 1
        if currentClass == 6:
            break
        subject = teacherSubjects[teacher]
        amountOfPeriods = teacherPeriods[teacher]
        if len(teachersForClass) != currentClass:
            teacherDict = teachersForClass[currentClass]
        else:
            teacherDict = {}
            teachersForClass.append(teacherDict)

        if len(schedule) != currentClass:
            scheduleDict = schedule[currentClass]
        else:
            scheduleDict = {}
            schedule.append(scheduleDict)
        counter = counter + 1
        if subject not in teacherDict or teacher == teacherDict[subject]:
            if teacherUsedPeriods[teacher] < teacherPeriods[teacher]:
                breakLoop = False
                for cl in range(currentClass):
                    dict1 = schedule[cl]
                    if currentPeriod in dict1 and teacher == dict1[currentPeriod]:
                        breakLoop = True
                if breakLoop:
                    continue
                else:
                    scheduleDict[currentPeriod] = teacher
                    teacherUsedPeriods[teacher] = teacherUsedPeriods[teacher] + 1
                    if subject not in teacherDict:
                        teacherDict[subject] = teacher
                    currentPeriod = currentPeriod + 1
                    counter = 0

    if counter >= len(teacherSubjects):
        not_possible = True

# person = {"teacherSubjects": teacherSubjects, "teacherPeriods": teacherPeriods,
#           "teacherUsedPeriods": teacherUsedPeriods,
#           "teachersForClass": teachersForClass, "schedule": schedule}
#
# personJSON = json.dumps(person, indent=4, sort_keys=True)
#
# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)
