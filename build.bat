@echo off
chcp 65001 >nul
setlocal
title Landing - AI Inference Deployment and Quantization
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"

set "PY=C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe"
if not exist "%PY%" set "PY=python"

"%PY%" -c "import reportlab, matplotlib, markdown, fitz, PIL" >nul 2>&1
if errorlevel 1 (
    echo [info] installing python packages ...
    "%PY%" -m pip install --quiet --disable-pip-version-check reportlab matplotlib markdown pymupdf pillow
)

rem usage:
rem   build.bat                 build all volumes
rem   build.bat intro           build the intro volume only
rem   build.bat compute         build the compute volume only
rem   build.bat precision       build the precision volume only
rem   build.bat engine          build the engine volume only
rem   build.bat figures         re-render all figures
rem   build.bat figures intro   re-render one volume's figures

set "TARGET=%~1"
if "%TARGET%"=="" set "TARGET=all"

if /i "%TARGET%"=="all" goto :all
if /i "%TARGET%"=="figures" goto :figures
if /i "%TARGET%"=="intro" goto :one
if /i "%TARGET%"=="compute" goto :one
if /i "%TARGET%"=="precision" goto :one
if /i "%TARGET%"=="engine" goto :one

echo Unknown volume: %TARGET%
echo Choose one of: intro / compute / precision / engine / figures / all
goto :fail

:all
call :build intro
if errorlevel 1 goto :fail
call :build compute
if errorlevel 1 goto :fail
call :build precision
if errorlevel 1 goto :fail
call :build engine
if errorlevel 1 goto :fail
goto :done

:one
call :build %TARGET%
if errorlevel 1 goto :fail
goto :done

:build
set "NAME=%~1"
echo.
echo ==================================================
echo   Building %NAME%
echo ==================================================
"%PY%" books\build\lint.py --book books\%NAME%
if errorlevel 1 exit /b 1
"%PY%" books\build\build.py --book books\%NAME%
if errorlevel 1 exit /b 1
exit /b 0

:figures
set "ONLY=%~2"
if not "%ONLY%"=="" (
    call :figs %ONLY%
    goto :done
)
for %%B in (intro compute precision engine) do call :figs %%B
goto :done

:figs
set "B=%~1"
echo [figures] %B%
for /d %%D in (books\code\%B%\ch*) do (
    if exist "%%D\figs.py" (
        pushd "%%D"
        "%PY%" figs.py >nul 2>&1
        if errorlevel 1 echo       [!] %%~nxD figures failed
        popd
    )
)
exit /b 0

:done
echo.
echo ==================================================
echo   Done. PDFs are in the output folder.
echo ==================================================
pause
exit /b 0

:fail
echo.
echo [failed] build stopped. See the messages above.
pause
exit /b 1
