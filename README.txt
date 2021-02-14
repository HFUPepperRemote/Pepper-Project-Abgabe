Corona Info Terminal V1.0 Abgabe: 14.02.21, Hochschule Furtwangen, Masterstudiengang MOS an der Fakultät Informatik. Betreuer: Dr. Elmar Cochlovius. Martin Kramer Ersteller: Vasiliy Seibert.

Für detailierte Informationen: siehe Dokumentation
Kontakt: vasiliy.sviyazov@hs-furtwangen.de.

Installationsanweisung:

1)Stelle sicher, dass der Entwicklungsrechner und Pepper mit dem selben Netzwerk verbunden sind.
2) Öffne ein Tool für die FTP übertragung (z.b Filezilla link zum Download in der Doku)
3) Python Skript auf dem Unix Verzeichnis ablegen (z.b. [/data/home/nao/deineApplikaiton] )
4) Webinhalte auf dem nginx Server ablegen (z.b [/data/home/nao/.local/share/PackageManager/apps/deineApplikation/html])
Stelle eine SSH Verbindung zum Pepper System her.
führe das Python Skript auf dem Roboter aus -> python deineApplikation.py -EVTLparameter



Note: Beachte, dass die Verknüpfung vom Python Skript zu den Webinhalten in dem Python Skript definiert sein muss: siehe auch: Dokumentation.