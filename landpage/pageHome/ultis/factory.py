from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def depoimentos():
    return {
        'description': fake.sentence(nb_words=20),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/paris,girl/all' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(depoimentos())