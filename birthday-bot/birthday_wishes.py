import random


def select_birthday_wish():
    birthday_wishes = ['Forget the past, forget the future and please forget the present too because I forgot to get you one.',
                       'Another year closer to getting those senior citizen seats on the bus!',
                       'Perhaps a glass of wine? They say it gets better with age.',
                       'I wanted to get you something to remind you of your youth, but they were sold out of dinosaur bones.',
                       'Ahhh, one day closer to your inevitable end!',
                       "Another year older, another year wiser. That's what they say, at least.",
                       "Finally, I thought you'd never be legal!",
                       ]

    selector = random.randint(0, len(birthday_wishes)-1)
    return birthday_wishes[selector]
