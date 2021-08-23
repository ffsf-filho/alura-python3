from filme import Filme
from serie import Serie
from playlist import Playlist
from junior import Junior
from pleno import Pleno
from senior import Senior


def testes():
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    vingadores.dar_like()
    vingadores.dar_like()
    print(vingadores)

    atlanta = Serie('atlanta', 2018, 2)
    atlanta.dar_like()
    print(atlanta)

    tmep = Filme('todo mundo em pânico', 1999, 100)
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()

    demolidor = Serie('Demolidor', 2016, 5)
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()

    print("\n======================================================================\n")

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
    print(f'O demolidor está na Playlist? {demolidor in playlist_fim_de_semana}\n')
    print(f'Playlist: {playlist_fim_de_semana.nome}\nTamanho: {len(playlist_fim_de_semana)}\n')
    for programa in playlist_fim_de_semana:
        print(programa)

    print("\n======================================================================\n")

    print('José')
    jose = Junior('José')
    jose.busca_perguntas_sem_resposta()
    jose.mostrar_tarefas()

    print()

    print('Luan')
    luan = Pleno('Luan')
    luan.busca_perguntas_sem_resposta()
    luan.busca_cursos_do_mes()
    luan.mostrar_tarefas()

    print()

    print('Roger')
    roger = Senior('Roger')
    print(roger)


if __name__ == '__main__':
    testes()