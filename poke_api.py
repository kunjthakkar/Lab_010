import requests
import image_lib
import os 

Poke_api_link = 'https://pokeapi.co/api/v2/pokemon/'

#The main function that will help other functions to run the script 
def main():
    poke_info = get_poke_info("Rockruff")
    poke_info = get_poke_info("123")
    names= get_pokemon_name()
    download_pokemon_artwork('dugtrio' , 'c:\\temp')
    return

def get_poke_info(pokemon):
    """ Gets info about a specific Pokemon from the PokeAPi.
    
    Args:
         pokemon (str): Pokemon name (or Pokedex number )
         
    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
#converting to string object and all lower case
    pokemon = str(pokemon).strip().lower() 
    
#checking if the name is an empty string 
    if pokemon == '':
        print('Error : Pokemon name not found')
        return 

#sending GET request 
    print(f'Getting information for {pokemon}... ', end='')
    url = Poke_api_link +pokemon
    
    response_message = requests.get(url)
    
# check if the request was successful 
    if response_message.status_code == requests.codes.ok:
        print('successful')
    
#Return dictionary of Pokemon 
        return response_message.json()
    else:
        print('failure')
        print(f' Response code: {response_message.status_code}({response_message.reason})')

        return
    
def get_pokemon_name(offset=0, limit=100000):
#This command helps to get mame of all the pokemons that

    
    query_parameter = {
        "limit" : limit,
        "offset" : offset
    }
#sending GET request  for name
    print(f'Getting list of Pokemon names ... ', end='')
    response_message = requests.get(Poke_api_link, params=query_parameter)
    
# check if the request was successful 
    if response_message.status_code == requests.codes.ok:
        print('successful')
    
#Return dictionary of Pokemon 
        dictionary = response_message.json()
        pokemon_names = [p["name"] for p in dictionary['results']]
        return pokemon_names
    
    else:
        print('failure')
        print(f' Response code: {response_message.status_code}({response_message.reason})')

        return    
    
def download_pokemon_artwork(pokemon, folder_path):
    
    poke_info = get_poke_info(pokemon)
    if poke_info is None:
        return False
    poke_image_url = poke_info['sprites']['other']['official-artwork']['front_default']
    
    image_data =image_lib.download_image(poke_image_url)
    
    if image_data is None:
        return False
    
    #this code is to get the extension 
    image_extension = poke_image_url.split('.')[-1]
    file_name = f'{poke_info["name"]}.{image_extension}'
    file_path = os.path.join(folder_path, file_name)
    
    
    if image_lib.save_image_file(image_data, file_path ):
        return file_path
    
    return False
    
    
    
    if __name__ == '__main__':
        main()