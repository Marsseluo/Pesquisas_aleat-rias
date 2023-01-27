import os
import random
import webbrowser
from selenium import webdriver
import pandas as pc
from collections import Counter
from random import sample
import time

# os.startfile('msedge')
search = 'De acordo com o Digital Foundry, o Xbox Series X usará uma CPU AMD Zen 2' \
         'personalizada com oito núcleos e clock de 3,8 GHz cada, uma GPU AMD RNDA 2 ' \
         'também customizada com com 12 teraflops e 52 unidades de computação ' \
         'com 1,825 GHz cada. Tudo isso abastecido por um processador de 7 nm, além ' \
         'de 16 GB de RAM GDDR6 e unidade armazenamento SSD NVME (também personalizada) ' \
         'de 1 TB.Esses 16 GB de RAM já eram conhecidos, mas agora seu uso foi detalhado. ' \
         'Essa memória será dividida em 10 GB para a GPU, 3,5 GB para a memória padrão ' \
         'e 2,5 GB para o sistema operacional. Mas algo que deixou os jornalistas e muitos ' \
         'analistas surpresos foi o fato de o console ter a possibilidade de ter seu ' \
         'armazenamento expandido por meio de SSDs de 1TB, bem como suportar um HD externo, ' \
         'que pode ser espetado em uma porta USB 3.2, na traseira do console.' \
         'Xbox 360 took a different approach to hardware compared to its predecessor. ' \
         'The XCPU, named Xenon at Microsoft and "Waternoose" at IBM, is a custom ' \
         'triple-core 64-bit PowerPC-based design by IBM. The CPU emphasized high ' \
         'floating point performance through multiple FPU and SIMD vector processors ' \
         'in each core. The SIMD vector processor (VMX128) was modified for the Xbox to ' \
         'include a dot-product instruction. The dot-product instruction took far less ' \
         'latency than discrete instructions. The VMX128 was also modified by the addition ' \
         'of direct 3D (D3D) compressed data format. This led to an approximate 50 percent ' \
         'savings in required band-width and memory footprint making the CPU having a ' \
         'theoretical peak performance of 115.2 GFLOPS, being capable of 9.6 billion dot ' \
         'products per second. Each core of the CPU was capable of simultaneous multithreading ' \
         'and was clocked at 3.2 GHz. However, to reduce CPU die size, complexity, cost, and ' \
         'power demands, the processor used in-order execution in contrast to the Intel ' \
         'Coppermine 128-based Pentium III used in the original Xbox, which used more complex ' \
         'out-of-order execution. The original chip used a 90 nm process, although a newer ' \
         '65 nm process SOI revision was implemented on later models, which was in-turn ' \
         'superseded by a 45 nm combined CPU and GPU chip. A 21.6 GB/s front side bus, ' \
         'aggregated 10.8 GB/s upstream and downstream, connected Xenon with the graphics ' \
         'processor/northbridge. Xenon was equipped with an 8th way set associative 1 MB ' \
         'Level 2 cache on-die running at half CPU clock speed. This cache was shared ' \
         'amongst the three CPU cores.[9] Each core had separate L1 caches, each ' \
         'containing a two-way set associative 32-Kbyte L1 instruction cache and a' \
         ' four-way set associative 32-Kbyte L1 data cache. The write-through data cache did ' \
         'not allocate cache lines on writes. The CPU also contained ROM storing Microsoft ' \
         'private encrypted keys, used to decrypt game data. The heat sink implemented to ' \
         'cool the Xenon CPU was composed of aluminum fins with a copper base, and a heat ' \
         'pipe. Newer revisions, which had a smaller core, do not feature the heat pipe or ' \
         'copper base. The heat sink was cooled by two 70 mm fans at the rear of the console ' \
         'on original-style consoles, while a single fan mounted on the side of the consoles ' \
         'was used in Xbox 360 S consoles. There were several types of fan used in Xbox 360s, ' \
         'which were produced by Nidec, Sunon, and Delta Electronics.' \
         'While the Xbox Series S shares many features with its sister console, Xbox Series X' \
         ', the hardware inside packs some notable differences. The lower-tier console is expected' \
         ' to cut back the specifications in several key areas, including the GPU, RAM, ' \
         'and onboard solid-state drive (SSD) storage. The device also loses the disc ' \
         'drive in the process, making the trade-off as a digital-only experience. But ' \
         'that still leaves highly-capable console, proving increasingly alluring when ' \
         'entering the next generation on a budget.'

pesquisa = search.split()  # transforma texto entrada em lista
# print(Counter(pesquisa))

nova_pesquisa = []

for item in pesquisa:  # verifica e remove palavras repetidas da lista
    if item not in nova_pesquisa:
        nova_pesquisa.append(item)
# print(len(nova_pesquisa))
# print(Counter(nova_pesquisa))
# n_search = int(input('Digite a quantidade de pesquisas desejadas\n'))
tamanho = len(nova_pesquisa)
# print(tamanho)

inicio = random.randint(0, tamanho - 41)  # cria um número aleatorio para o inicio do indice da lista
fim = inicio + 41  # soma 41 ao numero de inicio da lista para formar o número final

for i in nova_pesquisa[inicio:fim]:  # separa cada elemento da lista
    # lista.append(i)
    # print(Counter(lista))

    # print(i)
    webbrowser.open(f'https://www.bing.com/search?q={i}'  # adiciona o resultado do for um a um na pesquisa do bing
                    '&form=ANSNB1&refig=a128dd977aa941a2a4996fe2c5bcc04f&pc=W129')

    time.sleep(random.randint(1, 8))  # aguarda de 1 a 8 segundos para a execução do proximo for
    input()




