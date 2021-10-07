import pandas as pd
import matplotlib.pyplot as plt

# a seguinte linha assume que 'dados.csv' está na mesma pasta do arquivo .py
dados = pd.read_csv('dados.csv')

def suites():
    """
    Conta a frequência dos valores da coluna 'suites' do DataFrame dados. 
    
    Retorna uma pd.Series e cria um gráfico de pizza com o resultado.
    """
    counts = dados['suites'].value_counts()
    counts.plot.pie(autopct='%1.1f%%')
    
    return counts

def area():
    """
    Cria um histograma com 20 classes uniformes das áreas dos apartamentos no 
    DataFrame dados. 
    
    Retorna um DataFrame com as linhas com maior área dos apartamentos.
    """
    areas = dados['area']
    areas.plot.hist(bins=20, color='green')
    
    return dados.loc[dados['area'] == dados['area'].max()]

def procura(preco, area, condominio):
    """
    Recebe preco, area e condominio, calcula a frequência dos valores da coluna 
    'bairro' do DataFrame dados com as condições que o preço é menor ou igual ao 
    preco passado, area é maior ou igual à area passada, condomínio é menor ou igual
    ao condominio passado.

    Retorna as frequências dos bairros nos dados filtrados. Cria um gráfico de barras
    com o resultado.
    """
    df = dados.loc[(dados['preco'] <= preco) & (dados['area'] >= area) & (dados['condominio'] <= condominio)]
    out = df['bairro'].value_counts()
    out.plot.bar(color='orange', rot=0)
    
    return out

