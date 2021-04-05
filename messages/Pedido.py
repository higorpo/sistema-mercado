mensagens = {
    'adicionar': 'Adicionar novo pedido',
    'listar': 'Listar pedidos',
    'ja_cadastrado': 'AVISO: Um pedido com este código já foi cadastrado!',
    'label_observacao': 'Digite uma observação para este pedido:',
    'mostrando_cadastros': 'Mostrando pedidos cadastrados',
    'lista_valores':
        lambda pedido: f'Código: {pedido.codigo}\nObservação: {pedido.observacao}\nData: {pedido.data_pedido}\nCliente: {pedido.cliente.nome}\nFuncionário: {pedido.funcionario.nome}\nForma de pagamento: {pedido.forma_pagamento.metodo}\nPreço da compra: R$ {pedido.obter_dados_faturamento()}\nItem(s) pedido:\n{pedido.obter_itens_pedido()} ---',
    'selecionar_cliente_adicionar_pedido': 'Qual cliente está fazendo essa compra?\nSelecione uma das duas opções abaixo para escolher um cliente.',
    'cadastro_cliente_adicionar_pedido': 'Cadastre um novo cliente para adicionar a este pedido.',
    'selecionar_funcionario_adicionar_pedido': 'Qual funcionário está vendendo essa compra?\nSelecione uma das duas opções abaixo para escolher um funcionário.',
    'cadastro_funcionario_adicionar_pedido': 'Cadastre um novo funcionário para adicionar a este pedido.',
    'selecionar_forma_pagamento_adicionar_pedido': 'Qual é a forma de pagamento para este pedido?\nSelecione uma das duas opções abaixo para escolher uma forma de pagamento.',
    'cadastro_forma_pagamento_adicionar_pedido': 'Cadastre uma nova forma de pagamento para adicionar a este pedido.',
    'sem_produtos_estoque': 'Não há produtos em estoque, cadastre-os primeiro...',
    'preco_compra': lambda total_preco: f'O preço total desta compra foi de R$ {round(total_preco, 2)}.',
    'nao_tem_estoque': 'ERRO: Esta quantidade não está disponível no estoque! Digite outra:',
}
