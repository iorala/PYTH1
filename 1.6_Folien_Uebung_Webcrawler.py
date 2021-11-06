# Übung: WebCrawlerSchreiben sie ein Programm, dass:
# eine Web URL entgegennimmt und
# anschliessend ausgibt, wie viele Wort auf der entsprechenden Webseite vorkommen.
# Erweitern sie ihr Programm, sodass es erneute nach der URL fragt, wenn eine URL nicht geöffnet werden konnte.

from urllib.request import urlopen
with urlopen("http://www.fhgr.ch") as source:
    print(len(source.read().decode('utf-8').split()))