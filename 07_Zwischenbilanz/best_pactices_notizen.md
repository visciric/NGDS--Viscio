# Genauigkeit

- Vertrauenswürdige Bibliotheken/Packages verwenden
- Tests für alle Möglichkeiten inkl. Grenzfälle (Edge Cases)
  - Vergleiche mit analytischen Lösungen
  - Vergleiche mit Standardbibliotheken
  - Tests auf allen Ebenen (Unit, Integration, System)
- Variablendeklarationen (z.B. `int` vs. `float`)
- Fehlerbehandlung
- Maschinenpräzision beachten (Teilen und Subtrahieren)


# Effizienz

- Keine Wiederholungen (caching, memoization)
- Vektorisierung (z.B. `numpy`, map, filter, reduce)
- Parallelisierung (z.B. `multiprocessing.Pool`)
- wenig Zugriffe auf IO (Dateisystem, Datenbank, Netzwerk, Console, etc.)


# Modularität / Wiederverwendbarkeit

- Aufteilen nach einzelnen Aufgaben (Single Responsibility Principle)
- Delegation
- Verallgemeinerung


# Verständlichkeit / Wartbarkeit

- Dokumentation 
- Storyline / klarer Aufbau
- ähnliche Funktionen zusammen in ein Modul
- Sinnvolle Variablennamen
- Code Conventions
- Klare und konsistente Interfaces / Signaturen
    - `f(x: float, y:float, n_steps:int) -> np.ndarray`
    - `g(x: float, y:float, tol:float) -> np.ndarray`
