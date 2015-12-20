#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from file_manager import *
from fifo import *
from otm import *
from lru import *


def main():

    filename = sys.argv[-1] # Recebe o nome do arquivo do console

    if(filename == sys.argv[0]): # Verifica se algum arquivo foi recebido
        print("Arquivo não informado!")

    else:
        fm = FileManager() # Inicializa o gerenciador de arquivos

        inputs = fm.read_input(filename) # Le o arquivo e retorna em forma de lista

        frame_size = inputs.pop(0) # Captura o tamanho do frame informado no arquivo

        fifo = FIFO() # Inicializa o algoritmo FIFO
        fifo.execute(frame_size, inputs) # Executa o algoritmo FIFO

        otm = OTM() # Inicializa o algoritmo OTM
        otm.execute(frame_size, inputs) # Executa o algoritmo OTM

        lru = LRU() # Inicializa o algoritmo LRU
        lru.execute(frame_size, inputs) # Executa o algoritmo LRU


if __name__ == '__main__':
    main()
