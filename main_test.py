import random
import main


def test_makeList():
    students = main.makeList()

    lenofdict = len(students)
    lenofkeys = len(students[0].keys())
    main.printList(students)

    assert lenofdict == 5, "Invalid value. Expected 5"
    assert lenofkeys == 3, "Invalude number of keys. Expecting 3"
    assert int(
        students[0]['ID']) == 1001, "Invalid id of the fist student. Expecting 1001"
    assert int(
        students[1]['ID']) == 1002, "Invalid id of the fist student. Expecting 1002"
    assert int(
        students[2]['ID']) == 1003, "Invalid id of the fist student. Expecting 1003"
    assert int(
        students[3]['ID']) == 1004, "Invalid id of the fist student. Expecting 1004"

    lenofscores = len(students[4]['Scores'])
    assert lenofscores == 4, "Expecting 4"


def test_scorebySubject():
    students = main.makeList()

    lenofstudents = len(students)
    assert lenofstudents == 5, "Expecting 5"

    slist = main.scoresbySubject(students)
    lenofslist = len(slist)
    keyval = list(slist.keys())
    print('Your keys: ', keyval)
    assert lenofslist == 4, "Expecting 4"
    assert slist[keyval[0]] == (
        100, 100, 90, 100, 100), "Expecting (100, 100, 90, 100, 100) "
    assert slist[keyval[3]] == (
        60, 60, 100, 90, 90), "Expecting (100, 100, 90, 100, 100) "


def test_findStudents():
    students = main.makeList()

    gtlist = main.findstudents(students)
    lenofdict = len(gtlist)
    print('The number of students in your result ', lenofdict)
    main.printList(gtlist)
    assert lenofdict == 3, "Expecting 3"
    assert gtlist[0]['ID'] == 1003, "Expecting 1003"
    assert gtlist[1]['ID'] == 1004, "Expecting 1004"
    assert gtlist[2]['ID'] == 1005, "Expecting 1005"


def test_getAvgList():
    students = main.makeList()

    avglist = main.getAvgList(students)
    print(avglist)

    assert len(avglist) == 5, "Expecting 5"
    assert avglist[0] == 70.0, "Expecting 70.0"
    assert avglist[1] == 73.75, "Expecting 73.75"
    assert avglist[4] == 87.5, "Expecting 87.5"
