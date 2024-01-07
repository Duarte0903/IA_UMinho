<h1 align="center">Projeto da UC de Inteligência Artificial - 2023/2024</h1>
<h2 align="center">Health Planet - Empresa de distribuição</h2>

## Definição
A empresa de distribuição Health Planet tem como objetivo utilizar o meio de entrega de encomendas mais sustentável/ecológico para o planeta.

## Elementos deste repositório
Este repositório contém:
- Base de dados do sistema, separados por temas para manutenção do estado do programa ao fechar e reabrir.
- Código do programa. Todas as funcionalidades e algoritmos que o programa oferece.

## Utilização
- O programa verifica se as pastas da base de dados existem e se não, cria-as. Por este motivo, para manter as pastas no seu sítio, o programa deve ser executado na pasta raiz do repositório através do comando ```python src/main.py```
- Todas as interações com o programa são feitas via terminal, com os menus que são imprimidos.

## Funcionalidades
- Podem ser feitas encomendas, associar essas encomendas a um cliente e o programa irá calcular o melhor caminho dependendo de onde esse cliente mora, bem como a maneira mais eficiente de entregar a encomenda.
- Cada encomenda ficará pendente até ser feito o pedido de entrega. Nesse momento o programa vai selecionar um estafeta disponível que cumpra as condições de entrega da encomenda.
- Os estafetas devem ser associados a plataforma previamente para poderem fazer entregas.
- Os clientes devem também ser associados à plataforma previamente para poderem efetuar encomendas.
- No final a entrega é marcada como concluida quando o cliente a avaliar e o estafeta ficará disponível.
- Podem também ser executados os algoritmos de pathfinding isoladamente através do menu de algoritmos. Estes algoritmos mostram o caminho entre duas cidades que encontrarem primeiro, bem como o custo dessa viagem, logo eles darão resultados diferentes.
- Na criação de uma encomenda é sempre escolhido o caminho mais eficiente em termos de custo.
- O programa também oferece um mapa com os custos de deslocação entre cidades e também as heurísticas associadas a cidade introduzida.

## Conclusão
Trabalho realizado por Pedro Silva, António Silva, Diogo Barros e Duarte Leitão no âmbito da UC de Inteligência Artificial.
