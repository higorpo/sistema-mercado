mensagens = {
    'adicionar': 'Cadastrar novo cliente',
    'excluir': 'Excluir cliente',
    'editar': 'Editar cliente',
    'listar': 'Listar clientes',
    'buscar': 'Buscar clientes',
    'listar_compras': 'Listar compras de um cliente',
    'ja_cadastrado': 'AVISO: Um cliente com este CPF já foi cadastrado!',
    'label_cpf': 'CPF do cliente',
    'label_nome': 'Nome do cliente',
    'label_email': 'Email do cliente',
    'label_telefone': 'Telefone (com DDD) do cliente',
    'label_vip': 'O cliente é VIP?',
    'nada_cad_excluir': 'AVISO: Não há nenhum cliente para excluir, cadastre um primeiro...',
    'mostrando_cadastros': 'Mostrando clientes cadastrados',
    'lista_valores':
        lambda cliente: f'Nome: {cliente.nome}\nCPF: {cliente.cpf}\nTelefone: {cliente.telefone}\nEmail: {cliente.email}\nEndereço: {cliente.endereco}\nVIP: {cliente.vip}\nPedidos: {cliente.obter_pedidos()}\n ---',
    'nada_cadastrado_busca': 'AVISO: Não existem clientes para buscar, cadastre um primeiro...',
    'erro_excluir': 'ERRO: Erro ao excluir um cliente...',
    'titulo_tela_excluir': 'Qual cliente você deseja excluir do sistema?\nSelecione uma das duas opções abaixo para escolher um cliente para excluir',
    'titulo_tela_editar': 'Qual cliente você deseja editar?\nSelecione uma das duas opções abaixo para escolher um cliente para editar',
    'titulo_tela_buscar': 'Selecione uma das opções abaixo para buscar por um cliente...',
    'mostrando_lista_compras': 'Mostrando compras do cliente',
    'lista_pedidos_por_cliente':
        lambda pedido: f'Data: {pedido.data_pedido}\nForma de pagamento: {pedido.forma_pagamento.metodo}\nItem(s) pedido:\n{pedido.obter_itens_pedido()}Preço da compra: R${round(pedido.obter_dados_faturamento(), 2)}\n ---',
    'cliente_nao_possui_pedidos': 'AVISO: Este cliente não possui nenhum pedido ainda...'
}
