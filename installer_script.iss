[Setup]
AppName=Reproductor de Música
AppVersion=1.0
DefaultDirName={autopf}\Reproductor de Música by Gonzalo Garcez
DefaultGroupName=Reproductor de Música
OutputDir=Output
OutputBaseFilename=Setup-ReproductorMusica
SetupIconFile=icono.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{autoprograms}\Reproductor de Música"; Filename: "{app}\ReproductorMusica.exe"
Name: "{autodesktop}\Reproductor de Música"; Filename: "{app}\ReproductorMusica.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Accesos directos:"; Flags: unchecked

[Run]
Filename: "{app}\ReproductorMusica.exe"; Description: "Iniciar Reproductor de Música"; Flags: nowait postinstall skipifsilent
