mensagens = {
    'adicionar': 'Cadastrar novo produto',
    'excluir': 'Excluir produto',
    'editar': 'Editar produto',
    'listar': 'Listar produtos',
    'buscar': 'Buscar produtos',
    'ja_cadastrado': 'AVISO: Este produto já foi cadastrado anteriormente',
    'mostrando_cadastros': 'Mostrando produtos cadastrados',
    'nada_cadastrado': 'Não há nada cadastrado para ser listado...',
    'lista_valores':
        lambda produto: f'Código do produto: {produto.codigo}\nNome do produto: {produto.nome}\nPreço: {produto.preco}\nQuantidade em estoque: {produto.qtd_estoque}\nMarca: {produto.marca}\nCategoria: {produto.categoria.nome}\n ---',
    # TODO: Talvez seja melhor centralizar isso no Sistema
    'label_atualmente': lambda atributo, valor: f'@ {atributo} cadastrado(a) atualmente é {valor}. Digite -- se você quer manter esse valor!',
    'nada_cadastrado_busca': 'AVISO: Não existem produtos para buscar, cadastre um primeiro...',
    'titulo_tela_editar': 'Qual produto você deseja editar?\nSelecione uma das duas opções abaixo para escolher um produto para editar',
    'titulo_tela_buscar': 'Selecione uma das opções abaixo para buscar por um produto...',
    'label_nome': 'Digite o nome do produto',
    'label_preco': 'Digite o preço do produto',
    'label_estoque': 'Digite a quantidade do estoque inicial do produto',
    'label_marca': 'Digite a marca do produto',
    'selecionar_categoria_adicionar_produtos': 'A qual categoria de produto este produto pertence?\nSelecione uma das duas opções abaixo para escolher uma categoria de produto'
}
