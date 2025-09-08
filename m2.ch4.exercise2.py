print('Move the last line of program to the top.\n What error message do you get?')
print('You get a Traceback, and a NameError: name is not defined')

print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()


repeat_lyrics()