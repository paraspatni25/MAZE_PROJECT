"""
Paras Patni
Vishnu Vardhan
"""


def maze_map(array: object) -> object:

    """This function will run the map/grid/maze
    :type array: object
    :rtype: object
    """

    command = ""
    """Taking a variable"""
    while command == "":
        """Defining the loop to take input from user until the user give a valid input"""
        command = input("Enter 6 for moving the player P to right, "
                        " 4 for for moving the player P to left, "
                        " 8 for for moving the player P to up, "
                        " 2 for for moving the player P to down"
                        " and to quit the game at anytime enter quit ")
        """Assigning the variable with the given input by user"""

    if "quit" == command:
        """Checking the input if user wants to quit the game or not """
        quit_message()
        """This function will Display the quiting message defined in function"""
        return
    if command != '' and command.isdigit():
        command = int(command)
        """Using this condition we are converting the input into integer 
        Again after converting the input we are again saving back in the same variable"""

    if not command != 4 or not command != 6 or not command != 8 or not command != 2:
        """the condition to check the given input i what we need to run the game"""

        for a in range(len(array)):
            """this loop will display the position of player "p" in the game"""
            for b in range(len(array[a])):
                if not "P" != array[a][b]:
                    i: int = a
                    j: int = b

        if not array[i + 1][j] != "E ":
            """checking the for the EXIT in the next position in the game"""
            if not command != 2:
                if not command != 6:
                    array[i][j + 1] = " "
                    array[i][j + 1] = "P"
                    array[i][j] = " "
                    to_print_array(array)
                    """printing the game to the screen"""
                    end_screen()
                    """the function will print the ending screen"""
                    return

            elif not array[i][j + 1] != "E" and not command != 6:
                """checking the for the EXIT in the next position in the game with given input"""
                array[i][j + 1] = " "
                array[i][j + 1] = "P"
                array[i][j] = " "
                to_print_array(array)
                """printing the game to the screen"""
                end_screen()
                """the function will print the ending screen"""
                return

            elif not array[i][j - 1] != "E" and not command != 4:
                """checking the for the EXIT in the next position in the game with given input"""
                array[i][j - 1] = " "
                array[i][j - 1] = "P"
                array[i][j] = " "
                to_print_array(array)
                """printing the game to the screen"""
                end_screen()
                """the function will print the ending screen"""
                return

            elif not array[i + 1][j] != "E" and not command != 2:
                """checking the for the EXIT in the next position in the game with given input"""
                array[i + 1][j] = " "
                array[i + 1][j] = "P"
                array[i][j] = " "
                to_print_array(array)
                """printing the game to the screen"""
                end_screen()
                """the function will print the ending screen"""
                return

            elif not array[i - 1][j] != "E" and not command != 8:
                """checking the for the EXIT in the next position in the game with given input"""
                array[i - 1][j] = " "
                array[i - 1][j] = "P"
                array[i][j] = " "
                to_print_array(array)
                """printing the game to the screen"""
                end_screen()
                """the function will print the ending screen"""
                return

        elif not array[i][j - 1] != "E" and not command != 4:
            """checking the for the EXIT in the next position in the game with given input"""
            array[i][j - 1] = " "
            array[i][j - 1] = "P"
            array[i][j] = " "
            to_print_array(array)
            """printing the game to the screen"""
            end_screen()
            """the function will print the ending screen"""
            return

        elif not array[i + 1][j] != "E" and not command != 2:
            """checking the for the EXIT in the next position in the game with given input"""
            array[i + 1][j] = " "
            array[i + 1][j] = "P"
            array[i][j] = " "
            to_print_array(array)
            """printing the game to the screen"""
            end_screen()
            """the function will print the ending screen"""
            return

        elif not array[i - 1][j] != "E" and not command != 8:
            """checking the for the EXIT in the next position in the game with given input"""
            array[i - 1][j] = " "
            array[i - 1][j] = "P"
            array[i][j] = " "
            to_print_array(array)
            """printing the game to the screen"""
            end_screen()
            """the function will print the ending screen"""
            return

        elif not array[i][j + 1] != "E" and not command != 6:
            """checking the for the EXIT in the next position in the game with given input"""
            array[i][j + 1] = " "
            array[i][j + 1] = "P"
            array[i][j] = " "
            to_print_array(array)
            """printing the game to the screen"""
            end_screen()
            """the function will print the ending screen"""
            return

        elif not command != 4:
            """changing the position of player in the game with given input"""

            if not j - 1 != -1:
                maze_map(array)
                """Calling the function """

            elif not array[i][j - 1] != "X":
                maze_map(array)
                """Calling the function """

            elif not array[i][j - 1] != " ":
                array[i][j - 1] = "P"
                array[i][j] = " "

            elif not array[i][j + 1] != "E":
                array[i][j + 1] = "P"
                array[i][j] = " "

        elif not command != 6:
            """changing the position of player in the game with given input"""

            if not j + 1 != len(array[i]):
                maze_map(array)
                """Calling the function """

            elif not array[i][j + 1] != "X":
                maze_map(array)
                """Calling the function """

            elif not array[i][j + 1] != " ":
                array[i][j + 1] = "P"
                array[i][j] = " "

            elif not array[i][j + 1] != "E":
                array[i][j + 1] = "P"
                array[i][j] = " "

        elif not command != 8:
            """changing the position of player in the game with given input"""

            if not i - 1 != -1:
                maze_map(array)
                """Calling the function """

            elif not array[i - 1][j] != "X":
                maze_map(array)
                """Calling the function """

            elif not array[i - 1][j] != " ":
                array[i - 1][j] = "P"
                array[i][j] = " "

            elif not array[i][j + 1] != "E":
                array[i][j + 1] = "P"
                array[i][j] = " "

        elif not command != 2:
            """changing the position of player in the game with given input"""

            if not i + 1 != len(array):
                maze_map(array)
                """Calling the function """

            elif not array[i + 1][j] != "X":
                maze_map(array)
                """Calling the function """

            elif not array[i + 1][j] != " ":
                array[i + 1][j] = "P"
                array[i][j] = " "

        to_print_array(array)
        """printing the game to the screen"""
        maze_map(array)
        """Calling the function """

    else:
        maze_map(array)
        """Calling the function """
    return


