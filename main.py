from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    line1 = Line(Point(0, 0), Point(100, 100))
    line2 = Line(Point(100,100), Point(200, 200))
    win.create_line(line1, "red")
    win.create_line(line2, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
