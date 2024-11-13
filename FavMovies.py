#Display
def display_movies(movies):
    if not movies:
        print("No movies in the list.")
    else:
        print("\nFavorite Movies:")
        for title, details in movies.items():
            print(f"- {title} | Genre: {details['genre']} | Rating: {details['rating']}")
    print()

#add
def add_movie(movies):
    title = input("Enter the movie title: ")
    genre = input("Enter the genre: ")
    rating = input("Enter the rating: ")
    
    movies[title] = {'genre': genre, 'rating': rating}
    print(f"{title} has been added.\n")

#rem
def remove_movie(movies):
    title = input("Enter the movie title to remove: ")
    if title in movies:
        del movies[title]
        print(f"{title} has been removed.\n")
    else:
        print(f"{title} is not in the list.\n")

#main menu
def main():
    movies = {}
    while True:
        print("1.Add a Movie")
        print("2.Remove a Movie")
        print("3.View Movies")
        print("4.Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            remove_movie(movies)
        elif choice == '3':
            display_movies(movies)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()