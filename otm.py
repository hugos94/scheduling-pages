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

        while requisitions: # Executar loop enquanto a lista de requisicoes nao for vazia
            page = requisitions.pop(0) # Retira o primeiro elemento e carrega a page
            if page not in frames: # Verifica se o frame contem a pagina
                if (len(frames) == frame_size): # Verifica se a lista esta cheia
                    best_distance = -1 # Variavel que identifica a maior distancia entre as referencias das paginas
                    candidate = -1 # Candidato a ser removido do frame
                    for position,value in enumerate(frames): # Iteracao nas paginas alocadas
                        try: # Excecao que verifica se a lista possui o elemento que esta no frame
                            if (requisitions.index(value) >= best_distance): # Verifica qual a distancia dos elementos do frame e maior
                                best_distance = value # Armazena a maior distancia
                                candidate = position # Armazena o candidato a ser removido do frame
                        except ValueError: # Se nao tiver, ela para a iteracao e coloca o elemento para ser retirado do frame
                            candidate = position # Posicao do frame que nao estao na lista de requisicoes
                            break # Para a iteracao
                    sai = frames.pop(candidate) # candidate é removido da lista
                miss+=1 # Contador de miss incrementado
                frames.append(page) # Pagina referenciada é adicionada a lista

        print("OTM " + str(miss)) # Impressao do algoritmo FIFO
