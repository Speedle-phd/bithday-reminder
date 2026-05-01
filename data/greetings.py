from random import choice
from typing import Callable, Any, TypedDict


class MessageEntry(TypedDict):
    function: Callable[[dict[str, Any], str], str]
    context: list[str]


def function1(person: dict[str, Any], username: str):
    _, lname, _, gender, *_ = person.values()
    return f"Guten Tag {"Mister" if gender == "male" else "Misses"} {lname}.\n\nZu deinem Jubeljubiläum wünsche ich dir all das tolle Zeug, was man sich halt so wünscht im Leben.\n\nHoffe du hast einen schönen Tag und du lässt dich gebührend feiern.\n\nLiebe Grüße und alles Liebe zum Geburtstag.\n\nWünscht dir {username}"


def function2(person: dict[str, Any], username: str):
    _, _, nickname, *_ = person.values()
    return f"Bleib immer schön artig, haben sie gesagt. Und du so: Klar, oftmals unartig, mal neuartig, mal andersartig, gelegentlich gutartig, immer mal wieder eigenartig, ganz selten mal bösartig, aber auf jeden Fall immer einzigartig! \n\nAlles Liebe zu deinem Geburtstag {nickname},\n\nWünscht dir {username}"


def function3(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Manch einer argumentiert, dass Zeit als Konzept gar nicht existiert. Sie sei nur ein Instrument, um Ordnung in die Welt zu bringen und den Prozessen eine weitere Dimension zu geben. So gesehen kann man kaum sagen, dass du älter geworden bist. Das was man sagen kann ist, dass du einfach noch toller geworden bist.\n\nAlles Liebe zum Geburtstag {fname},\n\nWünscht dir {username}"


def function4(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Wie schrecklich, dass an Geburstagen immer gleich ans Altern und an die Vergänglichkeit des Lebens gedacht werden muss. Dabei ist es doch schlussendlich einfach so, dass man eine weitere Sonnenumrundung mit all seinen Lieben verbringen durfte. Und jede weitere Umrumdung ist ein Geschenk und keine Last. Denn am Ende ist es nur wichtig, wie man die Zeit nutzt, die einem gegeben wurde und sich nicht von einer sinnlosen numerischen Größe einschüchtern lässt.\n\nAlles Liebe zum Geburtstag {fname},\n\nWünscht dir {username}"


def function5(person: dict[str, Any], username: str):
    _, lname, _, gender, _, _ = person.values()
    return f"Grüße Sie, werter Jubeljubilar, namentlich {"Mister" if gender == "male" else "Misses"} {lname}.\n\nZu Ihrem glorreichen, epischen und denkwürdigen Geburtstag wünsche ich ein weiteres Jahr voller packender Abenteuer, glückseligen Erlebnissen und verwüstungsresistenter Gesundheit.\n\nLiebe Grüße und alles Gute zum Geburtstag.\n\nWünscht Ihnen {username}"


def function6(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Ein weiteres Jahr ist um - manche würden sagen, du bist älter geworden. Ich sage: Du bist erfahrener, weiser und wahrscheinlich besser im Ausreden erfinden geworden. Das sind doch die wichtigen Lebenskompetenzen!\n\nAlles Liebe zum Geburtstag {fname},\n\nWünscht dir {username}"


def function7(person: dict[str, Any], username: str):
    _, _, nickname, *_ = person.values()
    return f"Herzlichen Glückwunsch, {nickname}! Du hast erfolgreich weitere 365 Tage überlebt, ohne dabei die Welt in Schutt und Asche zu legen. Das ist eine beachtliche Leistung in der heutigen Zeit!\n\nAlles Gute zum Geburtstag,\n\nWünscht dir {username}"


def function8(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Mathematisch betrachtet bist du heute exakt dort angelangt, wo du vor einem Jahr warst - nur mit 365 Tagen mehr Lebenserfahrung im Gepäck. Ob das nun Fortschritt oder Kreisbewegung ist, überlasse ich deiner philosophischen Interpretation, {fname}.\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function9(person: dict[str, Any], username: str):
    _, lname, _, gender, *_ = person.values()
    return f"Verehrte{"r" if gender == "male" else ""} {"Herr" if gender == "male" else "Frau"} {lname},\n\nheute ist der Tag, an dem wir Ihre erfolgreiche Erdumrundung feiern! Gratulation zu dieser astronautischen Meisterleistung. Die Schwerkraft scheint Ihnen nichts anhaben zu können.\n\nAlles Gute zum Geburtstag,\n\nWünscht Ihnen {username}"


def function10(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Liebe{"r" if person.get("gender") == "male" else ""} {fname},\n\nein Jahr älter bedeutet auch ein Jahr mehr Berechtigung, anderen gute Ratschläge zu geben, die sie gar nicht hören wollen. Nutze diese neue Superkraft weise!\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function11(person: dict[str, Any], username: str):
    _, _, nickname, *_ = person.values()
    return f"Hey {nickname}! Wusstest du, dass Geburtstage statistisch gesehen gesund sind? Menschen, die die meisten Geburtstage haben, leben am längsten. Das ist doch mal eine erfreuliche Wissenschaft!\n\nAlles Gute zum Geburtstag,\n\nWünscht dir {username}"


def function12(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Herzlichen Glückwunsch, {fname}! Du hast ein weiteres Lebensjahr gemeistert, ohne dass die Welt untergegangen ist. Das ist entweder ein Zeichen deiner Harmlosigkeit oder deiner außergewöhnlichen Selbstbeherrschung.\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function13(person: dict[str, Any], username: str):
    _, lname, *_ = person.values()
    return f"Werter {lname}-Clan Angehörige{"r" if person.get("gender") == "male" else ""},\n\nheute feiern wir den Tag, an dem du beschlossen hast, diesem Planeten beizutreten. Eine Entscheidung, die du bisher - soweit erkennbar - nicht bereut hast.\n\nAlles Gute zum Geburtstag,\n\nWünscht dir {username}"


def function14(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Philosophisch betrachtet, {fname}, ist jeder Geburtstag ein kleines Wunder: Du warst schon mal jünger und wirst nie wieder so jung sein wie heute. Genieße also diesen einmaligen Moment der optimalen Jugendlichkeit!\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function15(person: dict[str, Any], username: str):
    _, _, nickname, *_ = person.values()
    return f"Liebe{"r" if person.get("gender") == "male" else ""} {nickname},\n\nGratulation! Du hast ein weiteres Jahr erfolgreich absolviert, ohne dabei von einem Meteoriten getroffen zu werden. Bei der aktuellen Raumschrott-Situation ist das wirklich bemerkenswert.\n\nAlles Gute zum Geburtstag,\n\nWünscht dir {username}"


def function16(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Ein Toast auf dich, {fname}! Mögest du auch im nächsten Lebensjahr die wunderbare Gabe behalten, älter zu werden, ohne erwachsen zu werden. Das ist eine Kunst, die nur wenige beherrschen.\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function17(person: dict[str, Any], username: str):
    _, lname, _, gender, *_ = person.values()
    return f"Geschätzte{"r" if gender == "male" else ""} {"Herr" if gender == "male" else "Frau"} {lname},\n\nSie haben ein weiteres Jahr Lebenserfahrung gesammelt! Diese können Sie nun wie eine Sammlung seltener Briefmarken horten oder großzügig an Jüngere weitergeben, die sie gar nicht haben wollen.\n\nAlles Gute zum Geburtstag,\n\nWünscht Ihnen {username}"


def function18(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Herzlichen Glückwunsch, {fname}! Du bist jetzt offiziell berechtigt, Sätze mit 'Früher war alles besser' zu beginnen. Nutze diese neue Macht verantwortungsvoll!\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function19(person: dict[str, Any], username: str):
    _, _, nickname, *_ = person.values()
    return f"Hey {nickname}! Ein weiteres Jahr voller Erinnerungen liegt hinter dir - manche davon kannst du dich sogar noch daran erinnern! Das ist doch schon mal ein Erfolg.\n\nAlles Gute zum Geburtstag,\n\nWünscht dir {username}"


def function20(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Liebe{"r" if person.get("gender") == "male" else ""} {fname},\n\nein Geburtstag ist wie ein persönlicher Neujahrstag - nur mit besserer Musik und ohne die Verpflichtung, unrealistische Vorsätze zu fassen. Viel entspannter also!\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function21(person: dict[str, Any], username: str):
    _, lname, *_ = person.values()
    return f"Verehrte Familie {lname},\n\nheute feiert ein{"" if person.get("gender") == "male" else "e"} Ihrer Angehörigen den erfolgreichen Abschluss eines weiteren Lebensjahres. Gratulation zu diesem familiären Erfolg!\n\nAlles Gute zum Geburtstag,\n\nWünscht {username}"


def function22(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Wissenschaftlich erwiesen: Menschen, die Geburtstag haben, sind statistisch glücklicher als Menschen, die keinen haben. Du gehörst also heute zur privilegierten Gruppe, {fname}!\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function23(person: dict[str, Any], username: str):
    _, _, nickname, *_ = person.values()
    return f"Herzlichen Glückwunsch, {nickname}! Du hast ein weiteres Jahr erfolgreich überlebt, ohne dabei die Gesetze der Physik zu brechen. Das zeigt bemerkenswerte Disziplin!\n\nAlles Gute zum Geburtstag,\n\nWünscht dir {username}"


def function24(person: dict[str, Any], username: str):
    fname, *_ = person.values()
    return f"Ein weiterer Beweis, dass die Zeit relativ ist, {fname}: Für manche fühlt sich ein Jahr an wie eine Ewigkeit, für andere wie ein Augenblick. Du scheinst zur letzteren Kategorie zu gehören - das ist ein gutes Zeichen!\n\nAlles Liebe zum Geburtstag,\n\nWünscht dir {username}"


def function25(person: dict[str, Any], username: str):
    _, lname, _, gender, *_ = person.values()
    return f"Hochverehrte{"r" if gender == "male" else ""} {"Herr" if gender == "male" else "Frau"} {lname},\n\nSie haben ein weiteres Jahr gemeistert, ohne dabei die Erdrotation zu beeinträchtigen. Das ist eine beachtliche Leistung, die zu wenig gewürdigt wird!\n\nAlles Gute zum Geburtstag,\n\nWünscht Ihnen {username}"


MESSAGES_LIST: list[MessageEntry] = [
    {"function": function1, "context": ["all"]},
    {"function": function2, "context": ["all"]},
    {"function": function3, "context": ["all"]},
    {"function": function4, "context": ["all"]},
    {"function": function5, "context": ["all"]},
    {"function": function6, "context": ["all"]},
    {"function": function7, "context": ["all"]},
    {"function": function8, "context": ["all"]},
    {"function": function9, "context": ["all"]},
    {"function": function10, "context": ["all"]},
    {"function": function11, "context": ["all"]},
    {"function": function12, "context": ["all"]},
    {"function": function13, "context": ["all"]},
    {"function": function14, "context": ["all"]},
    {"function": function15, "context": ["all"]},
    {"function": function16, "context": ["all"]},
    {"function": function17, "context": ["all"]},
    {"function": function18, "context": ["all"]},
    {"function": function19, "context": ["all"]},
    {"function": function20, "context": ["all"]},
    {"function": function21, "context": ["all"]},
    {"function": function22, "context": ["all"]},
    {"function": function23, "context": ["all"]},
    {"function": function24, "context": ["all"]},
    {"function": function25, "context": ["all"]},
]


def choose_message(person: dict[str, Any], username: str) -> str:
    context = person["context"]

    MESSAGE_LIST = [
        message["function"]
        for message in MESSAGES_LIST
        if context in message["context"] or "all" in message["context"]
    ]
    print(len(MESSAGE_LIST))

    return choice(MESSAGE_LIST)(person, username)
