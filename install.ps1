# 1. Tworzenie środowiska wirtualnego Python (venv)
Write-Host "--- Step 1: Creating virtual environment ---" -ForegroundColor Cyan
if (!(Test-Path "venv")) {
    python -m venv venv
    Write-Host "Virtual environment created." -ForegroundColor Green
} else {
    Write-Host "Virtual environment already exists." -ForegroundColor Gray
}

# 2. Instalacja bibliotek Python
Write-Host "`n--- Step 2: Installing Python dependencies ---" -ForegroundColor Cyan
if (Test-Path "requirements.txt") {
    .\venv\Scripts\pip install -r requirements.txt
} else {
    Write-Host "Warning: requirements.txt not found. Skipping pip install." -ForegroundColor Yellow
}

# 3. Automatyczna instalacja FFmpeg
Write-Host "`n--- Step 3: Setting up FFmpeg ---" -ForegroundColor Cyan
$ffmpegFolder = "$pwd\ffmpeg"
$ffmpegZip = "$pwd\ffmpeg.zip"
$ffmpegUrl = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

if (!(Test-Path "$ffmpegFolder\bin\ffmpeg.exe")) {
    Write-Host "FFmpeg not found. Starting download (approx. 100MB)..." -ForegroundColor Yellow
    
    # Pobieranie
    Invoke-WebRequest -Uri $ffmpegUrl -OutFile $ffmpegZip
    
    Write-Host "Extracting FFmpeg..." -ForegroundColor Yellow
    Expand-Archive -Path $ffmpegZip -DestinationPath "$pwd\temp_ffmpeg" -Force
    
    # Przenoszenie plików tak, aby struktura była poprawna (ffmpeg/bin/...)
    $extractedFolder = Get-ChildItem -Path "$pwd\temp_ffmpeg" -Directory | Select-Object -First 1
    Move-Item -Path "$($extractedFolder.FullName)\*" -Destination "$pwd\ffmpeg" -Force
    
    # Sprzątanie
    Remove-Item -Path $ffmpegZip -Force
    Remove-Item -Path "$pwd\temp_ffmpeg" -Recurse -Force
    
    Write-Host "FFmpeg installed successfully." -ForegroundColor Green
} else {
    Write-Host "FFmpeg is already installed in the project folder." -ForegroundColor Gray
}

# 4. Dodawanie FFmpeg do zmiennej środowiskowej PATH (User)
$ffmpegBinPath = "$pwd\ffmpeg\bin"
$currentPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)

if ($currentPath -notlike "*$ffmpegBinPath*") {
    Write-Host "`n--- Step 4: Updating System PATH ---" -ForegroundColor Cyan
    [Environment]::SetEnvironmentVariable(
        "Path",
        $currentPath + ";$ffmpegBinPath",
        [EnvironmentVariableTarget]::User
    )
    Write-Host "FFmpeg added to PATH. Please restart your IDE/Terminal to apply changes." -ForegroundColor Green
}

Write-Host "`nInstallation finished! You can now run the project using: python main.py" -ForegroundColor Cyan
pause