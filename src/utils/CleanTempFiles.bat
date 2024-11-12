@echo off
setlocal

set "TempDir=%TEMP%"
set "Retries=5"
set "Delay=500"

:retry
set "Counter=0"

for /r "%TempDir%" %%f in (*) do (
    rem Check if the file can be opened (not in use)
    call :tryDeleteFile "%%f"
)

for /d /r "%TempDir%" %%d in (*) do (
    rem Check if the directory can be deleted (not in use)
    call :tryDeleteDir "%%d"
)

goto :EOF

rem Function to try deleting a file
:tryDeleteFile
set "File=%~1"
rem Try deleting the file
del "%File%" /f /q
if exist "%File%" (
    rem File could not be deleted, so we skip it
    echo Skipped (in use or protected): %File%
) else (
    rem File deleted successfully
    echo Deleted: %File%
)
goto :EOF

rem Function to try deleting a directory
:tryDeleteDir
set "Dir=%~1"
rem Try deleting the directory
rd "%Dir%" /s /q
if exist "%Dir%" (
    rem Directory could not be deleted, so we skip it
    echo Skipped (in use or protected): %Dir%
) else (
    rem Directory deleted successfully
    echo Deleted: %Dir%
)
goto :EOF
