# 🔴 DARK SQL | DATABASE USER PARSER 🔴

<p align="center">
  <img width="300" height="250" alt="image" src="https://github.com/user-attachments/assets/25fc9462-c1e9-4167-a1c6-3687b2d49798" />
</p>

Software desenvolvido para **visualização, organização e separação de usuários** a partir de arquivos de texto (logs/databases).  
O sistema processa dados brutos e os estrutura utilizando Python com abordagem orientada a objetos.

---

## 🛠️ Arquitetura do Projeto

O projeto segue uma estrutura modular organizada para separar responsabilidades entre dados, lógica e modelagem:

```
src/
├── database/ # Contém o arquivo database.txt (base de dados)
├── full/ # Execução principal e lógica (databaseUser.py, exe.py)
├── logo/ # Elementos visuais (ASCII/logo)
└── model/ # Estrutura de dados (@dataclass)
```
---

## ⚠️ Configurações Importantes

### 1. Separador de Dados (`:`)

Por padrão, o sistema utiliza `:` como delimitador:

```
usuario@email.com:senha123
```

Se o seu arquivo utilizar outro formato (`;`, `|`, `,`, etc), é obrigatório alterar no código:

```python
self.dados = self.sep.split(":")
```

➡️ Substitua ":" pelo separador correspondente ao seu arquivo.

### 2. Inserção de Usuários

Você pode utilizar o sistema de duas formas:

Opção 1 — Arquivo padrão:

Insira seus dados em:

`src/database/database.txt`

Opção 2 — Arquivo próprio:

Utilize outro arquivo .txt

Ajuste o nome no código para corresponder ao novo arquivo

Caso contrário, ocorrerá erro de leitura (`FileNotFoundError`).

### 3. Uso de Dataclass

O projeto utiliza `@dataclass` para representar os usuários.

Forma correta de acessar os dados:

```python
print(usuario.email)
```

Forma incorreta:

```python
print(usuario["email"])
```

---

## 🚀 Execução do Projeto

Para evitar problemas com importação de módulos, execute sempre a partir da raiz do projeto:

```bash
cd "c:\\Users\\pasta"
python -m src.main
```

> Nota: se o seu script principal for diretamente `src/main.py`, execute `python src/main.py`.

---

## 📄 Exemplo de Entrada

```
user1@email.com:senha1
user2@email.com:senha2
user3@email.com:senha3
```

---

## 📌 Observações

- Certifique-se de que o arquivo está no local correto
- Verifique o separador antes da execução
- Estrutura incorreta de dados pode causar falhas no parsing

---

## 👤 Autor

anjo-yxz
