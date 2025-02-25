from typing import List

from v1.models.pokemon import Pokemon
from v1.repository.pokemon_repository import PokemonRepository


class PokemonService:
    def __init__(self, repository: PokemonRepository):
        self.repository = repository

    def get_all_pokemons(self) -> List[Pokemon]:
        return self.repository.get_all_pokemons()

    def get_pokemon_by_id(self, pokemon_id: int) -> Pokemon:
        return self.repository.get_pokemon_by_id(pokemon_id)

    def add_pokemon(self, pokemon: Pokemon):
        self.repository.add_pokemon(pokemon)
        return pokemon

    def update_pokemon(self, pokemon_id: int, updated_pokemon: Pokemon) -> Pokemon:
        return self.repository.update_pokemon(pokemon_id, updated_pokemon)

    def delete_pokemon(self, pokemon_id: int) -> Pokemon:
        return self.repository.delete_pokemon(pokemon_id)
