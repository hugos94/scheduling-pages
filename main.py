#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from file_manager import *
from fcfs import *
from sjf import *
from rr import *

def main():

    filename = sys.argv[-1] # Recebe o nome do arquivo do console

    if(filename == sys.argv[0]): # Verifica se algum arquivo foi recebido
        print("Arquivo não informado!")

    else:
        fm = FileManager() # Inicializa o gerenciador de arquivos

        inputs = fm.read_input(filename) # Le o arquivo e retorna em forma de lista

        frame_size = inputs.pop(0) # Captura o tamanho do frame informado no arquivo

        fifo = FIFO(frame_size) # Inicializa o algoritmo FIFO
        fifo.execute(inputs) # Executa o algoritmo FIFO
        #
        # otm = OTM() # Inicializa o algoritmo SSTF
        # otm.execute(inputs) # Executa o algoritmo SSTF
        #
        # lru = LRU() # Inicializa o algoritmo Elevador
        # lru.execute(inputs) # Executa o algoritmo Elevador


if __name__ == '__main__':
    main()
