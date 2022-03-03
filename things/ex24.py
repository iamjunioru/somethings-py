# crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com a palavra 'santo'.

print("""se for True, é pq começa com o nome 'SANTO', 
se for False, é pq não começa com o nome 'SANTO'""") # """ deixa comentar varias linhas com quebra sem criar outro print

cidade = str(input('digite o nome da cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')