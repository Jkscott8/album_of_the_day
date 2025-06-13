from string import capwords
import pandas as pd
import random
import datetime as dt


album_df = pd.read_csv('top500albums.csv', quotechar='"')
ranking = pd.read_csv('AlbumRankings.csv')
marys_ranking = pd.read_csv('Marys_AlbumRankings.csv')
albums_listened = pd.read_csv('albumslistened.csv')


def todaysAlbum(date):
    global albums_listened
    if date not in albums_listened['date'].values:
        print('Finding album...')
        while True:
            rand = random.randint(0, len(album_df)-1)
            aod = album_df.iloc[rand]
            album_name = aod['album']
            if album_name not in albums_listened['album'].values:
                new_entry = pd.DataFrame({'date': [date], 'album': [album_name]})
                albums_listened = pd.concat([albums_listened, new_entry], ignore_index=True)
                albums_listened.to_csv('albumslistened.csv', index=False)
                print("Today's Album is: " + capwords(str(aod['album'])) + ' by ' + capwords(str(aod['artist'])) + ' Rank: ' + str(rand + 1))
                return
    else:
        print('Todays Album: ')
        return print(capwords(albums_listened.loc[albums_listened['date']==date,'album'][0]))

def album_raking(album,score,artist=None, genre=None):
    global ranking
    if artist is not None and genre is not None:
        new_entry = pd.DataFrame({'album': album, 'artist': [artist], 'genre': [genre], 'score': [score]})
        ranking = pd.concat([ranking, new_entry], ignore_index=True)
        ranking.to_csv('AlbumRankings.csv', index=False)
        print(ranking.sort_values(by='score', ascending=False))
        return
    album_info = album_df.loc[album_df['album'] == album]
    if not album_info.empty:
        artist = album_info['artist'].values[0]
        genre = album_info['genre'].values[0]
        new_entry = pd.DataFrame({'album': album, 'artist': [artist], 'genre':[genre], 'score': [score]})
        ranking = pd.concat([ranking, new_entry], ignore_index=True)
        ranking.to_csv('AlbumRankings.csv', index=False)
    else:
        print('Album Not Found')
    print(ranking.sort_values(by='score', ascending=False))
    return None

def marys_album_raking(album,score,artist=None, genre=None):
    global marys_ranking
    if artist is not None and genre is not None:
        new_entry = pd.DataFrame({'album': album, 'artist': [artist], 'genre': [genre], 'score': [score]})
        marys_ranking = pd.concat([marys_ranking, new_entry], ignore_index=True)
        marys_ranking.to_csv('Marys_AlbumRankings.csv', index=False)
        print(marys_ranking.sort_values(by='score', ascending=False))
        return
    album_info = album_df.loc[album_df['album'] == album]
    if not album_info.empty:
        artist = album_info['artist'].values[0]
        genre = album_info['genre'].values[0]
        new_entry = pd.DataFrame({'album': album, 'artist': [artist], 'genre':[genre], 'score': [score]})
        ranking = pd.concat([marys_ranking, new_entry], ignore_index=True)
        ranking.to_csv('Marys_AlbumRankings.csv', index=False)
    else:
        print('Album Not Found')
    print(marys_ranking.sort_values(by='score', ascending=False))
    return None


todaysAlbum(str(dt.date.today()))
#album_raking('exile on main street', 22)
#marys_album_raking('the bends', 60)