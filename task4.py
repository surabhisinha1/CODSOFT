# Sample movie list
movies = [
    {"title": "Harry Potter", "genre": ["science-fiction", "drama", "mystery"], "type": "hollywood"},
    {"title": "Twilight", "genre": ["romance", "thriller", "vampire"], "type": "hollywood"},
    {"title": "Mission Mangal", "genre": ["science-fiction", "drama"], "type": "bollywood"},
    {"title": "Shershaah", "genre": ["war", "action", "drama"], "type": "bollywood"},
    {"title": "Sherlock Holmes", "genre": ["mystery", "detective-fiction"], "type": "hollywood"}
]

# Allowed options
valid_genres = ["science-fiction", "drama", "mystery", "romance", "thriller", "vampire", "war", "action", "detective-fiction"]
valid_types = ["hollywood", "bollywood"]

# Function to get valid input
def get_valid_input(prompt, valid_list):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_list:
            return user_input
        else:
            print("Please enter correctly.")

# Get user preferences with validation
print("Choose genre:\n- Science-Fiction \n- Drama \n- Mystery \n- Romance \n- Thriller \n- Vampire \n- War \n- Action \n- Detective-fiction")
user_genre = get_valid_input("Enter genre: ", valid_genres)

print("Choose type:\n- Hollywood \n- Bollywood")
user_type = get_valid_input("Enter type: ", valid_types)

# Recommendation function
def recommendation(user_genre, user_type, movie_list):
    suggestions = []
    for m in movie_list:
        if m["type"] == user_type:
            count = len(set([user_genre]) & set(m["genre"]))
            if count > 0:
                suggestions.append((m["title"], count))
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return [title for title, _ in suggestions]

# Get recommendations
recommended_movies = recommendation(user_genre, user_type, movies)

# Output results
if recommended_movies:
    print("\nRecommended Movies for You:")
    for movie in recommended_movies:
        print(" -", movie)
else:
    print("No matching movies found.")
