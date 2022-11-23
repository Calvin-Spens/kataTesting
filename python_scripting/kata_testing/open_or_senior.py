# The Western Suburbs Croquet Club has two categories of membership, 
# Senior and Open.
# They would like your help with an application form that will tell 
# prospective members which category they will be placed.
#
# To be a senior, a member must be at least 55 years old and 
# have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; 
# the better the player the lower the handicap.
#
# Input
# Input will consist of a list of pairs. 
# Each pair contains information for a single potential member. 
# Information consists of an integer for the person's age and 
# an integer for the person's handicap.
#
# Output
# Output will consist of a list of string values 
# (in Haskell and C: Open or Senior) stating whether the 
# respective member is to be placed in the senior or open category.

def open_or_senior(data):
#     categeory = []
#     for age_score in data:
#         if age_score[0] > 54 and age_score[1] > 7:
#             categeory.append("Senior")
#         else: 
#             categeory.append("Open")
#     return categeory

    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

 print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])) 
