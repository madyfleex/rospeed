try:
    import orjson as json
except ModuleNotFoundError:
    print("El módulo orjson no está instalado. Por favor, instálelo con el comando pip install orjson.")
    exit()

from src.threading import *

if __name__ == "__main__":
    main = RoSpeed()
    main.main()
