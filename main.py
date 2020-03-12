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

#Main routine goes here
recipe_name = not_blank("Please enter the name of your recipe: ")

error = ("Your recipe name contains a number")
noError = ("No errors detected :)")
message = ("")
hasErrors = False
numError = False

for letter in recipe_name:
  if letter.isdigit() == True:
    hasErrors = True
    numError = True
    message = error

print("You are making {}".format(recipe_name),": ", message)