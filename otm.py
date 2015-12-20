#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class OTM(object):
    '''  Algoritmo de ótimo de escalonamento de páginas utilizados para atender as requisicoes. '''

    def execute(self, frame_size, inputs):
        ''' Metodo que executa o algoritmo de escalonamento de páginas Ótimo. '''

        requisitions = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        frames = [] # Lista que armazena as paginas

        miss = 0 # Contador de miss

        for page in requisitions: # Iteracao na lista de requisicoes
            candidate = -1 #
            p = -1
            if not page in frames: # Verifica se a lista possui a pagina
                if (len(frames) == frame_size): # Verifica se a lista esta cheia
                    for position,value in enumerate(frames): # Iteracao nas paginas alocadas
                        if (requisitions.index(value) >= candidate): #
                            candidate = value #
                            p = position
                    frames.pop(frames.index(frames[p])) # candidate é removido da lista
                miss+=1 # Contador de miss incrementado
                frames.append(page) # Pagina referenciada é adicionada a lista

        print("OTM " + str(miss)) # Impressao do algoritmo FIFO
