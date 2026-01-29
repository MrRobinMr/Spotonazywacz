# Spotonazywacz

![Project Preview](preview.png)

Spotonazywacz to inteligentne narzędzie w języku Python służące do pobierania i zarządzania plikami muzycznymi. Program automatycznie dba o poprawne metadane oraz przejrzyste nazewnictwo Twojej biblioteki audio.

## Dlaczego Spotonazywacz?

Projekt został zaprojektowany tak, aby maksymalnie uprościć proces przygotowania środowiska. Dzięki zintegrowanemu skryptowi instalacyjnemu, nie musisz ręcznie konfigurować bibliotek ani pobierać zewnętrznych narzędzi takich jak FFmpeg – program zrobi to za Ciebie.

## Wymagania

* **System operacyjny:** Windows (wymagany do działania skryptu instalacyjnego .ps1)
* **Python:** wersja 3.10 lub nowsza
* **Uprawnienia:** Możliwość uruchamiania skryptów PowerShell (Set-ExecutionPolicy)

## Szybki Start (Instalacja)

Aby uruchomić projekt po raz pierwszy, wykonaj poniższe kroki:

1. **Uruchom instalator:**
   Znajdź plik `install.ps1` w głównym folderze projektu. Kliknij go prawym przyciskiem myszy i wybierz **"Uruchom z PowerShell"** (Run with PowerShell).
   
   *Skrypt automatycznie:*
   * Utworzy środowisko wirtualne (venv).
   * Zainstaluje wymagane biblioteki Python.
   * Pobierze i wypakuje oficjalne pliki binarne **FFmpeg**.
   * Doda FFmpeg do zmiennych środowiskowych Twojego systemu.

2. **Uruchom program:**
   Po zakończeniu instalacji, otwórz terminal w folderze projektu i wpisz:
   **python main.py**

## Rozwiązywanie problemów

* **Błąd uprawnień PowerShell:** Jeśli system blokuje skrypt, otwórz PowerShell jako Administrator i wpisz: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`, a następnie spróbuj ponownie uruchomić instalator.
* **Odświeżenie ścieżek:** Jeśli po instalacji system nadal nie "widzi" FFmpeg, zrestartuj swój edytor (np. VS Code) lub terminal.

## Autor

**Jakub Nowak**
* GitHub: [MrRobinMr](https://github.com/MrRobinMr)

---
*Uwaga: Ten projekt służy do celów edukacyjnych i zarządzania własną biblioteką plików.*
