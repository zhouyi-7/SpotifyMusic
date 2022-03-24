from lyricsgenius import Genius

def get_song_lyrics(genius, artist, song):
    
    """Returns the lyrics of a song given the song name and the artist name"""
    
    try:
        song = genius.search_song(artist=artist, title=song)
        return song.lyrics
                
    except Exception as e:
        return "Error " + str(e)
        


        
    

