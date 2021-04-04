mensagens = {
    'adicionar': 'Adicionar novo pedido',
    'listar': 'Listar pedidos',
    'ja_cadastrado': 'AVISO: Um pedido com este código já foi cadastrado!',
    'label_observacao': 'Digite uma observação para este pedido:',
    'mostrando_cadastros': 'Mostrando pedidos cadastrados',
    'nada_cadastrado': 'Não há nada cadastrado para ser listado...',
    'lista_valores':
        lambda pedido: f'Código: {pedido.codigo}\nObservação: {pedido.observacao}\nData: {pedido.data_pedido}\nCliente: {pedido.cliente.nome}\nForma de pagamento: {pedido.forma_pagamento.metodo}\nItem(s) pedido:\n{pedido.obter_itens_pedido()} ---',
}
