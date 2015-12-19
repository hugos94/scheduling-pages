#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class LRU(object):
    '''  Algoritmo de escalonamento de páginas que utiliza a politica "Least Recently Used" para atender as requisicoes. '''

    def execute(self, frame_size, inputs):
        ''' Metodo que executa o algoritmo de escalonamento de páginas com a politica "Least Recently Used". '''

        requisitions = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        frames = [] # Lista que armazena as paginas
        used_frames = []

        miss = 0 # Contador de miss

        for page in requisitions: # Iteracao na lista de requisicoes
            candidate = -1 # Inicializa o candidato a ser retirado como -1
            value = float("inf") # Inicializa o valor de comparacao como infinito
            if not page in frames: # Verifica se a lista possui a pagina
                if (len(frames) == frame_size): # Verifica se a lista esta cheia
                    for p in range(frame_size): # Iteracao nas paginas alocadas
                        if (used_frames[p] < value): # Se o contador de hit de cada pagina for menor que o valor minimo
                            value = used_frames[p] # Valor minimo recebe o valor de hit da pagina
                            candidate = p # candidate recebe o candidato a ser retirado
                    frames.pop(candidate) # candidate é removido da lista
                    used_frames.pop(candidate) # o contador de hit do candidate é removido da lista
                miss+=1 # Contador de miss incrementado
                frames.append(page) # Pagina referenciada é adicionada a lista
                used_frames.append(int(1)) # Contador de hit da pagina referenciada é adicionada na lista
            else:
                used_frames[frames.index(page)] += 1 # Contador de hit da pagina referenciada e incrementado

        print("LRU " + str(miss)) # Imprime a saida do LRU