def level():
    maze_level: str = ""
    while not maze_level != "":
        maze_level = (input("Please choose your level : for EASY press 1 ,  for MEDIUM press 2 ,  For HARD press 3"))
    if not maze_level != "1" or not maze_level != "2" or not maze_level != "3":
        if not maze_level != "2":
            array = [
                ["P", " ", " ", " ", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", " ", "X", " ", " ", " ", " ", " ", "X", "X", " ", "X", "X", "X", "X", "X", " ", "X", "X", " ", " ", " ", " ", " ", " ", "X", "X"],
                ["X", " ", " ", " ", " ", " ", " ", "X", "X", " ", "X", " ", " ", " ", "X", " ", " ", "X", " ", " ", "X", " ", " ", "X", "X", "X", "X", " ", " ", "X"],
                ["X", " ", "X", "X", "X", "X", " ", "X", "X", " ", "X", " ", "X", "X", "X", "X", " ", "X", " ", "X", "X", " ", "X", "X", "X", "X", "X", "X", " ", "X"],
                ["X", " ", " ", " ", "X", "X", " ", "X", " ", " ", " ", " ", "X", "X", "X", "X", " ", "X", " ", " ", " ", " ", "X", "X", "X", "X", "X", "X", " ", "X"],
                ["X", "X", "X", " ", "X", " ", " ", "X", "X", "X", " ", "X", "X", "X", " ", " ", " ", "X", " ", " ", " ", "X", "X", " ", " ", " ", " ", " ", " ", "X"],
                ["X", "X", "X", " ", "X", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", "X", "X", "X", "X", " ", "X", "X", " ", "X", "X", "X", "X", " ", "X"],
                [" ", " ", " ", " ", "X", "X", " ", "X", "X", "X", " ", " ", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", "X", " ", "X", "X", "X", "X", " ", "X"],
                ["X", " ", "X", "X", "X", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", " ", " ", "X", "X", "X", " ", "X", "X", " ", "X", "X", "X", "X", " ", "X"],
                ["X", " ", "X", "X", "X", "X", " ", " ", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", " ", " ", "X", " ", " ", "X", "X", " ", " ", " ", "X"],
                ["X", " ", " ", "X", "X", " ", " ", "X", "X", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X", "X", " ", " ", "X", "X", "X", " ", "X", "X", "X"],
                ["X", "X", " ", "X", "X", " ", "X", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", " ", " ", "X", " ", " ", "X", "X", "X", " ", " ", "X", "X"],
                ["X", "X", " ", " ", "X", " ", " ", "X", "X", "X", " ", "X", " ", " ", " ", "X", " ", "X", "X", " ", "X", "X", " ", " ", " ", " ", "X", " ", "X", "X"],
                ["X", "X", "X", " ", "X", "X", " ", "X", "X", "X", " ", " ", " ", " ", "X", " ", " ", "X", " ", " ", "X", "X", " ", " ", "X", "X", "X", " ", " ", "X"],
                ["X", "X", "X", " ", "X", "X", " ", " ", " ", "X", "X", " ", "X", " ", "X", " ", "X", "X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X"],
                ["X", "X", "X", " ", "X", "X", "X", "X", " ", "X", " ", " ", "X", " ", "X", " ", "X", "X", " ", " ", " ", "X", "X", " ", " ", " ", "X", " ", " ", "X"],
                ["X", "X", "X", " ", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", " ", "X", "X", "X", "X", " ", " ", " ", " ", "X", " ", "X", " ", "X", "X"],
                ["X", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", " ", "X", "X", "X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", " ", "X"],
                ["X", "X", "X", "X", " ", " ", " ", " ", " ", "X", "X", " ", "X", "X", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", "X", " ", "E"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]]
            to_print_array(array)
            """printing the game to the screen"""
            maze_map(array)
            """Calling the function to initialize the game"""

        elif not maze_level != "1":
            array = [
                ["P", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X", ],
                ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", ],
                ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
                ["X", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", "X", "X", ],
                ["X", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "E", ],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ]]
            to_print_array(array)
            """printing the game to the screen"""
            maze_map(array)
            """Calling the function to initialize the game"""

        elif not maze_level != "3":
            array = [
                ["P", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
                ["X", " ", "X", "X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", " ", " ", "X", ],
                ["X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", " ", " ", "X", ],
                ["X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", "X", "X", " ", "X", ],
                ["X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", "X", " ", " ", " ", "X", ],
                ["X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", "X", " ", "X", " ", "X", ],
                ["X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", "X", "X", ],
                ["X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", " ", "X", "X", "X", "X", ],
                ["X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", " ", " ", "X", ],
                ["X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", "X", "X", "X", " ", "X", ],
                ["X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", " ", " ", "X", ],
                ["X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", " ", "X", "X", "X", "X", ],
                ["X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", "X", " ", " ", "E", ],
                ["X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", "X", ],
                ["X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", "X", " ", " ", "X", ],
                ["X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", " ", "X", " ", "X", "X", ],
                ["X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", " ", "X", "X", " ", "X", " ", "X", " ", " ", "X", ],
                ["X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", " ", "X", " ", "X", "X", " ", "X", ],
                ["X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X", ],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ]]
            to_print_array(array)
            """printing the game to the screen"""
            maze_map(array)
            """Calling the function to initialize the game"""

    else:
        print("You have given an invalid input please choose from the below option only")
        level()
        """Calling the function to initialize the game"""
    return


def welcome_screen():
    """this function will print the predefined welcome message"""
    q = '   #     #'
    w = '   #  #  #  ######  #        ####    ####   #    #  ######      #####   ####       #####  #    #  ######      #    #    ##    ######  ###### '
    e = '   #  #  #  #       #       #    #  #    #  ##  ##  #             #    #    #        #    #    #  #           ##  ##   #  #       #   #      '
    r = '   #  #  #  #####   #       #       #    #  # ## #  #####         #    #    #        #    ######  #####       # ## #  #    #     #    #####  '
    t = '   #  #  #  #       #       #       #    #  #    #  #             #    #    #        #    #    #  #           #    #  ######    #     #      '
    y = '   #  #  #  #       #       #    #  #    #  #    #  #             #    #    #        #    #    #  #           #    #  #    #   #      #      '
    u = '    ## ##   ######  ######   ####    ####   #    #  ######        #     ####         #    #    #  ######      #    #  #    #  ######  ###### '
    o = '                                                                                                                                             '
    print(q)
    print(w)
    print(e)
    print(r)
    print(t)
    print(y)
    print(u)
    print(o)


def end_screen() -> object:
    """the function will print the ending screen"""
    q = '    #####          #         #     #      #######      #######      #     #      #######      ######         ##                             ##'
    w = '   #     #        # #        ##   ##      #            #     #      #     #      #            #     #       #     #   #             #   #     #'
    e = '   #             #   #       # # # #      #            #     #      #     #      #            #     #      #       # #               # #       #'
    r = '   #  ####      #     #      #  #  #      #####        #     #      #     #      #####        ######       #     #######           #######     #'
    t = '   #     #      #######      #     #      #            #     #       #   #       #            #   #        #       # #               # #       #'
    y = '   #     #      #     #      #     #      #            #     #        # #        #            #    #        #     #   #             #   #     #'
    u = '    #####       #     #      #     #      #######      #######         #         #######      #     #        ##                             ##'
    o = '                                                                                                                          #######'

    print(q)
    print(w)
    print(e)
    print(r)
    print(t)
    print(y)
    print(u)
    print(o)
    print("Thank You For Playing")
    return


def to_print_array(array) -> object:
    """printing the game to the screen"""
    """

    :rtype: object
    """
    line_to_print_array: str = ""
    """taking a variable to store the array in form of line to display output"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            line_to_print_array += array[i][j] + " "

        print(line_to_print_array)
        line_to_print_array = ""
        """resetting the variable to print the new line"""
    return


def quit_message():
    """the function will print the quit message screen"""
    q = "#####   #         ##    #   #        ##     ####     ##    #  #    #"
    w = "#    #  #        #  #    # #        #  #   #    #   #  #   #  ##   #"
    e = "#    #  #       #    #    #        #    #  #       #    #  #  # #  #"
    r = "#####   #       ######    #        ######  #  ###  ######  #  #  # #"
    t = "#       #       #    #    #        #    #  #    #  #    #  #  #   ##"
    y = "#       ######  #    #    #        #    #   ####   #    #  #  #    #"
    print(q)
    print(w)
    print(e)
    print(r)
    print(t)
    print(y)


welcome_screen()
"""Calling the function to print welcome message of the game"""
level()
"""Calling the function to initialize the game"""
