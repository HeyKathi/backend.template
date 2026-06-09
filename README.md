# Abgabe: Dokumentation XML-Export

## Funktionsaufrufe / Ablauf

1. Im Frontend wird der Export-Button gedrückt.
2. Der Browser macht einen Aufruf an `GET /export/xml`.
3. Die Backend-Route `export_xml()` in `backend/api/_routes.py` wird ausgeführt.
4. `export_xml()` bekommt die Datenbank-Verbindung über `get_db()`.
5. Dann ruft `export_xml()` `export_games_to_xml(db)` aus `backend/crud/_crud.py` auf.
6. `export_games_to_xml(db)` liest alle Zeilen aus der Tabelle `games`.
7. Aus den Daten wird ein XML-Dokument gebaut.
8. Das XML wird als Datei an den Browser gesendet.

## XML-Struktur

Die XML-Datei hat diese Struktur:

- `<tictactoe_export>`
  - `<metadata>`
    - `<export_date>`
    - `<application>`
    - `<version>`
  - `<games>`
    - `<game id="...">`
      - `<board>`
      - `<current_player>`
      - `<status>`
      - `<created_at>`
      - `<board_visualization>`
        - `<row number="...">`
          - `<cell position="..." column="...">`

### Verbindung zur Datenbank

Die Tabelle `games` hat diese Spalten:
- `id`
- `board`
- `current_player`
- `status`
- `created_at`

Im XML steht:
- `id` als `game`-Attribut
- `board` als `<board>`
- `current_player` als `<current_player>`
- `status` als `<status>`
- `created_at` als `<created_at>` (ISO-Format, z.B. 2026-06-09T14:30:45.123456)

Die 9 Zeichen von `board` werden zusätzlich in `<board_visualization>` als 3 Reihen aufgeteilt.

Das Datum `created_at` wird automatisch beim Erstellen eines Spiels gespeichert.

## Exportierte Datei

Die echte Export-Datei heißt:
- `tictactoe-export.xml`

Diese Datei wurde aus den echten Daten der vorhandenen Datenbank erstellt.

## Starten (Backend)

1. Virtuelle Umgebung erstellen und aktivieren:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Abhängigkeiten installieren:

```powershell
pip install -r requirements.txt
```

3. Backend starten (Uvicorn):

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. API-Endpunkte:

- Swagger UI: `http://localhost:8000/docs`
- XML-Export: `GET http://localhost:8000/export/xml` (oder im Browser `http://localhost:8000/export/xml`)

