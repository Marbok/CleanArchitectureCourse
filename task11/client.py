from cleaner_api import *

init() \
    .bind(move(100)) \
    .bind(turn(50)) \
    .bind(set('soap')) \
    .bind(start())
