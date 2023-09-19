import time as t

# message, you can set this to whatever

def Monkey(msg: str, urange: int = 1):

  monkey1 = """
            __
        w c(..)o   (
        |__(-)    __)
            /|   (
            (_)___)
            /|
           | |
           m  m
             """
  monkey2 = """
             __
       )   c(..)o w
      (__    (-)__|
         )   /|
        (____(_)
             /|
            / |
            m m
             """
  monkey = 1
  for x in range(urange * 2):
      for i in range(200):
        print()
      print(msg)
      if monkey == 1:
          print(monkey1)
          monkey = 2
      else:
          print(monkey2)
          monkey = 1
      t.sleep(0.5)
