from pathlib import Path
import xml.etree.ElementTree as ET
ruta = Path("D:\\steam\\steamapps\\common\\The Binding of Isaac Rebirth\\mods")

#En este linea de codigo ve la carga de las carpeta de mods y cuenta cuantos mods hay en total, luego imprime el total de mods encontrados.
print("====== Gestor de Mods ======", "\n","Mods totales:", len([item for item in ruta.iterdir() if item.is_dir()]))

#lectura de archivos metadata.xml y parseo de su contenido para obtener la informacion de los mods
for item in ruta.iterdir():
    if item.is_dir():
        metadata_file = item / "metadata.xml"
        if metadata_file.exists():
            tree = ET.parse(metadata_file)
            root = tree.getroot()

            name = root.find("name").text
            directory = root.find("directory").text
            mod_id = root.find("id").text
            version = root.find("version").text
    # descripcion de mods
        print(f"Nombre: {name}\n Versión: {version}\n ID: {mod_id}\n Directorio: {directory}")

 #Aqui quiero hacer un contador de mods cuales esten activo,con errores y cuales esten con coflictos 
print("====== Contador de mods ======")
#mods_activos = 0
#mods_inactivos = 0
#mods_con_errores = 0
#mods_sin_errores = 0
#mods_con_conflictos = 0;