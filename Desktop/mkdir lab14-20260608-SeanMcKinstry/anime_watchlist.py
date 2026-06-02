class Anime:
    def __init__(self,title, genre, status):
        self._title = title 
        self._genre = genre 
        self._status = status

    def display_info(self):
         print("Title:" ,self._title) 
         print("Genre:" ,self._genre)
         print("Status:" ,self._status) 

    def update_status(self, new_status):
         self._status = new_status

anime1 = Anime("Demon Slayer","Action","Watching")
anime2 = Anime("Spy x Family","Comedy","Completed")
anime3 = Anime("Jujutsu Kaisen","Action","Plan to Watch")


anime_list = [anime1, anime2, anime3]



for anime in anime_list:
     anime.display_info()
     print()


print ("Updating anime status...")
anime3.update_status("Watching")

print ("Updated Anime:")
anime3.display_info()