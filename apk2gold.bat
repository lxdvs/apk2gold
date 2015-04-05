set MPATH=%~dp0
set FOLDER=%~dnp1
call %MPATH%apktool\apktool d -f %1
call mkdir %FOLDER%\src
call rename %FOLDER%\smali .smali
call %MPATH%dex2jar-0.0.9.15\d2j-dex2jar %1
echo "Converting .class files to java..."
call java -jar %MPATH%jd-cli.jar %FOLDER%-dex2jar.jar -od %FOLDER%\src
call del %FOLDER%-dex2jar.jar
call python %MPATH%rreassoc.py %FOLDER%
