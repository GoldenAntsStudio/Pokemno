from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.hp = randint(30, 60)
        self.power = randint(200, 400)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
        Сила покемона {self.power}
        Здоровья покемона: {self.hp}
        """


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return 'Pokemon volshebnik primenl shit'
        
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f'''Сражение {self.pokemon_trainer} c {enemy.pokemon_trainer} здоровье {enemy.pokemon_trainer} теперь {enemy.hp}'''
        else:
            enemy.hp = 0
            return f'''Pobeda {self.pokemon_trainer} над {enemy.pokemon_trainer}'''
class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(1, 15)
        self.power = super_power
        result = super().attack(enemy)
        self.power = super_power
        return result + f'\n Боец применил супер атаку силой: {super_power}'
