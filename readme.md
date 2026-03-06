# Atividade ativa: Estrutura de dados

## 1. Desenvolver um programa em Python que:
-	Cadastre músicas em uma playlist.
-	Armazene os registros em uma Árvore Binária de Busca (BST).
-	Permita buscar uma música pelo nome.
-	Mostre o caminho percorrido na árvore até encontrar a música.

### Estrutura de dados
**Cada música deve conter**
* Nome da música (string) 
* Chave da árvore
* Autor (string)
* Duração em segundos (inteiro)


**Requisitos do Programa**
1. **Cadastro**: O programa deverá cadastrar 10 músicas.

>**Tipos de cadastro permitidos:**
>- Digitadas pelo usuário ou,
>- Inseridas por meio de uma lista fixa dentro do código, para facilitar testes.

>**Retorno:** Após cada inserção, o programa deve informar que a música foi inserida com sucesso.

2. **Busca por música:**

> O usuário deverá informar o nome da música
>> O programa deverá:
>> - Informar se a música foi encontrada
>> - Exibir nome, autor e duração
>> - Mostrar o caminho percorrido na árvore
>> - Mostrar o nível (profundidade) do nó encontrado


#### Exemplo de execução:
```
Digite o nome da música para busca: Diaba

Música encontrada
    Nome: Diaba
    Autor: Urias
    Duração: 186 segundos
    Caminho percorrido: raiz → direita → esquerda
    Nível na árvore: 2
```

Se não encontrar:
    Música não encontrada.

> **Estrutura esperada do código:**
>> O aluno deve criar:
>>-	Uma classe No (nó da árvore)
>>-	Uma classe ArvoreBinariaBusca
>>>	#### Método de inserção
>>>	#### Método de busca
>>-	Função principal para execução do programa

**Exemplo de execução no terminal python**
````
>>> from playlist import Playlist
>>> lista = Playlist("Batidão", "YouTube", "https://yt.com/kjsdljghadsl")
>>> lista.add_musica("Carro de malandro", "Tribo da periferia", "190")
>>> lista.add_musica("Abandonado", "Exaltasamba", "255")
>>> busca = lista.ArvoreBinariaBusca(lista.root)
>>> busca.get_musicas_pelo_nome("Abandonado") 
Nome: Abandonado
Autor: Exaltasamba
Duração: 255
Caminho percorrido: raiz -> esquerda
Nível da árvore: 1
[{'musica': 'Abandonado', 'autor': 'Exaltasamba', 'duracao': '255'}]
