import random


def main():
  level = get_level()

  ex = 0
  score = 0
  while ex < 10:
    x = generate_integer(level)
    y = generate_integer(level)
    ex += 1

    err = 0
    while err < 3:
      try:
        z = int(input(f'{x} + {y} = '))
      except ValueError:
        print('EEE')
        err += 1
      else:
        if z == (x + y):
          score += 1
          print('you score', score)
          break
        else:
          print('EEE')
          err += 1

    if err == 3:
      print(f'{x} + {y} = {x+y}')
  print('Score:', score)

def get_level():
  while True:
    try:
      level = int(input('Level: '))
    except ValueError:
      pass
    else:
      if 1 <= level <= 3:
        return level


def generate_integer(level):
  i = 10 ** (level - 1)
  j = 10 ** level - 1
  if level == 1:
    i -= 1
  print(i, j)
  return random.randint(i, j)


if __name__ == "__main__":
  main()