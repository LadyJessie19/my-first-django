# Principais Comandos do Django

Este arquivo contém uma lista dos comandos mais usados no Django, organizados por categorias, para facilitar o desenvolvimento e manutenção de projetos Django, como o "Borcelle Cosméticos".

1. Criação de Projeto e Apps
   Criar um novo projeto Django:
   bash
   django-admin startproject nome_do_projeto
   Exemplo: django-admin startproject borcelle
   Criar um novo app dentro de um projeto:
   bash
   python manage.py startapp nome_do_app
   Exemplo: python manage.py startapp app
   Registrar o app no projeto:
   Adicione o nome do app (ex.: 'app') à lista INSTALLED_APPS em settings.py:
   python
   INSTALLED_APPS = [
   ...
   'app.apps.AppConfig',
   ...
   ]
2. Gerenciamento de Banco de Dados e Migrações
   Criar migrações para os modelos:
   bash
   python manage.py makemigrations
   Gera arquivos de migração com base nas mudanças nos modelos.
   Aplicar migrações ao banco de dados:
   bash
   python manage.py migrate
   Aplica as migrações pendentes ao banco de dados, criando ou alterando tabelas.
   Listar migrações pendentes:
   bash
   python manage.py showmigrations
   Mostra o estado das migrações (aplicadas ou não).
   Simular migrações sem aplicá-las:
   bash
   python manage.py migrate --plan
   Mostra o que seria feito sem alterar o banco.
   Reverter uma migração específica:
   bash
   python manage.py migrate nome_do_app número_da_migração
   Exemplo: python manage.py migrate app 0001
   Limpar (resetar) o banco de dados, mantendo as tabelas:
   bash
   python manage.py flush
   Remove todos os dados, mas mantém a estrutura do banco.
   Exportar dados para um arquivo JSON (backup):
   bash
   python manage.py dumpdata > backup.json
   Importar dados de um arquivo JSON:
   bash
   python manage.py loaddata backup.json
3. Servidor de Desenvolvimento
   Iniciar o servidor de desenvolvimento:
   bash
   python manage.py runserver
   Inicia o servidor local em http://127.0.0.1:8000/. Use python manage.py runserver 0.0.0.0:8000 para permitir acesso externo.
   Verificar se há erros de sintaxe nos templates:
   bash
   python manage.py check --deploy
   Verifica erros de configuração e templates antes da implantação.
4. Administração e Usuários
   Criar um superusuário para o admin:
   bash
   python manage.py createsuperuser
   Cria um usuário com permissões de administrador (necessário para acessar /admin/).
   Acessar o shell interativo do Django:
   bash
   python manage.py shell
   Permite interagir com o banco de dados e modelos via Python.
   Executar comandos personalizados:
   bash
   python manage.py <nome_do_comando>
   Para comandos personalizados, crie uma classe Command em management/commands/ no app.
5. Arquivos Estáticos e Mídia
   Coletar arquivos estáticos para produção:
   bash
   python manage.py collectstatic
   Copia todos os arquivos estáticos de STATICFILES_DIRS e apps para STATIC_ROOT.
   Limpar arquivos estáticos antigos:
   bash
   python manage.py collectstatic --clear
   Remove os arquivos antigos antes de coletar novos.
   Criar um arquivo de tradução de mensagens:
   bash
   python manage.py makemessages -l pt_BR
   Gera arquivos .po para tradução em português do Brasil.
   Compilar traduções:
   bash
   python manage.py compilemessages
   Compila os arquivos .po em .mo para uso no projeto.
6. Testes
   Rodar todos os testes do projeto:
   bash
   python manage.py test
   Executa os testes em todos os apps com arquivos tests.py.
   Rodar testes específicos de um app:
   bash
   python manage.py test nome_do_app
   Exemplo: python manage.py test app
7. Outros Comandos Úteis
   Verificar a configuração do projeto:
   bash
   python manage.py check
   Verifica problemas de configuração ou código.
   Gerar documentação automática de modelos:
   bash
   python manage.py inspectdb > models.py
   Cria modelos Django baseados em uma base de dados existente (útil para reverse engineering).
   Limpar o cache do template:
   bash
   python manage.py clear_cache
   Remove o cache de templates, útil para corrigir problemas de cache.
   Notas Adicionais
   Substitua nome_do_projeto, nome_do_app, e outros placeholders pelos nomes reais do seu projeto (ex.: borcelle, app).
   Certifique-se de estar no diretório correto do projeto ao executar os comandos (cd path/to/your/project).
   Para projetos em produção, ajuste as configurações de DEBUG, ALLOWED_HOSTS, e use um banco de dados como PostgreSQL, MySQL, ou outro, em vez de SQLite.
