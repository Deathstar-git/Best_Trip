import random

from django import template
from MainApp.models import *

register = template.Library()


@register.filter
def next(some_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) + 1]  # access the next element
    except:
        return some_list[0]  # return empty string in case of exception


@register.filter
def previous(some_list, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) - 1]  # access the previous element
    except:
        return some_list[len(some_list) - 1]  # return empty string in case of exception


@register.simple_tag()
def get_rand_img_url(url):
    return url + "?" + str(random.randint(10, 10000))


@register.simple_tag()
def get_account_avatar(user_id):
    try:
        acc = Account.objects.get(user_id=user_id)
        return acc.avatar.url
    except:
        return ''
# @register.inclusion_tag('main/list_playlists.html')
# def show_playlists(curr_id=1):
#     pl = Playlist.objects.all()
#     return {'pl': pl, 'curr_id': curr_id}
#
#
# @register.simple_tag()
# def get_songs_info(pl_id):
#     songs = Song.objects.filter(playlist__pk=pl_id)
#     artist_names = []
#     song_names = []
#     song_urls = []
#     cover_urls = []
#     songs_id = []
#     for s in songs:
#         song_names.append(str(s.name))
#         song_urls.append("/media/" + str(s.link))
#         cover_urls.append("/media/" + str(s.icon))
#         songs_id.append(str(s.pk))
#     artists = Artist.objects.filter(song__in=songs_id)
#     for a in artists:
#         artist_names.append(str(a.name))
#     return {'artists': artist_names, 'songs': song_names,
#             'songs_urls': song_urls, 'cover_urls': cover_urls,
#             'songs_id': songs_id}
#
#
# @register.simple_tag()
# def get_artist_by_song_name(song_id):
#     song = Song.objects.get(pk=song_id)
#     artist = list(Artist.objects.filter(song__pk=song.pk).values())
#     return artist[0]['name']
