---
title: Benutzer verwalten
---

## Benutzer anlegen

**Voraussetzungen:**  
Sie sind als IAM Administrator im Admin-Portal angemeldet.  

**Schritte**  


1.  Klicken Sie die **Benutzer**-Kachel unter **Verwaltung Benutzer & Gruppen**.  
Die Benutzerauswahl öffnet sich.  
1.  Klicken Sie **Hinzufügen**.  
1.  Wählen Sie eine Benutzer-Vorlage entsprechend dem benötigten Benutzertyp und klicken Sie **Weiter**:  
    - openDesk Admin  
    - openDesk User  
1.  Geben Sie die benötigten Stammdaten (Vorname, Nachname etc.) ein und klicken Sie **Weiter**.  
**Hinweis**  
Der Wert des **Benutzernamens** (Anzeigename für den Account):  
    -   darf nicht identisch mit einem anderen Benutzernamen sein
    -   darf nur Ziffern, Buchstaben, Punkte, Bindestriche, oder Unterstriche enthalten
    -   muss mindestens 2 Zeichen lang sein
    -   muss mit einer Ziffer oder einem Buchstaben beginnen und enden
    -   darf nicht "admin" sein. 
1.  Geben Sie die E-Mail-Adresse des Benutzers ein und klicken Sie **Benutzer erstellen**.  
Der Benutzer wird im System erstellt. Die Person erhält per E-Mail einen Einladungslink des Portals.


:::tip[Gut zu wissen]
Das Passwort setzt die Person selbst.  
Die Liste der angelegten Personen wird über die Suche angezeigt:Klicken Sie auf das **Lupensymbol** im Feld **Suche Benutzer**.  
Die Benutzer-Vorlage kann nachträglich nicht geändert werden.  
Der Benutzerzugang als IAM Administrator (Benutzer-Vorlage openDesk Admin) wird jeweils zusätzlich zum normalen Benutzerzugang (Benutzer-Vorlage openDesk User) angelegt und kann aus Gründen der Sicherheit ausschließlich für Tätigkeiten auf dem openDesk Admin-Portal verwendet werden.
:::

Die Anlage vieler Personen, die in einem anderen System bereits vorhanden sind, kann über ein Import-Tool erfolgen.


## Benutzer ändern

**Voraussetzungen:**  
Sie sind als IAM Administrator im Admin-Portal angemeldet.  

**Schritte**  
1.  Klicken Sie die **Benutzer**-Kachel unter **Verwaltung Benutzer & Gruppen**.  
Die Benutzerauswahl öffnet sich.  
1.  Klicken Sie auf das **Lupensymbol"** im Feld **Suche Benutzer**.  
Die Liste der im System vorhandenen Benutzer wird angezeigt.  
1.  Wählen Sie einen Benutzer, um die Personendaten zu aktualisieren. Verwenden Sie ggf. die Suche. Die Eingabemaske wird angezeigt.  
1.  Aktualisieren Sie die Benutzerdaten und klicken Sie **Speichern**.  
  
Die Daten werden aktualisiert. Die Eingabemaske wird geschlossen und die Liste der im System vorhandenen Benutzer wird angezeigt.


:::tip[Did you know?]

Das Passwort setzt die Person selbst.  
Der Wert des **Benutzernamens** (Anzeigename für den Account):  
-   darf nicht identisch mit einem anderen Benutzernamen sein
-   darf nur Ziffern, Buchstaben, Punkte, Bindestriche, oder Unterstriche enthalten
-   muss mindestens 2 Zeichen lang sein
-   muss mit einer Ziffer oder einem Buchstaben beginnen und enden
-   darf nicht "admin" sein. 

:::

## Benutzer löschen
xxx was hat ers mit den zugehörigen Objekten auf sich? und was ist noch mit dem Löschen verbunden (physikalisches vs. logisches Löschen)  
Gibt es irgendwelche Löschregeln und Compliance-Vorgaben? Was macht eine Benutzerlöschung mit der Historie von irgendwelchen Vorgängen und Dokumenten?
Werden User-Aktionen irgendwo getrackt, z.B. Admin-Aktionen geloggt?  



**Voraussetzungen:**  
Sie sind als IAM Administrator im Admin-Portal angemeldet.  

**Schritte**  

1.  Klicken Sie die **Benutzer**-Kachel unter **Verwaltung Benutzer & Gruppen**.  
Die Benutzerauswahl öffnet sich.  

1. Klicken Sie den gewünschten Benutzer in der Liste an.  
**Tipp:**  
Verwenden Sie ggf. die Suche, um die Liste der Benutzer zu filtern.

1. Klicken Sie **Löschen**.  
Die Bestätigungsanfrage **Objekte löschen** öffnet sich.

1.  Bestätigen Sie mit **Löschen**.  
Achten Sie darauf, dass das Häkchen bei **Zugehörige Objekte löschen** gesetzt ist.
Der Benutzer wird im System gelöscht.


:::tip[Did you know?]
Die Liste der angelegten Personen wird über die Suche angezeigt: Klicken Sie auf das **Lupensymbol** im Feld **Suche Benutzer**.
:::


## Weitere Anwendungsfälle

### 2 FA einrichten

**Voraussetzungen:**  
Sie sind als IAM Administrator im Admin-Portal angemeldet.  

**Schritte**  

1.  Klicken Sie die **Benutzer**-Kachel unter **Verwaltung Benutzer & Gruppen**.  
Die Benutzerauswahl öffnet sich.  
1.  Klicken Sie auf das **Lupensymbol"** im Feld **Suche Benutzer**.  
Die Liste der im System vorhandenen Benutzer wird angezeigt.  
1.  Wählen Sie einen Benutzer, um die Personendaten zu aktualisieren. Verwenden Sie ggf. die Suche.Die Eingabemaske wird angezeigt.  
1.  Aktualisieren Sie die Benutzerdaten und klicken Sie **Speichern**.  
  
Die Daten werden aktualisiert.Die Eingabemaske wird geschlossen und die Liste der im System vorhandenen Benutzer wird angezeigt.


:::tip[Did you know?]
Das Passwort setzt die Person selbst.  
Der Wert des **Benutzernamens** (Anzeigename für den Account):  
-   darf nicht identisch mit einem anderen Benutzernamen sein
-   darf nur Ziffern, Buchstaben, Punkte, Bindestriche, oder Unterstriche enthalten
-   muss mindestens 2 Zeichen lang sein
-   muss mit einer Ziffer oder einem Buchstaben beginnen und enden
-   darf nicht "admin" sein. 
:::

### Administration der openDesk Anwendungen
Die openDesk Anwendungen haben eigene, integrierte Administrationsoberflächen.  
Sie benötigen dafür die Administrator-Rechte gemäß [Benutzereinstellungen openDesk](benutzerrechte)
