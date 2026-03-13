# Módulo 01 — Atividade de Revisão de Programação

Este repositório contém a implementação das atividades propostas no **Módulo 01 – Revisão de Programação**, utilizando a linguagem **Python**.

## Objetivo

Praticar conceitos básicos de programação, incluindo:

- Entrada e saída de dados
- Estruturas condicionais
- Estruturas de repetição
- Validação de dados
- Construção de menus interativos

---

# Exercícios

## 1) Cálculo de desconto

Faça um programa em **Python** que:

- Receba o valor de uma conta
- Receba um percentual de desconto
- Calcule o novo valor da conta após aplicar o desconto
- Exiba o resultado final.

---

## 2) Calculadora básica

Escreva um programa em **Python** que realize as operações básicas de uma calculadora:

- Soma
- Subtração
- Multiplicação
- Divisão

### Requisitos

O programa deve:

- Receber **dois números informados pelo usuário**
- Perguntar **qual operação será realizada**
- Validar se os dados informados são números
- Caso não sejam números, mostrar uma mensagem solicitando um valor válido
- Após mostrar o resultado, o programa deve **retornar ao início**

O programa **somente deve ser encerrado quando o usuário digitar a letra:**F


---

## 3) Cálculo do dígito verificador do CPF

Escreva um programa em **Python** que:

- Receba um **CPF informado pelo usuário**
- Calcule o **dígito verificador do CPF**

### Requisitos

- Validar se os dados informados são **numéricos**
- Caso contrário, mostrar mensagem solicitando um número válido
- Após apresentar o resultado, o programa deve **retornar ao início**
- O programa **somente será finalizado quando o usuário digitar:**
F

---

## 4) Cálculo do dígito verificador do CNPJ

Escreva um programa em **Python** que:

- Receba um **CNPJ informado pelo usuário**
- Calcule o **dígito verificador do CNPJ**

### Requisitos

- Validar se os dados informados são **numéricos**
- Caso não sejam números, exibir uma mensagem solicitando valor válido
- Após mostrar o resultado, o programa deve **retornar ao início**
- O programa **somente será finalizado quando o usuário digitar:**
F

---

## 5) Sistema de menu de usuários

Crie um programa em **Python** que imprima um **menu interativo** contendo as seguintes opções:

- 1 - Incluir usuário
- 2 - Excluir usuário
- 3 - Consultar usuário
- 4 - Alterar usuário
- 5 - Listar todos os usuários cadastrados
- 9 - Sair


### Requisitos

a) O programa **só deve ser finalizado quando o usuário escolher a opção 9 (Sair)**.

b) Caso o usuário escolha qualquer outra opção válida, o programa deve:

- Exibir o **número e o nome da opção selecionada**
- Encerrar o programa após a exibição.

c) Caso o usuário digite uma opção **não prevista**, o programa deve:

- Exibir uma mensagem de **"opção inválida"**
- O programa **não deve ser finalizado**

---

# Orientações para Entrega

1. Enviar **o link do código implementado** ou o **arquivo compactado (.zip)**.

2. Gravar um **vídeo de no máximo 10 minutos** apresentando:

- As **5 atividades**
- Explicação do código
- Demonstração do funcionamento dos programas.

3. Sugestões de ferramentas:

- **Google Colab** para implementação do código
- **Zoom** ou **OBS Studio** para gravação do vídeo

## Estrutura do Projeto

```
atividade-revisao-python/
│
├── README.md
├── exercicio1.py
├── exercicio2_calculadora.py
├── exercicio3_cpf.py
├── exercicio4_cnpj.py
└── exercicio5_menu.py
```