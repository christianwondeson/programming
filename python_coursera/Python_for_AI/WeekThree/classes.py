import matplotlib.pyplot as plt


# defined the parent class
class Circle(object):
    def __init__(self, radius=3, color="blue"):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius += r
        return self.radius

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis("scaled")
        plt.show()


RedCircle = Circle(10, "red")
dir(RedCircle)
RedCircle.drawCircle()


class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color="r"):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(
            plt.Rectangle((0, 0), self.width, self.height, fc=self.color)
        )
        plt.axis("scaled")
        plt.show()


SkinnyBlueRectangle = Rectangle(2, 3, "blue")
SkinnyBlueRectangle.drawRectangle()
