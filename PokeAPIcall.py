import requests
import pandas as pd
import os

def pokecall():
    categories = ["HP", "Atk", "Def", "SpAtk", "SPDef", "Spd"]
    pokedict = {"id": [], "Name": [], "HP": [], "Atk": [], "Def": [], "SpAtk": [],
            "SPDef": [], "Spd": [], "Weight": [], "Height": [], "Rarity": []}

    for i in range(1008):
        url = f"https://pokeapi.co/api/v2/pokemon/{i+1}"
        pokeponse = requests.get(url)
        pokelist = pokeponse.json()
        pokeponse.close()

        pokedict["id"].append(pokelist["id"])
        pokedict["Name"].append(pokelist["name"])
        pokedict["Weight"].append(pokelist["weight"])
        pokedict["Height"].append(pokelist["height"])

        for j in range(6):
            pokedict[categories[j]].append(pokelist["stats"][j]["base_stat"])

        url = f"https://pokeapi.co/api/v2/pokemon-species/{i+1}"
        pokeponse = requests.get(url)
        pokelist = pokeponse.json()
        pokeponse.close()

        if pokelist["is_mythical"] == True:
            rarity = "Mythical"
        elif pokelist["is_legendary"] == True:
            rarity = "Legendary"
        else:
            rarity = "Common"

        pokedict["Rarity"].append(rarity)
    path = os.getcwd()
    pokedex = pd.DataFrame.from_dict(pokedict).set_index("id")
    pokedex.to_csv(f"{path}\Dataframe\pokedex.csv")
