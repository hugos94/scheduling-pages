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
            candidate = -1
            value = float("inf")
            if not page in frames: # Verifica se a lista possui a pagina
                if (len(frames) == frame_size): # Verifica se a lista esta cheia
                    for p in range(frame_size):
                        if (used_frames[p] < value):
                            value = used_frames[p]
                            candidate = p
                    frames.pop(candidate)
                    used_frames.pop(candidate)
                miss+=1
                frames.append(page)
                used_frames.append(int(1))
            else:
                used_frames[frames.index(page)] += 1

        print("LRU " + str(miss))
