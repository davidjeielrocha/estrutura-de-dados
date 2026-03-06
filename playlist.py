class Playlist:
    class Node:
        def __init__(self, musica, autor, duracao):
            self.data = {
                "musica": musica,
                "autor": autor,
                "duracao": duracao
            }
            self.left = None
            self.right = None

    def __init__(self, nome, plataforma, link):
        self.name = nome
        self.plataforma = plataforma
        self.link = link
        self.root = None
    
    def add_musica(self, musica, autor, duracao):
        def insert(node, musica, autor, duracao):
            if node is None:
                return self.Node(musica, autor, duracao)
            if musica < node.data["musica"]:
                node.left = insert(node.left, musica, autor, duracao)
            else:
                node.right = insert(node.right, musica, autor, duracao)
            return node
        self.root = insert(self.root, musica, autor, duracao)
    
    def get_musicas(self):
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)
        inorder(self.root)
        return result
    
    class ArvoreBinariaBusca:
        def __init__(self, root):
            self.root = root

        def get_musicas_pelo_nome(self, nome):
            result = []
            caminho = []
            nivel_encontrado = None
            def search(node, pos):
                nonlocal nivel_encontrado            
                if node:
                    if pos == 0:
                        caminho.append("raiz")
                    if node.data["musica"] == nome:
                        result.append(node.data)
                        nivel_encontrado = pos
                        print("Música encontrada:")
                        print("Nome: "  + node.data["musica"] )
                        print("Autor: "  + node.data["autor"] )
                        print("Duração: "  + node.data["duracao"] )
                    if nome < node.data["musica"]:
                        caminho.append("esquerda")
                        search(node.left, pos+1)
                    elif nome > node.data["musica"]:
                        caminho.append("direita")
                        search(node.right, pos+1)
            search(self.root, 0)
            print("Caminho percorrido:", " -> ".join(caminho))
            if nivel_encontrado is not None:
                print(f"Nível da árvore: {nivel_encontrado}")
            else:
                print("Música não encontrada na árvore.")
            return result


# print("Testando a classe Playlist:")
# lista = Playlist("Só as melhores do K7", "Spotify", "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M")
# print("Nome da playlist:", lista.name)
# print("Plataforma:", lista.plataforma)
# print("Link:", lista.link)


# print("Adicionando músicas à playlist")
# lista.add_musica("Fim de semana no parque", "Racionais MC's", "3:45")
# print("Músicas atuais na playlist:", lista.get_musicas())

# lista.add_musica("Ta vendo aquela lua", "Exaltasamba", "3:16")
# print("Músicas atuais na playlist:", lista.get_musicas())

# lista.add_musica("Gangsta Paradise", "Colio", "3:21")
# print("Músicas atuais na playlist:", lista.get_musicas())

# print("Obtendo as músicas pelo nome")
# arvore = Playlist.ArvoreBinariaBusca(lista.root)
# print("Músicas encontradas:", arvore.get_musicas_pelo_nome("Gangsta Paradise"))

# print("Obtendo todas as músicas da playlist")
# print("Todas as músicas da playlist:", lista.get_musicas())