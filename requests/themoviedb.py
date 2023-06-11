import requests
class TheMovieDB:
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkM2FjZDRkNGJlNDVjYTJkZDQzNGY2ZmNmZDk5OWQxZSIsInN1YiI6IjY0NzRjMDk3OWFlNjEzMDE0NjY4ZGI3OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aRwdnN4w9TlVzX1KhIQQEcQ_N5ivAabmFUWYYTKObLg"
        }
        self.api_url = "https://api.themoviedb.org/3/"
        

    def getTrending(self):
        url = self.api_url + "trending/movie/day?language=en-US"
        response = requests.get(url,headers=self.headers)
        return response.json()

    def searchFilm(self,keyword,adult,page):
        url = self.api_url + f"search/movie?query={keyword}&include_adult={adult}&language=en-US&page={page}"
        response = requests.get(url,headers=self.headers)
        return response.json()
object = TheMovieDB()

while True:
    choose = input("1- Trending Movies\n2- Search Film\n3- Exit\nPlease write number: ")
    if choose == "3":
        break
    else:
        if choose == "1":
            movies = object.getTrending()
            for movie in movies["results"]:
                print(movie["title"])
        
        elif choose == "2":
            keyword = input("Please write keyword for searching: ")
            keyword = keyword.strip()
            adult = input("Please select adult content (Y/N): ")
            if adult == "Y":
                adult == "true"
            elif adult == "N":
                adult == "false"
            else:
                adult = input("Please write 'Y' or 'N': ")
            page = int(input("Please enter the number of pages you wish to view: "))
            movies = object.searchFilm(keyword=keyword,adult=adult,page=page)
            for movie in movies["results"]:
                print(f"{movie['original_title']} Overview: {movie['release_date']} Popularity: {movie['popularity']}")