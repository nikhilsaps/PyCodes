# this code will check movie name and disply playing info

class  movie:
    def __init__(self,name,genre,rating):
        self.name= name
        self.genre=genre
        self.rating=rating

    def __str__(self):
        return f"the movie {self.name} and {self.genre} and {self.rating}"


    def play(self):
        playing =True
        print(f"movie is playing {self.name}")

    def pause(self):
        playing =False
        print(f"movie is paused {self.name}")

def main():
    p=movie("nikhil ","horror",10)
    p.pause()





if __name__== "__main__":
    main()
