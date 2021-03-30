mensagens = {
    'cadastrar': 'Cadastrar novo funcionário',
    'excluir': 'Excluir funcionário',
    'editar': 'Editar funcionário',
    'listar': 'Listar funcionários',
    'buscar': 'Buscar funcionário',
    'ja_cadastrado': 'AVISO: Um funcionário com este CPF já foi cadastrado!',
    'label_cpf': 'Digite o CPF do funcionário:',
    'label_nome': 'Digite o nome do funcionário:',
    'label_email': 'Digite o email do funcionário:',
    'label_telefone': 'Digite o telefone (com DDD) do funcionário:',
    'label_salario': 'Digite o salario do funcionário:',
    'label_atualmente': lambda atributo, valor: f'@ {atributo} cadastrado(a) atualmente é {valor}. Digite -- se você quer manter esse valor!',
    'nada_cad_excluir': 'AVISO: Não há nenhum funcionário para excluir, cadastre um primeiro...',
    'mostrando_cadastros': 'Mostrando funcionários cadastrados',
    'nada_cadastrado': 'Não há nada cadastrado para ser listado...',
    'lista_valores':
        lambda funcionario: f'Nome: {funcionario.nome}\nCPF: {funcionario.cpf}\nTelefone: {funcionario.telefone}\nEmail: {funcionario.email}\nSalário: {funcionario.salario}\nData de contratação: {funcionario.data_contratacao}\n ---',
    'nada_cadastrado_busca': 'AVISO: Não existe funcionários para buscar, cadastre um primeiro...',
    'erro_excluir': 'ERRO: Erro ao excluir um funcionário...'
}
