from random import choice
from typing import Callable




def function1(person: dict[str:str]):
    _, lname, _, gender, *_ = person.values()
    return f"Guten Tag {"Mister" if gender == "male" else "Misses"} {lname}.\n\nZu deinem Jubeljubiläum wünsche ich dir all das tolle Zeug, was man sich halt so wünscht im Leben.\n\nHoffe du hast einen schönen Tag und du lässt dich gebührend feiern.\n\nLiebe Grüße und alles Liebe zum Geburtstag.\n\nWünscht dir Emanuel"


def function2(person: dict[str:str]):
    _, _, nickname, *_ = person.values()
    return f"Bleib immer schön artig, haben sie gesagt. Und du so: Klar, oftmals unartig, mal neuartig, mal andersartig, gelegentlich gutartig, immer mal wieder eigenartig, ganz selten mal bösartig, aber auf jeden Fall immer einzigartig! \n\nAlles Liebe zu deinem Geburtstag {nickname},\n\nWünscht dir Emanuel"


def function3(person: dict[str:str]):
    fname, *_ = person.values()
    return f"Manch einer argumentiert, dass Zeit als Konzept gar nicht existiert. Sie sei nur ein Instrument, um Ordnung in die Welt zu bringen und den Prozessen eine weitere Dimension zu geben. So gesehen kann man kaum sagen, dass du älter geworden bist. Das was man sagen kann ist, dass du einfach noch toller geworden bist.\n\nAlles Liebe zum Geburtstag {fname},\n\nWünscht dir Emanuel"


def function4(person: dict[str:str]):
    fname, *_ = person.values()
    return f"Wie schrecklich, dass an Geburstagen immer gleich ans Altern und an die Vergänglichkeit des Lebens gedacht werden muss. Dabei ist es doch schlussendlich einfach so, dass man eine weitere Sonnenumrundung mit all seinen Lieben verbringen durfte. Und jede weitere Umrumdung ist ein Geschenk und keine Last. Denn am Ende ist es nur wichtig, wie man die Zeit nutzt, die einem gegeben wurde und sich nicht von einer sinnlosen numerischen Größe einschüchtern lässt.\n\nAlles Liebe zum Geburtstag {fname},\n\nWünscht dir Emanuel"


def function5(person: dict[str:str]):
    _, lname, _, gender, _, _ = person.values()
    return f"Grüße Sie, werter Jubeljubilar, namentlich {"Mister" if gender == "male" else "Misses"} {lname}.\n\nZu Ihrem glorreichen, epischen und denkwürdigen Geburtstag wünsche ich ein weiteres Jahr voller packender Abenteuer, glückseligen Erlebnissen und verwüstungsresistenter Gesundheit.\n\nLiebe Grüße und alles Gute zum Geburtstag.\n\nWünscht Ihnen Emanuel"


# def function6(person: dict[str:str]):
#     fname, lname, nickname, gender, birthday, context = person.values()
#     return f"6"


MESSAGES_LIST: list[dict[str:Callable | list[str]]] = [
    {"function": function1, "context": ["all"]},
    {"function": function2, "context": ["all"]},
    {"function": function3, "context": ["all"]},
    {"function": function4, "context": ["all"]},
    {"function": function5, "context": ["all"]},
    # {"function": function6, "context": ["all"]},
]

def choose_message(person: dict[str:str]) -> str:
    context = person["context"]
    
    MESSAGE_LIST = [message["function"] for message in MESSAGES_LIST if context in message["context"] or "all" in message["context"]]
    print(len(MESSAGE_LIST))
    
    return choice(MESSAGE_LIST)(person)
