mensagens = {
    'adicionar': 'Cadastrar novo produto',
    'excluir': 'Excluir produto',
    'editar': 'Editar produto',
    'listar': 'Listar produtos',
    'buscar': 'Buscar produtos',
    'ja_cadastrado': 'AVISO: Este produto já foi cadastrado anteriormente',
    'mostrando_cadastros': 'Mostrando produtos cadastrados',
    'lista_valores':
        lambda produto: f'Código do produto: {produto.codigo}\nNome do produto: {produto.nome}\nPreço: {produto.preco}\nQuantidade em estoque: {produto.qtd_estoque}\nMarca: {produto.marca}\nCategoria: {produto.categoria.nome}\n ---',
    'nada_cadastrado_busca': 'AVISO: Não existem produtos para buscar, cadastre um primeiro...',
    'titulo_tela_editar': 'Qual produto você deseja editar?\nSelecione uma das duas opções abaixo para escolher um produto para editar',
    'titulo_tela_buscar': 'Selecione uma das opções abaixo para buscar por um produto...',
    'titulo_tela_selecionar': 'Selecione os produtos desejados (pressione ESPAÇO para marcar, ENTER para continuar):',
    'label_nome': 'Nome do produto',
    'label_preco': 'Preço do produto',
    'label_estoque': 'Quantidade no estoque',
    'label_marca': 'Marca do produto',
    'selecionar_categoria_adicionar_produtos': 'A qual categoria de produto este produto pertence?\nSelecione uma das duas opções abaixo para escolher uma categoria de produto',
    'label_quantidade_desejada': lambda produto: f'{produto.nome} (em estoque: {produto.qtd_estoque})',
    'estoque_vazio': 'Não há itens em estoque!'
}
