# 1. Создаем класс Movies.
class Movies:
# 2. Инициализируем пустой список.
    def __init__(self):
        self.movies = []
# 3. Добавляем метод, который принимает movie и добавляет его в конец списка.
    def add_movie(self, movie):
        self.movies.append(movie)
# 4. Создаем подклассы Comedy и Drama.
class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'
# 5 и 6. Создаем объекты, вызываем методы с входными параметрами.
comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))
        
    


        
        