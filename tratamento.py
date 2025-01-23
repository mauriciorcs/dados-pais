import pandas as pd

df = pd.read_csv('dados_consolidados.csv')

print("Exemplos de nomes na coluna 'FileName':")
print(df['FileName'].head())

# Extrair o código do nome do arquivo usando regex
# Supondo que o padrão é 'Automaticas_INMET_82024.csv'
df['Codigo'] = df['FileName'].str.extract(r'_(\d+)(?:\.csv)?')

# se não funcina, split como alternativa
if df['Codigo'].isna().any():
    df['Codigo'] = df['FileName'].str.split('_').str[-1].str.replace('.csv', '', regex=False)

df.to_csv('dados_tratados.csv', index=False)

print("Coluna 'Codigo' criada com sucesso e arquivo salvo como 'dados_tratados.csv'.")