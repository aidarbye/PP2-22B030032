movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1
def IMBD_above_5_5(movies):
    return movies["imdb"] > 5.5

# for i in movies:
#   if IMBD_above_5_5(i):
#     print(i["name"], "score is above 5.5")

# 2

def IMBD_above5_5(movies):
  return [i for i in movies if i["imdb"] > 5.5]

# rated_5_5_above = IMBD_above5_5(movies)
# for i in rated_5_5_above:
#   print(i["name"], i["imdb"])

# 3 

def categoryFind(movies, category):
  return [i for i in movies if i["category"] == category]

# romance_movies = categoryFind(movies, "Romance")
# for i in romance_movies:
#   print(i["name"], i["imdb"])

# 4 

def average_imdb_score(movies):
  total_imdb = 0
  for i in movies:
    total_imdb += i["imdb"]
  return total_imdb / len(movies)

# avg = average_imdb_score(movies)
# print("The avg is", avg)

# 5

def average_imdb_score_by_category(movies, category):
  movies_in_category = categoryFind(movies, category)
  total_imdb = 0
  for i in movies_in_category:
    total_imdb += i["imdb"]
  return total_imdb / len(movies_in_category)

# avg = average_imdb_score_by_category(movies, "Romance")
# print("The average is", avg)