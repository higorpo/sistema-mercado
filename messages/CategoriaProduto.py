mensagens = {
    'adicionar': 'Adicionar nova categoria de produto',
    'listar': 'Listar categorias de produto',
    'buscar': 'Buscar categorias de produto',
    'listar_produtos_por_categoria': 'Listar produtos por categoria',
    'ja_cadastrado': 'AVISO: Essa categoria de produto já foi cadastrada!',
    'label_nome_categoria': 'Nome da categoria de produto',
    'mostrando_cadastros': 'Mostrando as categorias de produto cadastradas',
    'lista_valores': lambda categoria_produto: f'- Código: {categoria_produto.codigo}    |    Categoria: {categoria_produto.nome}',
    'nada_cadastrado_busca': 'AVISO: Não existe categorias de produto para buscar, cadastre uma primeiro...',
    'mostrando_cadastros_para_selecionar': 'Selecione a categoria de produto para listar seus produtos:',
    'nenhum_produto_cadastrado': 'AVISO: Esta categoria ainda não possui nenhum produto cadastrado...',
    'mostrando_produtos_categoria': lambda categoria: f'Mostrando produtos da categoria {categoria.nome}',
    'lista_produtos_por_cateogria': lambda produto: f'Nome: {produto.nome}\nMarca: {produto.marca}\n ---'
}
