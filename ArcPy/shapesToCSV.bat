@echo off

set /p path="Digite o caminho para os arquivos Shapefiles -> "
set /p name="Digite o nome para o arquivo que será gerado -> "

shapes-to-csv.py %path% %name%

pause
