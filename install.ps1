[Environment]::SetEnvironmentVariable(
    "Path",
    [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User) + ";$pwd\ffmpeg\bin",
    [EnvironmentVariableTarget]::User)