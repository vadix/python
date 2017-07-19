def make_album(artist_name, album_name, tracks_number = ''):
    if tracks_number:
        full_album = {'artist_name':artist_name, 'album_name':album_name, 'tracks_number':tracks_number}
    else:
        full_album = {'artist_name':artist_name, 'album_name':album_name}

    return full_album

while True:
    print("\nPlease tell me:")
    print("(enter 'q' at any time to quit)")

    artist_n = input("Artist name: ")
    if artist_n == 'q':
        break
    album_n = input("Album name: ")
    if album_n == 'q':
        break
    track_num = input("Tracks number: ")
    if track_num == 'q':
        break

# album = make_album('vadix', 'stone', '12')
# print(album)xc
# album = make_album('test', 'qa')
# print(album)

album = make_album(artist_n, album_n, track_num)
print(album)
