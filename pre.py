# noinspection PyShadowingNames
def maze(arr):
    userinput = input("enter d for right,a for left, w for up ,s for down and stop to stop here only.")
    b = userinput

    if b == "stop":
        return

    if b == "a" or b == "d" or b == "w" or b == "s" or b == "E":

        for m in range(len(arr)):
            for n in range(len(arr[m:])):
                if arr[m][n] == "P":
                    i = m
                    j = n

        if arr[i][j + 1] == "E" and b == "d":
            print("Game over!!!!")
            return

        if b == "a":
            if j - 1 == -1:
                maze(arr)

            if arr[i][j - 1] == "*":
                maze(arr)

            if arr[i][j - 1] == " ":
                arr[i][j - 1] = "P"
                arr[i][j] = " "

        if b == "d":
            if j + 1 == arr[i].length:
                maze(arr)

            if arr[i][j + 1] == "*":
                maze(arr)

            if arr[i][j + 1] == " ":
                arr[i][j + 1] = "P"
                arr[i][j] = " "

        if b == "w":
            if i - 1 == -1:
                maze(arr)

            if arr[i - 1][j] == "*":
                maze(arr)

            if arr[i - 1][j] == " ":
                arr[i - 1][j] = "P"
                arr[i][j] = " "

        if b == "s":
            if i + 1 == arr.length:
                maze(arr)

            if arr[i + 1][j] == "*":
                maze(arr)

            if arr[i + 1][j] == " ":
                arr[i + 1][j] = "P"
                arr[i][j] = " "

        print("Update")
        line = ""
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                line += arr[i][j] + " "

            print(line)

            line = ""

        maze(arr)

    else:
        maze(arr)


a = "P"
i = 0
j = 0

anArray = [["P", "*", "*", "*", "*", "*", "*", "*", "*"],
           [" ", " ", "*", "*", "*", "*", "*", "*", "*"],
           ["*", " ", " ", "*", "*", "*", "*", "*", "*"],
           ["*", "*", " ", " ", "*", " ", " ", " ", "*"],
           ["*", "*", "*", " ", "*", " ", "*", " ", "*"],
           ["*", " ", " ", " ", "*", " ", "*", " ", "*"],
           ["*", " ", " ", " ", "*", " ", "*", " ", "*"],
           [" ", " ", "*", "*", "*", " ", "*", " ", "*"],
           [" ", "*", "*", "*", "*", " ", "*", " ", "*"],
           [" ", " ", "*", "*", "*", " ", "*", " ", "*"],
           ["*", " ", "*", " ", " ", " ", "*", " ", "*"],
           ["*", " ", "*", " ", "*", "*", "*", " ", "*"],
           ["*", " ", "*", " ", "*", "*", " ", " ", "*"],
           ["*", " ", " ", " ", "*", "*", " ", "*", "*"],
           ["*", "*", "*", "*", "*", "*", " ", "*", "*"],
           ["*", "*", "*", "*", "*", "*", " ", " ", "*"],
           ["*", "*", "*", "*", "*", "*", "*", " ", "*"],
           ["*", "*", "*", "*", "*", "*", "*", " ", "*"],
           ["*", "*", "*", "*", "*", "*", "*", " ", "E"],
           ["*", "*", "*", "*", "*", "*", "*", "*", "*"], ]
line: str = ""
for i in range(len(anArray)):
    for j in range(len(anArray[i])):
        line += anArray[i][j] + " "

    print(line)
    line = ""

maze(anArray)
