import os
import pymkv

"""
# CASO QUEIRA QUE AS ENTRADAS SEJAM PELO CONSOLE

dirA = input("Informe o diretório A: ")
dirA = dirA.replace('\\', '/')
dirA += "/"

dirB = input("Informe o diretório B: ")
dirB = dirB.replace('\\', '/')
dirB += "/"
"""

# DECLARAÇÃO DE VARIÁVEIS
dirA = "C:/Users/David S. Ferreira/3D Objects/MKVFactory/A/"
dirB = "C:/Users/David S. Ferreira/3D Objects/MKVFactory/B/"
dirOutput = "C:/Users/David S. Ferreira/3D Objects/MKVFactory/OUTPUT/"

# CRIANDO ARRAY COM OS ARQUIVOS DO DIRETÓRIO A (FULL PATH)
arrayDirA = os.listdir(dirA)
dirA += '{0}'
arrayDirA = [dirA.format(i) for i in arrayDirA]

# CRIANDO ARRAY COM OS ARQUIVOS DO DIRETÓRIO B (FULL PATH)
arrayDirB = os.listdir(dirB)
dirB += '{0}'
arrayDirB = [dirB.format(i) for i in arrayDirB]

print(arrayDirA)
print(arrayDirB)

############################################################

# DECLARAÇÃO DE VARIÁVEIS FILE
fileA = pymkv.MKVFile(arrayDirA.pop(0))
fileB = pymkv.MKVFile(arrayDirB.pop(0))

# DECLARAÇÃO DE VARIÁVEIS TRACK
fileATrack1 = pymkv.MKVTrack(arrayDirA.pop(0), track_id=1)

# OPERAÇÕES COM AS VARÁVEIS ANTES DECLARADAS
fileA.add_file(fileB)

fileATrack1.default_track = False
fileATrack1.forced_track = False

fileA.remove_track(0)
fileA.remove_track(1)
fileA.remove_track(2)

fileA.mux(dirOutput + '1.mkv')

'''
Essa pode ser uma ideia interessante, juntar dois arquivos e ir operando não funciona, então porque não pegar os tracks
e juntar em um mkv, mas tem que ver se ele aceita importar os anexos (attachments).

>>> from pymkv import MKVFile
>>> file = MKVFile()
>>> file.add_track(track1)
>>> file.add_track(track2)
>>> file.add_track(track3)
>>> file.mux('path/to/output.mkv')
'''
