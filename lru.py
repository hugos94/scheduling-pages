#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class LRU(object):
    '''  Algoritmo de escalonamento de páginas que utiliza a politica "Least Recently Used" para atender as requisicoes. '''

    def execute(self, frame_size, inputs):
        ''' Metodo que executa o algoritmo de escalonamento de páginas com a politica "Least Recently Used". '''

        requisitions = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        frames = [] # Lista que armazena as paginas
        list_used = [] # Lista de paginas ja utilizadas
        miss = 0 # Contador de miss

        for position,page in enumerate(requisitions): # Iteracao na lista de requisicoes
            if page not in frames: # Verifica se a lista possui a pagina
                candidate_position = -1 # Posicao do possivel candidato a sair do frame
                remove_candidate = -1 # Pagina candidata a sair da lista
                if (len(frames) == frame_size): # Verifica se a lista esta cheia
                    reverse_list = list_used[:] # Copia a lista de paginas ja utilizadas
                    reverse_list.reverse() # Reverte a lista para encontrar a pagina referenciada mais antiga no frame
                    for position,candidate in enumerate(frames): # Iteracao nas paginas existentes no frame
                        if(candidate_position <= reverse_list.index(candidate)): # Verifica se a pagina do frame foi utilizada com o maior tempo
                            candidate_position = reverse_list.index(candidate) # Troca o candidato a sair da lista
                            remove_candidate = position # Troca a posicao do candidato a sair da lista
                    frames.pop(remove_candidate) # Remove o candidato escolhido do frame
                miss+=1 # Contador de miss incrementado
                frames.append(page) # Pagina referenciada é adicionada a lista
            list_used.append(page) # Adiciona a pagina atual a lista de paginas utilizadas

        print("LRU " + str(miss)) # Imprime a saida do LRU
