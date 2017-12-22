import media


#It is good practice to call your class definition in one file
#and to call/use your class in a different file.

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0,0,300,450",
                        "https://youtu.be/KYz2wyBy3kc")

print (toy_story.storyline)
