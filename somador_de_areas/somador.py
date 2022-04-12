import pandas as pd

status = 'sim'
while status == 'sim':
    talhoes = input('Talhões (t1-t2-...-tn): ')

    tabela = pd.read_excel('talhoes_areas.xlsx')
    tabela = tabela.set_index('talhao')
    soma = tabela.loc[talhoes.upper().split(sep='-')].sum().area

    print('\nTalhões: {}\nÁrea:    {:.2f} ha'.format(talhoes.upper(), soma))

    status = input('\nNova consulta? ')