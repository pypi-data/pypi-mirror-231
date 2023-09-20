from typing import List
from dataclasses import dataclass, field


import spotipy
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyOAuth


from spotidl import exceptions, utils


# initializing the spotify api connection
# the OAuth object automatically reads valid env. variables so we don't need to
# manually assign them using `os.environ.get(<env_var name>)`
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

except spotipy.oauth2.SpotifyOauthError as ex:
    raise exceptions.EnvVariablesError(ex)


# defining structure for the song data we are going to get
@dataclass
class SpotifySong:
    """
    Stores data for the song fetched from Spotify.
    """

    name: str = "Unknown Song"
    # this generates a list with an unknown artist default
    artists: list = field(default_factory=lambda: ["Unknown Artist"])
    album_name: str = "Unknown Album"
    disc_number: int = 1
    track_number: int = 1
    cover_url: str = ""

    def __str__(self):
        return utils.make_song_title(self.artists, self.name, ", ")


def get_song_data(link: str) -> SpotifySong:
    """
    Gets relevant song details for the given Spotify song link.
    These are then passed onto other functions for further processing.
    """

    try:
        query = sp.track(link)

    except SpotifyException as exception:
        # wrapping the Spotify Exception
        # still unsure whether this is the correct approach
        raise exceptions.NoDataReceivedError(exception)

    else:
        # there can be multiple results,
        # iterating over the list and extracting data
        artists = []
        for artist in query["artists"]:
            artists.append(artist["name"])

        song = new_song(query, type_="song")

        return song


# this will serve as the common point for all entry types
# (individual song link, album link, etc.)
def new_song(query: dict, type_: str, **album_details) -> SpotifySong:
    """
    Makes a new SpotifySong given a raw "track" type item received from Spotify API.
    The track queried using different methods returns slightly modified data.
    """

    artists = []
    for artist in query["artists"]:
        artists.append(artist["name"])

    name = utils.correct_name(query["name"])

    if type_ == "song":
        album_name = utils.correct_name(query["album"]["name"])
        # "song" refers to the case where the user enters a song link; we need
        # to fetch data for just a single song
        song = SpotifySong(
            name=name,
            artists=artists,
            album_name=album_name,
            disc_number=query["disc_number"],
            track_number=query["track_number"],
            # the 1st link contains a link to the album art
            # of size 640 x 640 pixels
            cover_url=query["album"]["images"][0]["url"],
        )

    elif type_ == "album":
        song = SpotifySong(
            name=name,
            artists=artists,
            album_name=album_details["album_name"],
            disc_number=query["disc_number"],
            track_number=query["track_number"],
            cover_url=album_details["album_cover_url"],
        )

    return song


def get_album_data(link: str) -> tuple:
    """
    Gets album data for the given Spotify album link.
    It is then passed onto other functions for further processing.
    """

    # since our main data(all the relevant metadata, song URL) is associated
    # with the spotify song(referred to as "Track" in the spotify api), we
    # will need to make a list of all the songs in the album and then pass on
    # that list onto other functions.
    try:
        query = sp.album(link)

    except SpotifyException as exception:
        raise exceptions.NoDataReceivedError(exception)

    else:
        album: List[SpotifySong] = []
        album_name = utils.correct_name(query["name"])

        for track in query["tracks"]["items"]:
            # since this time we are directly receiving data that we otherwise
            # extracted from get_song_data using a link entered by the user, we
            # will need to generate a SpotifySong object another way

            song = new_song(
                track,
                type_="album",
                album_name=album_name,
                album_cover_url=query["images"][0]["url"],
            )

            album.append(song)

        # returning album name since we'll need it when making the album folder to
        # use as the save directory
        return (album_name, album)


def get_playlist_data(link: str) -> tuple:
    """
    Gets playlist data for the given Spotify playlist link.
    It is then passed onto other functions for further processing.
    """

    # we need playlist id to fetch its information
    playlist_id = utils.get_playlist_id(link)

    try:
        query = sp.playlist_tracks(playlist_id)
        playlist_name = sp.playlist(playlist_id)["name"]

    except SpotifyException as exception:
        raise exceptions.NoDataReceivedError(exception)

    else:
        # can fetch a 100 tracks at a time
        # the "next" dictionary key gets the next batch, if the no. of results
        # exceeds 100
        tracks = query["items"]

        while query["next"]:
            query = sp.next(query)
            tracks.extend(query["items"])

        # now, to extract data from each entry in the list and get a SpotifySong object
        playlist_songs: List[SpotifySong] = []

        for track in tracks:
            song = new_song(track["track"], type_="song")

            playlist_songs.append(song)

        return playlist_name, playlist_songs
