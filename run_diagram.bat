@echo off
set "JSON_FILE=%~1"
IF "%JSON_FILE%"=="" (
    echo Erreur: Veuillez glisser-déposer un fichier JSON sur ce script ou le fournir en argument.
    pause
    exit /b 1
)
python es_mapping_to_mermaid.py "%JSON_FILE%"
start "" index.html 