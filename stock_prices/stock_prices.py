#!/usr/bin/python

import argparse

def find_max_profit(prices):
  lowest = prices[0]
  highest = prices[0]
  max_profit = None
  for price in prices[1:]:
    difference = price - lowest
    if max_profit == None or difference > max_profit:
      max_profit = difference
    if price > highest:
      highest = price
    if price < lowest:
      lowest = price  
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))