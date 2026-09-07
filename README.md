## Clean-Architecture
#Configs iniciais

## 1. Inicialização e Versionamento
- `git init` → Cria o repositório Git para controle de versão.
- `git add .` + `git commit -m "..."` → Adiciona arquivos e registra mudanças no histórico, com mensagens padronizadas (ex.: `config:`).

## 2. Ambiente Virtual
- `python3 -m venv venv` → Cria ambiente isolado para dependências.
- `source venv/bin/activate` → Ativa o ambiente virtual para usar Python e pip locais.

## 3. Qualidade de Código (Linting)
- `pip3 install pylint` → Instala o Pylint para verificar estilo e bugs.
- `pylint --generate-rcfile > .pylintrc` → Gera arquivo de configuração para personalizar regras.

## 4. Gerenciamento de Dependências
- `pip3 freeze > requirements.txt` → Lista pacotes e versões instaladas.
- `pip3 install -r requirements.txt` → Recria o ambiente em outra máquina.

## 5. Automação com Pre-commit
- `pip3 install pre-commit` → Instala ferramenta para rodar verificações automáticas.
- `pre-commit install` → Ativa os hooks no repositório, garantindo que checagens (como Pylint) rodem antes de cada commit.
