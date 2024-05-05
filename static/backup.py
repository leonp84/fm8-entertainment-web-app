# from .models import Movie
# import json5

# with open('data.json', 'r') as file:
#     json_string = file.read()

# contents = json5.loads(json_string)

# for movie in contents:
#     if movie['isTrending']:
#         my_movie = Movie(
#             title=movie['title'],
#             year=movie['year'],
#             category=movie['category'],
#             rating=movie['rating'],
#             isBookmarked=movie['isBookmarked'],
#             isTrending=movie['isTrending'],
#             thumbnail_trending_small=movie['thumbnail']['trending']['small'][2:],
#             thumbnail_trending_large=movie['thumbnail']['trending']['large'][2:],
#             thumbnail_regular_small=movie['thumbnail']['regular']['small'][2:],
#             thumbnail_regular_medium=movie['thumbnail']['regular']['medium'][2:],
#             thumbnail_regular_large=movie['thumbnail']['regular']['large'][2:]
#         )
#         my_movie.save()
#     else:
#         my_movie = Movie(
#             title=movie['title'],
#             year=movie['year'],
#             category=movie['category'],
#             rating=movie['rating'],
#             isBookmarked=movie['isBookmarked'],
#             isTrending=movie['isTrending'],
#             thumbnail_regular_small=movie['thumbnail']['regular']['small'][2:],
#             thumbnail_regular_medium=movie['thumbnail']['regular']['medium'][2:],
#             thumbnail_regular_large=movie['thumbnail']['regular']['large'][2:]
#         )
#         my_movie.save()
