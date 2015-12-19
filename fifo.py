#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class FIFO(object):
    '''  Algoritmo de escalonamento de páginas que utiliza a politica "First In, First Out" para atender as requisicoes. '''

    def execute(self, frame_size, inputs):
        ''' Metodo que executa o algoritmo de escalonamento de páginas com a politica "First In, First Out". '''

        requisitions = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        frames = [] # Lista que armazena as paginas

        miss = 0 # Contador de miss

        for page in requisitions: # Iteracao na lista de requisicoes
            if not page in frames: # Verifica se a lista possui a pagina
                if (len(frames) == frame_size): # Verifica se a lista esta cheia
                    frames.pop(0) # Retira a primeira pagina que entrou
                miss+=1 # Incrementa a variavel de miss
                frames.append(page) # Adiciona a pagina requerida ao fim da lista

        print("FIFO " + str(miss))
