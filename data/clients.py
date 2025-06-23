from dataclasses import dataclass


@dataclass
class Client:
    first_name: str
    last_name: str
    postal_code: str


test_user1 = Client(
    first_name='John',
    last_name='Wick',
    postal_code='454000'
)

test_user2 = Client(
    first_name='Anakin',
    last_name='Skywalker',
    postal_code='196158'
)


