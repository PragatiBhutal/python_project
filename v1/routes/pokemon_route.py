from fastapi import APIRouter, Depends
from typing import List

from v1.models.pokemon import Pokemon
from v1.repository.pokemon_repository import PokemonRepository
from v1.services.pokemon_service import PokemonService

router = APIRouter()


def get_pokemon_service():
    repository = PokemonRepository()
    return PokemonService(repository)


@router.get("/pokemons", response_model=List[Pokemon])
def get_all_pokemons(service: PokemonService = Depends(get_pokemon_service)):
    return service.get_all_pokemons()


@router.get("/pokemons/{pokemon_id}", response_model=Pokemon)
def get_pokemon(pokemon_id: int, service: PokemonService = Depends(get_pokemon_service)):
    return service.get_pokemon_by_id(pokemon_id)


@router.post("/pokemons", response_model=Pokemon)
def add_pokemon(pokemon: Pokemon, service: PokemonService = Depends(get_pokemon_service)):
    return service.add_pokemon(pokemon)


@router.put("/pokemons/{pokemon_id}", response_model=Pokemon)
def update_pokemon(pokemon_id: int, updated_pokemon: Pokemon, service: PokemonService = Depends(get_pokemon_service)):
    return service.update_pokemon(pokemon_id, updated_pokemon)


@router.delete("/pokemons/{pokemon_id}", response_model=Pokemon)
def delete_pokemon(pokemon_id: int, service: PokemonService = Depends(get_pokemon_service)):
    return service.delete_pokemon(pokemon_id)
