import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._genres=DAO.getGenres()
        self._artists=DAO.getArtists()
        self._idMapArtists={i.ArtistId: i for i in self._artists}
        self._grafo: nx.DiGraph=nx.DiGraph()
    def getGenres(self):
        return DAO.getGenres()
    def creaGrafo(self, gen:int):
        self._grafo.clear()
        a=DAO.getArtistsFromGenre(gen)
        for i,j in a:
            self._grafo.add_node(self._idMapArtists[i], pop=j)
        e=DAO.getEdges(gen)
        p=nx.get_node_attributes(self._grafo, "pop")
        n=0
        for i,j in e:
            pi=p[self._idMapArtists[i]]
            pj=p[self._idMapArtists[j]]
            if pi > pj:
                self._grafo.add_edge(self._idMapArtists[i], self._idMapArtists[j], weight=pi+pj)
            elif pi == pj:
                self._grafo.add_edge(self._idMapArtists[i], self._idMapArtists[j], weight=pi + pj)
                self._grafo.add_edge(self._idMapArtists[j], self._idMapArtists[i], weight=pi + pj)
            else:
                self._grafo.add_edge(self._idMapArtists[j], self._idMapArtists[i], weight=pi + pj)
        s=list()
        for i in self._grafo.nodes:
            en=0
            ex=0
            for j in self._grafo.in_edges(i, data=True):
                en+=j[2]["weight"]
            for j in self._grafo.out_edges(i, data=True):
                ex+=j[2]["weight"]
            s.append((i, ex-en))
        s.sort(key=lambda x: x[1], reverse=True)
        artInf=s[0]
        e = list(self._grafo.edges(data=True))
        e.sort(key=lambda x: x[2]["weight"], reverse=True)
        arcPes=e[:5]
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges(), artInf, arcPes, [self._idMapArtists[i] for i,j in a]




