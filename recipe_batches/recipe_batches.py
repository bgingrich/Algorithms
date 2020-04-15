#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = None
  for recipe_ingredients, recipe_count in recipe.items():
    if recipe_ingredients in ingredients:
      ingredient_count = ingredients[recipe_ingredients]
      maximum = int(ingredient_count/recipe_count)
      if batches == None or maximum < batches:
        batches = maximum
    else:
      return 0

  return batches or 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 200, 'butter': 100, 'flour': 51 }
  print("{batches} batch(es) can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))