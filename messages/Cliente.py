mensagens = {
    'cadastrar': 'Cadastrar novo cliente',
    'excluir': 'Excluir cliente',
    'editar': 'Editar cliente',
    'listar': 'Listar clientes',
    'buscar': 'Buscar cliente',
    'ja_cadastrado': 'AVISO: Um cliente com este CPF já foi cadastrado!',
    'label_cpf': 'Digite o CPF do cliente:',
    'label_nome': 'Digite o nome do cliente:',
    'label_email': 'Digite o email do cliente:',
    'label_telefone': 'Digite o telefone (com DDD) do cliente:',
    'label_vip': 'O cliente é VIP? (s/n)',
    'label_atualmente': lambda atributo, valor: f'@ {atributo} cadastrado(a) atualmente é \'{valor}\'. Digite -- se você quer manter esse valor!',
    'nada_cad_excluir': 'AVISO: Não há nenhum cliente para excluir, cadastre um primeiro...',
    'mostrando_cadastros': 'Mostrando clientes cadastrados',
    'nada_cadastrado': 'Não há nada cadastrado para ser listado...',
    'lista_valores':
        lambda cliente: f'Nome: {cliente.nome}\nCPF: {cliente.cpf}\nTelefone: {cliente.telefone}\nEmail: {cliente.email}\nEndereço: {cliente.endereco}\nVIP: {cliente.vip}\n ---',
    'nada_cadastrado_busca': 'AVISO: Não existem clientes para buscar, cadastre um primeiro...',
    'erro_excluir': 'ERRO: Erro ao excluir um cliente...'
}