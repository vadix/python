def make_album(artist_name, album_name, tracks_number = ''):
    if tracks_number:
        full_album = {'artist_name':artist_name, 'album_name':album_name, 'tracks_number':tracks_number}
    else:
        full_album = {'artist_name':artist_name, 'album_name':album_name}

    return full_album

album = make_album('vadix', 'stone', '12')
print(album)
album = make_album('test', 'qa')
print(album)

