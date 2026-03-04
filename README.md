# pOnto — Sistema de Controle de Ponto Gratuito

O pOnto é um sistema de controle de ponto simples, gratuito e de código aberto. Foi criado para suprir a falta de soluções acessíveis para quem precisa de um controle de ponto básico sem custos ou complexidade desnecessária.

## Funcionalidades

- Registro de entrada e saída por empregado
- Cálculo automático de horas trabalhadas
- Controle de diferença em relação à jornada esperada (4 horas)
- Confirmação via modal antes de registrar o ponto
- Senha única para validar o registro
- Painel administrativo completo para o gerente
- Restrição de acesso por IP
- Scripts de configuração e inicialização para Windows

## Tecnologias

- Python 3.x
- Django 6.0.2
- Django REST Framework 3.16.1
- SQLite
- Bootstrap 5.3.3

## Pré-requisitos

- Python 3.x instalado — [python.org/downloads](https://www.python.org/downloads/)
- Git instalado — [git-scm.com](https://git-scm.com/)

## Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/oguiaraujo/pOnto-Sistema.git
cd pOnto-Sistema
```

**2. Execute o setup (apenas na primeira vez):**
```
setup.bat
```

Durante o setup você será solicitado a:
- Definir a senha para bater o ponto
- Informar os IPs das máquinas que terão acesso ao sistema
- Criar o usuário administrador (gerente)

**3. Para iniciar o sistema no dia a dia:**
```
iniciar.bat
```

## Acesso

| Página | URL |
|---|---|
| Bater ponto | `http://<IP-do-servidor>:8000/` |
| Painel do gerente | `http://<IP-do-servidor>:8000/admin/` |

Substitua `<IP-do-servidor>` pelo IP da máquina onde o sistema está rodando.

## Como descobrir o IP de uma máquina

**No Windows**, abra o Prompt de Comando e execute:
```
ipconfig
```
Procure pela seção **"Adaptador de Rede sem Fio"** (Wi-Fi) ou **"Adaptador Ethernet"** (cabo) e anote o valor de **Endereço IPv4**, que terá um formato parecido com `192.168.1.105`.

Para abrir o Prompt de Comando rapidamente pressione `Win + R`, digite `cmd` e pressione Enter.

> **Dica:** Computadores conectados via cabo tendem a ter IPs fixos na rede local, o que evita a necessidade de atualizar o `.env` com frequência. Máquinas conectadas via Wi-Fi podem ter o IP alterado pelo roteador ao reconectar.


## Configuração de IPs

O sistema restringe o acesso apenas às máquinas autorizadas. Os IPs são definidos durante o setup e ficam armazenados no arquivo `.env`:

```
IPS_PERMITIDOS=XXX.X.X.X,XXX.X.X.X
```

Para adicionar ou remover IPs, edite o arquivo `.env` diretamente e reinicie o servidor.

## Estrutura do projeto

```
pOnto/
├── config/             # Configurações do Django
├── core/               # App principal
│   ├── models.py       # Bolsista e SessaoTrabalho
│   ├── views.py        # Lógica de registro de ponto
│   ├── serializers.py  # API REST
│   ├── urls.py         # Rotas
│   ├── admin.py        # Painel administrativo
│   └── middleware.py   # Restrição de acesso por IP
├── templates/
│   └── core/
│       └── punch.html  # Interface de registro de ponto
├── setup.bat           # Configuração inicial (executar uma vez)
├── iniciar.bat         # Inicialização diária
├── setup_env.py        # Geração do arquivo .env
├── requirements.txt    # Dependências do projeto
└── .env.example        # Exemplo de variáveis de ambiente
```

## Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `DJANGO_SECRET_KEY` | Chave secreta do Django (gerada automaticamente) |
| `DJANGO_DEBUG` | Modo debug — sempre `True` |
| `SENHA_PONTO` | Senha para registrar o ponto |
| `ALLOWED_IPS` | IPs autorizados separados por vírgula |

## Como contribuir

Contribuições são bem-vindas! Se você encontrou um bug, tem uma sugestão ou quer adicionar uma funcionalidade:

1. Faça um fork do repositório
2. Crie uma branch para sua alteração:
```bash
git checkout -b minha-alteracao
```
3. Faça o commit das suas mudanças:
```bash
git commit -m "Descrição da alteração"
```
4. Envie para o seu fork:
```bash
git push origin minha-alteracao
```
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [oguiaraujo](https://github.com/oguiaraujo)