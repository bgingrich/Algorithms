#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  allPlays = [[]]
  for i in range(n):
    newPlays = []
    for a in allPlays:
      for p in plays:
        newPlay = a + [p]
        newPlays.append(newPlay)
    allPlays = newPlays
  return allPlays  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')