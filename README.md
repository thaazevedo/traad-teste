# traad-teste
Repositório com o código da Prova Técnica da TRAAD


## Exercícios Técnicos

### Exercício 1:

Lista ligada é uma das estruturas de dados mais importantes na computação, utilizada em uma enorme quantidade de aplicações. Uma lista encadeada ou lista ligada é uma estrutura de dados linear e dinâmica. Ela é composta por várias células que estão interligadas através de ponteiros, ou seja, cada célula possui um ponteiro que aponta para o endereço de memória da próxima célula

(fonte: https://pt.wikipedia.org/wiki/Lista_ligada#:~:text=Uma%20lista%20encadeada%20ou%20lista,de%20mem%C3%B3ria%20da%20pr%C3%B3xima%20c%C3%A9lula.)

Em anexo, você encontrará uma implementação parcial de uma lista ligada. O exercício consiste em implementar os métodos vazios, para garantir o correto funcionamento da lista ligada, e fazer com que os testes definidos no __main__ rodem adequadamente.

### Exercício 2

Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada, assim como a existência de cartas disponíveis e horários de nascer e pôr do sol. No Brasil, estas informações são disponibilizadas pelo site https://aisweb.decea.mil.br/.  Nesta página é possível encontrar links para cartas, horários do sol e as informações de TAF e METAR, que são boletins meteorológicos codificados.

Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) e imprima na tela:
As cartas disponíveis
Os horários de nascer e pôr do sol de hoje
A informação de TAF e METAR disponíveis
Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.
