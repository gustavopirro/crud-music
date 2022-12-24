from model.Music import Music
from datetime import date

def add_music():
    music_name = input('Insira o nome da música:\n')
    music_artist = input('Insira o nome do artista:\n')

    try:
        music_year_of_publication = int(input('Insira o ano de publicação da música:\n'))
    except ValueError:
        print('Data invalida!')
        return

    normalized_year = date(music_year_of_publication, 1, 1).strftime('%d-%m-%Y')
    music = Music(music_name, music_artist, normalized_year).save()
    return music

def search_music():
    music_name = str(input('Insira o nome da música:\n'))
    return Music().get(music_name)

def filter_musics_by_year():
    pass

def get_musics():
    return Music().all()

def stop_cli():
    print('Obrigado e volte sempre!')
    exit()