# Spotonazywacz

![Project Preview](preview.png)

Spotonazywacz to specjalistyczne narzędzie oparte na języku Python, przeznaczone do pobierania i zarządzania plikami muzycznymi. Projekt kładzie duży nacisk na poprawne metadane oraz czyste i przejrzyste nazewnictwo plików. Dzięki integracji z silnikiem FFmpeg, zapewnia wysoką jakość przetwarzania dźwięku i idealnie zorganizowaną lokalną bibliotekę muzyczną.

## Wymagania projektowe

Aby pomyślnie uruchomić projekt, będziesz potrzebować:
* **Python 3.10 lub nowszy**
* **System operacyjny Windows** (wymagany do poprawnego działania skryptu instalacyjnego PowerShell)
* **Pliki binarne FFmpeg**

## Instalacja i konfiguracja

Postępuj zgodnie z poniższymi krokami, aby upewnić się, że aplikacja działa poprawnie:

### 1. Konfiguracja FFmpeg
Aplikacja wymaga silnika FFmpeg do przetwarzania plików audio.
* Musisz umieścić folder o nazwie **ffmpeg** bezpośrednio w głównym katalogu projektu.
* Wewnętrzna struktura musi wyglądać następująco: `Spotonazywacz/ffmpeg/bin/ffmpeg.exe`

### 2. Uruchomienie skryptu instalacyjnego
Zamiast ręcznie instalować biblioteki, użyj dostarczonego skryptu automatyzacji znajdującego się w folderze głównym:
* Znajdź plik **install.ps1**.
* Kliknij go prawym przyciskiem myszy i wybierz **Uruchom z PowerShell**.
* Skrypt automatycznie skonfiguruje środowisko i zainstaluje wszystkie niezbędne zależności Pythona.

## Jak używać

1. Potwierdź, że folder **ffmpeg** znajduje się w głównym katalogu projektu.
2. Otwórz terminal lub wiersz poleceń w folderze projektu.
3. Uruchom aplikację, wpisując:
   **python main.py**

## Rozwiązywanie problemów

* **Polityka wykonywania skryptów:** Jeśli PowerShell blokuje skrypt `install.ps1`, otwórz PowerShell jako Administrator i uruchom komendę: `Set-ExecutionPolicy RemoteSigned`.
* **Problemy z FFmpeg:** Jeśli program się uruchamia, ale nie przetwarza dźwięku, sprawdź, czy folder `ffmpeg` ma nazwę pisaną małymi literami i czy zawiera podfolder `bin` z plikami wykonywalnymi `.exe`.
* **Zdjęcie podglądowe:** Upewnij się, że plik `preview.png` znajduje się w katalogu głównym, aby obrazek nagłówka wyświetlał się poprawnie na GitHubie.

## Kluczowe funkcje

* Automatyczne pobieranie muzyki i inteligentne nazywanie plików.
* Synchronizacja metadanych za pomocą FFmpeg.
* Konfiguracja środowiska jednym kliknięciem dzięki dedykowanemu instalatorowi PowerShell.
* Obsługa formatów audio o wysokiej wierności.

## Autor

**Jakub Nowak**
* GitHub: [MrRobinMr](https://github.com/MrRobinMr)
