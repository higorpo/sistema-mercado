mensagens = {
    'cadastrar': 'Cadastrar novo fornecedor',
    'excluir': 'Excluir fornecedor',
    'editar': 'Editar fornecedor',
    'listar': 'Listar fornecedores',
    'buscar': 'Buscar fornecedor',
    'ja_cadastrado': 'AVISO: Um fornecedor com este CNPJ já foi cadastrado!',
    'label_cnpj': 'Digite o CNPJ do fornecedor:',
    'label_nome': 'Digite o nome do fornecedor:',
    'label_email': 'Digite o email do fornecedor:',
    'label_telefone': 'Digite o telefone (com DDD) do fornecedor:',
    'label_atualmente': lambda atributo, valor: f'@ {atributo} cadastrado(a) atualmente é {valor}. Digite -- se você quer manter esse valor!',
    'nada_cad_excluir': 'AVISO: Não há nenhum fornecedor para excluir, cadastre um primeiro...',
    'mostrando_cadastros': 'Mostrando fornecedores cadastrados',
    'nada_cadastrado': 'Não há nada cadastrado para ser listado...',
    'lista_valores':
        lambda fornecedor: f'Nome: {fornecedor.nome}\nCNPJ: {fornecedor.cnpj}\nTelefone: {fornecedor.telefone}\nEmail: {fornecedor.email}\nEndereço: {fornecedor.endereco}\nFornece: {fornecedor.fornece.nome}\n ---',
    'nada_cadastrado_busca': 'AVISO: Não existem fornecedores para buscar, cadastre um primeiro...',
    'erro_excluir': 'ERRO: Erro ao excluir um fornecedor...'
}
