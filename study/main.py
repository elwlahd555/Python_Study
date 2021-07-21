# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pythonProject.calculation import add, substract


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = 10;
    a = 5;
    a = '';
    if a == '':
        print("blank");
    elif a == 5:
        print("a 는 5");
    else:
        print("a 는 10");

    for i in range(0, 10):
        print(i);

    arr = [5, 3, 2, 1, 2, 4];

    dictval = dict();
    dictval["apple"] = 5;
    dictval["banana"] = 3;
    dictval["melon"] = 8;
    for j in dictval.keys():
        print(j);

    for l in dictval.keys():
        print(dictval[l]);

    try:
        a = [2, 3, 4, 5];
        print(a[4]);

    except Exception as e:
        print(e);

    # b=[4,1,3,10,3];
    b = ["b", "c", "eqsd"];
    # b.sort();
    b.sort(reverse=True);
    print(b);

    c=dict()
    c["Jessy"]=30
    c["suzy"]=28
    c["Minsu"]=40

    for i in c.values():
        print(i)

    print(add(4,5))
    print(substract(4,5))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
