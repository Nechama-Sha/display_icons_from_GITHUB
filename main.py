
import displayPython
import asyncio


def main():
    manage()

def manage():
    while(True):
        temp=input("press 1 to print all icons' names or 2 to search an icon's name by a keyword")
        if temp.isdigit():
            ans=int(temp)
            if ans==1:
                displayPython.display_all()
            else:
                displayPython.display_by_keyword()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
