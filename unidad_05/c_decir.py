#pip install cowsay // esto va en consola xdd sino no funca
import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.cow("hola, " + sys.argv[1])
