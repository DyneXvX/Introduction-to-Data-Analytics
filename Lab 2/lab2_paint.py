# %%
def paint():
    print()
    print('Welcome to the paint needed calculator.')
    print('---------------------------------------')
    while True:
        try:
            length = int(input('Enter the length of the room: '))
            width = int(input('Enter the width of the room: '))
            height = int(input('Enter the height of the room: '))
            doors = int(input('How many doors are in the room? '))
            windows = int(input('How many windows are in the room? '))
            break
        except ValueError:
            print('Your values need to be in numbers please.')

    totaldoors = 25 * doors
    totalwindow = 10 * windows
    walls1 = 2*(width * height)
    walls2 = 2*(length * height)
    area = (walls1 + walls2) - (totaldoors + totalwindow)
    paintneeded = (area / 315)

    if (doors > 1 and windows <= 1):
        print('{paintneeded: .2f} gallons of paint are needed to a paint a room {width: .2f} feet wide by {length: .2f} feet long \
    by {height: .2f} feet height with {doors} doors and {windows} window'.format(**locals()))
    elif (doors <= 1 and windows > 1):
        print('{paintneeded: .2f} gallons of paint are needed to a paint a room {width: .2f} feet wide by {length: .2f} feet long \
    by {height: .2f} feet height with {doors} door and {windows} windows'.format(**locals()))
    elif (doors > 1 and windows > 1):
        print('{paintneeded: .2f} gallons of paint are needed to a paint a room {width: .2f} feet wide by {length: .2f} feet long \
    by {height: .2f} feet height with {doors} doors and {windows} windows'.format(**locals()))
    else:
        print('{paintneeded: .2f} gallons of paint are needed to a paint a room {width: .2f} feet wide by {length: .2f} feet long \
    by {height: .2f} feet height with {doors} door and {windows} window'.format(**locals()))

    print()

# For calculating the paint needed, the program should calculate the amount of paint needed to paint the
# walls of a room of the given length and width. You may use the following assumptions:

# Paint covers 315 square feet per gallon
# Each door in the room is 25 square feet and each window is 10 square feet.
# Rooms may contain four walls. Each wall can be considered a rectangle. The total area needed
# to paint the walls would area of the rectangle.
# 2 walls in the room will be a product of width and height,
# and the other 2 walls would be a product of the length and height of the room.
# Subtract door surface area and window area from the total area of the wall to be painted
# To calculate the volume of paint needed, you will have to divide the total area to be painted
# by the area that can be covered for a gallon.
# %%
