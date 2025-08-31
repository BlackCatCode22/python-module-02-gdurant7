print('What will the following python program print out?\n'
      'def fred ():\n'
      '    print("Zap")\n'
      '\n'
      'def jane():\n'
      '    print("ABC")\n'
      '\n'
      'jane()\n'
      'fred()\n'
      'jane()\n')

def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()

print('Answer: d) ABC Zap ABC')