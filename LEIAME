Este é um sistema de votação online.

    #votoTwitter <id_votação> <+1,-1,0> <comentario>

Exemplo:
    #votoTwitter pnpsDireto +1 pois tem que ser deliberativo, claro

Neste caso, o usuário votou a favor da consulta identificada como pnpsDireto
com o comentário "pois tem que ser...".

Para subir o sistema, coloque as chaves do Twitter
no arquivo maccess.py. Neste mesmo aarquivo, coloque
o acesso ao mongodb. Crie gratuitamente estas contas
no Heroku e no Mongolab, por exemplo.

É necessário subir o streamer de tweets:
    $ heroku create twitterStreamer
    $ git push heroku master

e o servidor que analisa os tweets coletados. Substitua
o Procfile pelo Procfile.server e o requirements.txt
pelo requirements.txt.server, e suba para uma nova instância:

    $ cp Procfile.server Procfile
    $ cp requirements.txt.server requirements.txt
    $ heroku create votacaoServer
    $ git push heroku2 master

Dúvidas/Sugestões:
Canal IRC #labmacambira @ Freenode
Marcelo Saldanha
Vincícius Brás Rocha
