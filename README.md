# README - System Resource

# System Resource

Ferramenta desenvolvida em Python para correção, otimização e automação do Windows.

O objetivo do projeto é centralizar, em uma única interface, diversas ferramentas de manutenção do sistema operacional, permitindo que o usuário execute procedimentos técnicos sem a necessidade de utilizar o Prompt de Comando, o PowerShell ou outras ferramentas nativas do Windows.

---

## Objetivos do projeto

* Simplificar tarefas de manutenção do Windows.
* Automatizar procedimentos repetitivos.
* Centralizar ferramentas do sistema em uma única aplicação.
* Oferecer uma interface intuitiva para usuários comuns e técnicos.

---

## Funcionalidades da versão 1.0

### Disco

* Limpeza de arquivos temporários.
* Verificação de erros no disco.
* Otimização do HD.
* Otimização do SSD.

### Sistema

* Verificação da integridade dos arquivos do Windows.
* Restauração de arquivos corrompidos.
* Recuperação dos componentes do sistema.

### Rede

* Ativação da descoberta de rede.
* Reinicialização dos adaptadores.
* Limpeza do cache DNS.
* Restauração das configurações de rede.

### Desempenho

* Limpeza do cache do sistema.
* Ajustes de desempenho.
* Gerenciamento de processos.

---

## Tecnologias utilizadas

* Python.
* Tkinter.(Pensando na possibilidade de trocar o Tkinter por QT)
* PowerShell.
* Logging.
* PyInstaller.

---

## Estrutura do projeto

```text
SystemResource/
│
├── README.md
├── main.py
│
├── interface/
│   ├── __init__.py
│   ├── janela_principal.py
│   └── componentes.py
│
├── servicos/
│   ├── __init__.py
│   ├── disco.py
│   ├── rede.py
│   ├── restauracao.py
│   ├── limpeza.py
│   └── desempenho.py
│
├── recursos/
│   ├── icones/
│   └── imagens/
│
├── logs/
│
└── configuracoes/
```

---

## Como executar o projeto

1. Clone o repositório.
2. Instale as dependências.
3. Execute o arquivo principal.
4. Selecione os serviços desejados.
5. Clique em **Executar**.

---

## Requisitos

* Windows 10.
* Windows 11.
* Python 3.

Algumas funções exigirão permissões administrativas.

---

## Recursos planejados para versões futuras

* Criação automática de pontos de restauração.
* Agendamento de tarefas.
* Sistema de backup.
* Relatórios detalhados.
* Atualizações automáticas.
* Modo avançado para usuários técnicos.

---

## Aviso

O System Resource realiza alterações no sistema operacional. Antes de executar qualquer procedimento, recomenda-se criar um ponto de restauração e fazer backup dos arquivos importantes.

---

## Licença

Este projeto está sendo desenvolvido para fins educacionais e de aprendizado em automação, manutenção e otimização do Windows.
