from django.shortcuts import render
from django.http import HttpResponse


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# ABOUT PAGE
def about(request):
    return render(request, 'about.html')

class Game:
    def __init__(self, title, rating, description):
        self.title = title
        self.rating = rating
        self.description = description

games = [
    Game('Fallout 3', 'PG-13', 'Post-Apocalyptic RPG / Strategy Game'),
    Game('The Sims 4', 'E for Everyone', 'Simpulation Strategy Game.')
]

# GAMES INDEX / VIEW ALL GAMES
def games_index(request):
    return render(request, 'games/index.html', { 'games' : games })