
dados = {
    'mes' : ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro'],
    'Produtos' : ['camiseta',  'tenis', 'bota', 'camiseta', 'calça'],
    'Quantidade' : [40,70,60,50,80]
    
}

df = pd.DataFrame(dados)
v_janeiro = df[df['mes'] == 'Janeiro']
pmv_janeiro = v_janeiro['Quantidade'].idxmax()
p_janeiro = df.loc[pmv_janeiro, 'Produtos']
procentagem_janeiro = df.loc[pmv_janeiro, 'Quantidade'] / v_janeiro['Quantidade'].sum() * 100

print(f"\nProduto mais vendido em janeiro: ", p_janeiro, "com ", procentagem_janeiro, "% das vendas\n")

vc_janeiro = df[(df['Produtos'] == 'camiseta') & (df['mes'] == 'Janeiro')]['Quantidade'].values[0]
vc_fervereiro = df[(df['Produtos'] == 'camiseta') & (df['mes'] == 'Fevereiro')]['Quantidade'].values[0]

aumento_percentual = ((vc_fervereiro - vc_janeiro) / vc_janeiro) * 100

print("\nAumento percentual nas vendas de camisetas de janeiro para fevereiro: ", aumento_percentual, "%\n")

pmv_geral= df.groupby('produto')['Quantidade'].sum().idxmax()
tv_geral = df.groupby('Produto')['Quantidade'].sum().max()

print(f"\nProduto mais vendido em geral: ", {tv_geral}, "com ", pmv_geral, "% das vendas\n")
    print(dado[0],dado[1],dado[2])
