from random import randrange

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
result = []


def get_jokes(repeat=True, times=1):
    for i in range(times):
        nouns_r, adverbs_r, adjectives_r = randrange(len(nouns)),\
                                           randrange(len(adverbs)),\
                                           randrange(len(adjectives))
        if not repeat:
            result.append(nouns.pop(nouns_r) + ' ' + adverbs.pop(adverbs_r) + ' ' + adjectives.pop(adjectives_r))
        else:
            result.extend([nouns[nouns_r] + ' ' + adverbs[adverbs_r] + ' ' + adjectives[adjectives_r]])
    print(result)


get_jokes(False, 5)
