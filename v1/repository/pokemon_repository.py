import requests
from typing import List

from v1.models.pokemon import Pokemon


class PokemonRepository:
    def __init__(self):
        self.pokemons: List[Pokemon] = []
        self.data_url = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"
        self.fetch_and_store_data()

    def fetch_and_store_data(self):
        response = requests.get(self.data_url)
        if response.status_code == 200:
            pokemon_data = response.json()
            self.pokemons = [Pokemon(**data) for data in pokemon_data]

    def get_all_pokemons(self) -> List[Pokemon]:
        return self.pokemons

    def get_pokemon_by_id(self, pokemon_id: int) -> Pokemon:
        return next((pokemon for pokemon in self.pokemons if pokemon.id == pokemon_id))

    def add_pokemon(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)

    def update_pokemon(self, pokemon_id: int, updated_pokemon: Pokemon):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.id == pokemon_id:
                self.pokemons[i] = updated_pokemon
                return True
        return None

    def delete_pokemon(self, pokemon_id: int):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.id == pokemon_id:
                del self.pokemons[i]
                return True
        return None
