from cleaner_api import api

for s in '100 move -90 turn soap set start 50 move stop'.split(' '):
    api.make(s)