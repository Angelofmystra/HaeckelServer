from worldbuilder.models import Character

def make_character(username, password, conn):
    c = Character(
    name=username,
    desc="",
    user=username,
    connection=conn,
    role="",
    rooms=1,
    title="the fresh meat",
    alignmnet="TN",
    maxHealth=1,
    currentHealth=1,
    ac=10,
    fort=0,
    ref=0,
    will=0,
    spot=0,
    listen=0,
    newOrNot=True,
    ).save()
    return "blah"
