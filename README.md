# traad-teste
> Repositório com o código da Prova Técnica da TRAAD

## Conteúdos

:small_blue_diamond: [Estrutura do projeto](#estrutura-do-projeto)
:small_blue_diamond:  [Requisitos](#requisitos)
:small_blue_diamond:  [Instalação](#instalação)
:small_blue_diamond:  [Como usar](#como-usar-arrow_forward)
:small_blue_diamond:  [Exercícios Técnicos](#exercícios-técnicos-pencil)
:small_blue_diamond:  [Tecnologias](#tecnologias-books)
:small_blue_diamond:  [Autor](#autor)

## Estrutura do projeto 
 - `exerc1/`: código-fonte do Exercício 1 - LinkedList;
 - `exerc2/`: código-fonte do Exercício 2 - Scrapping; 

## Requisitos
  - [Python 3.10](https://www.python.org/downloads/release/python-3100/)
  - [Docker Compose](https://docs.docker.com/compose/install/)
  - [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Instalação 
```sh
# Clone o repositório:
git clone https://github.com/thaazevedo/traad-teste.git

# Entre no diretório do repositório:
cd traad-teste/
```

## Como usar :arrow_forward:

- Exercício 1 - LinkedList:
  ```sh
    1- Manualmente:
      # Entre no diretório do exercício:
      cd exerc1/

      # Rodando exercício:
      python linkedlist.py
    
    2- Com Docker:
      # Rodando exercício:
      docker-compose run exerc1
      
    ```
- Exercício 2 - Scrapper:  
    ```sh
    1- Manualmente:
      # Entre no diretório do exercício:
      cd exerc2/
      
      # Instala, cria e ativa virtualenv:
      pip install virtualenv
      virtualenv venv
      . venv/bin/activate

      # Instalando requirements
      pip install -r requirements.txt
    
      # Rodando exercício:
      python scrapper.py
    
    2- Com Docker:
       # Rodando exercício:
      docker-compose run exerc2
      
    ```

## Exercícios Técnicos :pencil:

### Exercício 1:

Lista ligada é uma das estruturas de dados mais importantes na computação, utilizada em uma enorme quantidade de aplicações. Uma lista encadeada ou lista ligada é uma estrutura de dados linear e dinâmica. Ela é composta por várias células que estão interligadas através de ponteiros, ou seja, cada célula possui um ponteiro que aponta para o endereço de memória da próxima célula

(fonte: https://pt.wikipedia.org/wiki/Lista_ligada#:~:text=Uma%20lista%20encadeada%20ou%20lista,de%20mem%C3%B3ria%20da%20pr%C3%B3xima%20c%C3%A9lula.)

Em anexo, você encontrará uma implementação parcial de uma lista ligada. O exercício consiste em implementar os métodos vazios, para garantir o correto funcionamento da lista ligada, e fazer com que os testes definidos no __main__ rodem adequadamente.

### Exercício 2:

Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada, assim como a existência de cartas disponíveis e horários de nascer e pôr do sol. No Brasil, estas informações são disponibilizadas pelo site https://aisweb.decea.mil.br/.  Nesta página é possível encontrar links para cartas, horários do sol e as informações de TAF e METAR, que são boletins meteorológicos codificados.

Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) e imprima na tela:
As cartas disponíveis
Os horários de nascer e pôr do sol de hoje
A informação de TAF e METAR disponíveis
Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.

## Tecnologias :books:
As seguintes ferramentas foram usadas na construção do projeto:

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Autor

👤 **Thays Azevedo**

[![Linkedin Badge](https://img.shields.io/badge/-Thays-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/thays-azevedo-0022621ab/)](https://www.linkedin.com/in/thays-azevedo-0022621ab/) [![Gmail Badge](https://img.shields.io/badge/-thaysparecida2015@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:thaysparecida2015@gmail.com)](mailto:thaysparecida2015@gmail.com)
