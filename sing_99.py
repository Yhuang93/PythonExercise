# Print every line of the song "99 bottles on the wall"
# writing a function
def sing_99():
    for bo in range(99,-1,-1):
        if bo == 0:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall...")
        elif bo == 1:
            print("{} bottle of beer on the wall, {} bottle of beer.".format(bo,bo))
            print("Take one down, pass it around, no more bottles of beer to go.")
        elif bo == 2:
            print("{} bottles of beer on the wall, {} bottles of beer.".format(bo,bo))
            print("Take one down, pass it around, 1 bottle of beer on the wall...")
        else:
            print("{} bottles of beer on the wall, {} bottles of beer.".format(bo,bo))
            print("Take one down, pass it around, {} bottles of beer on the wall...".format(bo-1))
sing_99()
