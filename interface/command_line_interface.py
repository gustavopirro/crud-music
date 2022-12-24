from controller.music_controller import *
import logging


def handle_data(db_data, data_type):
    ARRAY_TYPE = type([])
    DICT_TYPE = type({})

    if data_type == ARRAY_TYPE:
        for obj in db_data:
            try:
                print(obj['name'], obj['artist'], obj['published_at'])
            except KeyError as e:
                logging.error(e)
    
    elif data_type == DICT_TYPE:
        try:
            print('\n', db_data['name'], db_data['artist'], db_data['published_at'])
        except KeyError as e:
            logging.error(e)
    
    else:
        print('Ops! não foi possível realizar esta ação!')
    

    

def run_cli():
    user_input_choice = None
    menu_functions = {
        1: add_music,
        2: search_music,
        3: filter_musics_by_year,
        4: get_musics,
        5: stop_cli
    }

    print('Bem vindo ao gerenciador de musicas, por favor escolha a opção desejada:')
    while True:
        try:
            user_input_choice = int(
                input('\n1 - Adicionar musica\n2 - Buscar música\n3 - Filtrar músicas por ano de publicação\n4 - Mostrar lista de músicas\n5 - Finalizar Programa\n'))
        except ValueError:
            print('\nPor favor insira um valor valido.\n\n')
        
        if type(user_input_choice) != int or user_input_choice > 5:
            print('\nPor favor insira um valor valido.\n\n')
            continue
    
        response = menu_functions[user_input_choice]()
        handle_data(response, type(response))
        print('\nO que deseja fazer agora?\n')
