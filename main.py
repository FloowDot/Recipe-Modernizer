#Get recipes name and check its not blank

#Not blank function goes here
def not_blank(question):

  valid = False
  while not valid:
    response = input(question)
    if response == "":
      continue
    else:
      return response

    return response

#Main routine goes here
recipe_name = not_blank("Please enter the name of your recipe: ")

print("You are making {}".format(recipe_name))
