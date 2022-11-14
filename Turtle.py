import turtle
from math import *
from random import *
from time import *
from turtle import *


class TurtleTest:
    def __init__(self, titre: str = "Turtle", moves=None, speed_turtle=0, width_turtle=3, backcolor=None, helper=False):
        if moves is None:
            moves = []
        self.__creator = "One Shot"
        self.birthday = "26/08/2022"
        self.name = titre
        self.speed = speed_turtle
        self.width = width_turtle
        self.backcolor = backcolor
        self.x = 1366
        self.y = 768
        self.T = ["red", "darkred", "darkorange", "orange", "gold", "lightyellow", "yellow", "lightgreen", "green",
                  "darkgreen", "turquoise", "cyan", "lightblue", "skyblue", "blue", "navy", "darkblue", "purple",
                  "magenta", "violet", "lightpink", "pink", "chocolate", "brown", "maroon", "white", "darkgrey", "grey",
                  "black"]
        self.g = len(self.T)                                                    # Nb couleurs disponibles
        if helper:
            self.Helper()
        self.CreateNew(moves)

    def CreateNew(self, mouvs):
        self.NewPainting()

        self.Fonction(mouvs)

        self.Exit()

    def NewPainting(self):
        title(self.name)
        setup(width=1.0, height=1.0)
        speed(self.speed)
        width(self.width)
        if self.backcolor is not None:
            bgcolor(self.backcolor)
        elif self.backcolor == "r" or self.backcolor == "random":
            self.RandomBackground()
        else:
            bgcolor("white")

    @staticmethod
    def RandomBackground():
        c1 = uniform(0, 1)
        c2 = uniform(0, 1)
        c3 = uniform(0, 1)
        bgcolor(c1, c2, c3)

    @staticmethod
    def Fonction(mouvs):
        for mouv in mouvs:
            try:
                if int(mouv[1:]):
                    if mouv[0] == "r":
                        rt(int(mouv[1:]))
                    elif mouv[0] == "f":
                        fd(int(mouv[1:]))
                    elif mouv[0] == "b":
                        bk(int(mouv[1:]))
                    elif mouv[0] == "p":
                        stamp()
                    elif mouv[0] == "u":
                        up()
                    elif mouv[0] == "d":
                        down()
                    elif mouv[0] == "h":
                        ht()
                    elif mouv[0] == "s":
                        speed(int(mouv[1]))
                    elif mouv[0] == "w":
                        width(int(mouv[1]))
                    elif mouv[0] == "g":
                        goto(int(mouv[1:5]), int(mouv[5:]))
                    elif mouv[0] == "c":
                        circle(int(mouv[1:4]), int(mouv[4:7]), int(mouv[7:]))
            except Exception as ex:
                print(ex)
                print(f"<Format movement '{mouv}' incorrect>\n")

    def Helper(self):
        lenght = 30
        print("-" * lenght)
        print(f"Programm name : {self.__class__.__name__}\nCreated by : {self.__creator}\nDate of creation : "
              f"{self.birthday}")
        print("-" * lenght)
        print(f"Purpose : \nUse to make simple programm with Turtle software.")
        print("-" * lenght)
        print(f"Arguments : \n- titre (string) : The title of the turtle window. Default value : 'Turtle'\n"
              f"- moves (array) : The movements the turtle will execute during the programm. Empty by default. Accept :\n"
              f"\t¤ 'r000' : Use to rotate the turtle. Can start from 0°C to 360°C.\n"
              f"\t¤ 'f0000' : Move the turtle forward the among of pixel entered. Can be negative.")
        print(f"\t¤ 'b0000' : The opposite of 'f0000', make the turtle move backward. Can be negative.\n"
              f"\t¤ 'p0' : Make the turtle stamp the cursor mark on the window.\n\t¤ 'u0' : Put the pen up (stop "
              f"drawing).\n\t¤ 'd0' : Put the pen down (restart drawing).\n\t¤ 'h0' : Hide the turtle (not visible on "
              f"screen).\n\t¤ 's0' : Set the speed of the turtle (default : speed = 0). Can start from 0 to 9. Maximum "
              f"speed : 0.\n\t¤ 'w0' : Set the width of the pen line (default : width = 3). Can start from 1 to 10.")
        print(f"\t¤ 'g00000000' : Make the turtle go to the point of coords ('0000', '0000'). Can't be negative.\n"
              f"\t¤ 'c0000000' : Make a circle of radius '000', an extent of '00' and steps of '00'. Can't be negative.")
        print(f"- speed_turtle (integer) : The speed of the turtle. Default value : 0 (max speed).\n- width_turtle"
              f"(integer) : The width of the pen line. Default value : 3.\n- backcolor (string) : The color of the "
              f"background. Default value : 'white'.\n- helper (boolean) : Write explaining texts on the console in "
              f"order to give informations about this programm to the user. \n  Active on True. Default value : False.")
        print("-" * lenght + "\n")

    @staticmethod
    def Exit():
        print("Création terminée !")
        sleep(0.5)
        print("Votre peinture est prête !")
        sleep(0.5)
        print("Merci d'avoir choisi CyberLife Entreprise !")
        exitonclick()


if __name__ == "__main__":
    Moves = ["f100", "r90", "b50", "r-90", "s3", "w6", "f30", "u0", "g00010001", "d0", "c0350401", "p0"]
    tortue = TurtleTest("Test", Moves, 5, 1, "red", True)

quit()
