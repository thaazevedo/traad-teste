import requests

from bs4 import BeautifulSoup

class Scrapper:
    """
    Classe para scrapper de informações sobre os aérodromos.
    """

    def validate_len_icao(self, icao: str):
        """
        Verifica se o código ICAO possui 4 caracteres

        Retorna:
            True caso o tamanho seja 4, caso contrário, False
        """
        return False if len(icao) != 4 else True  

    def format_url(self, icao: str):
        """
        Formata a url para a requisição.

        Args:
            icao: Código do aeródromo
        
        Retorna:
            A url formatada
        """
        format_url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={icao}"

        return format_url
    
    def request(self, url: str):
        """
        Executa a requisição GET na url da página do aeroporto.

        Args:
            url: Url da página a ser acessada
        
        Retorna:
            A página se a requisição for bem sucedida, caso contrário, None 
        """
        try:
            response = requests.get(url)
           
            # Se o código ICAO possuir 4 dígitos, mas não for de um
            # aeródromo válido, o site retorna o history maior de zero
            if len(response.history) > 0:
                print("\nErro ao encontrar informações do aeródromo solicitado\n")
                return None
            
            # Após isso, verifique o status_code da resposta do site
            return response.text if response.status_code == 200 else None
                
        except Exception as error:
            print(f'Erro durante execução da função `request`: {str(error)}')
        
        return None
    
    def parser_html(self, html: str):
        """
        Realiza o parser da página HTML.

        Args:
            html: Conteúdo da página HTML

        Retorna:
            Objeto BeautifulSoup que contém as informações da página HTML após parser
        """
        
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    def get_infos(self, soup: BeautifulSoup):
        """
        Realiza a extração e formatação das informações requisitadas do aeródromo.
        
        Args:
            soup: Objeto BeautifulSoup após parser da página HTML
        
        Retorna:
            Dicionário com as informações do aeródromo
        """
        try:
            # Nome do aeródromo:
            name = soup.find('span', title='Nome do Aeródromo').text
            
            # Cidade do aeródromo:
            city = soup.find('span', title='cidade').text

            # Estado do aeródromo:
            state = soup.find('span', title='Estado').text
            
            # Cartas disponíveis:
            format_letters = []

            # Pega as tags `a` que possuem infos das cartas:
            tag_letters = soup.select('a[onclick^="javascript:pageTracker._trackPageview(\'/cartas/aerodromos\')"]')
            
            # Para cada tag, obtém o seu nome e link do pdf, 
            # adicionando a uma lista
            for tag in tag_letters: 
                letter = {
                    'name': tag.text,
                    'pdf': tag['href']
                }
                format_letters.append(letter)
            
            # Horário de nascer do sol
            sunrise = soup.find('sunrise').text
        
            # Horário do pôr do sol
            sunset = soup.find('sunset').text
            
            # Pega a coluna lateral, que possui informaçõe de TAF e METAR
            right_col = soup.select('div.col-lg-4.order-sm-12 p')
        
            # TAF
            taf = right_col[3].text

            # METAR  
            metar = right_col[2].text

            # Cria dicionário com informações do aeródromo
            aerodrome_data = {
                'name': name,
                'city': city,
                'state': state,
                'letters': format_letters,
                'sunrise': sunrise,
                'sunset': sunset,
                'taf': taf,
                'metar': metar
            }

            return aerodrome_data
                
        except Exception as error:
            print(f'Erro durante execução da função `get_infos`: {str(error)}')



def run_scrapper():
    scrapper = Scrapper()
    icao = input("Digite o código ICAO: ")

    valid_icao = scrapper.validate_len_icao(icao)

    if not valid_icao:
        print("\nCódigo ICAO inválido!\n")
    
    else:
        url = scrapper.format_url(icao)

        html = scrapper.request(url)
        
        if html:
            soup = scrapper.parser_html(html)   
            aerodrome_data = scrapper.get_infos(soup)
            print_data(aerodrome_data)

def print_data(data: dict):
    """
    Realiza a impressão das informações da tela do usuário

    Args:
        data: Dicionário com as informações do aeródromo
    """

    # Print nome e localização do Aeródromo pesquisado:
    print(f"\n\n AERÓDROMO {data['name']} / {data['city']}, {data['state']}")

    # Print cartas disponíveis:
    print(f"---> Cartas disponíveis:")
    if len(data["letters"]) > 0:
        for letter in data["letters"]:
            print(f"    {letter['name']}: {letter['pdf']}")
    else:
        print(f"    Nenhuma carta encontrada!")
    
    # Print horários de nascer e pôr do sol
    print(f"---> Horário Nascer do Sol: {data['sunrise']}")
    print(f"---> Horário Pôr do Sol: {data['sunset']}")

    # print informações de TAF e METAR disponíveis:
    print(f"---> TAF: {data['taf']}")
    print(f"---> METAR: {data['metar']}")
    print(f"\nDados retirados da AISWEB - https://aisweb.decea.mil.br")
    
    



if __name__ == "__main__":
    run_scrapper()