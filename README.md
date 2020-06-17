# Fundamentos de Arquitetura de Sistemas - Digital Innovation One por [Rafael Galleani][]

Repositório [pessoal][Natan Albuquerque] de estudos do curso de fundamentos de arquitetura de sistemas da [Digital Innovation One][DIO]. Conteúdo para revisão de meus conhecimentos sobre os tópicos fundamentais explanados no curso.

## Serviços Web (Web Services)

Serviços para interoperabilidade de sistemas que visa a independência de linguagem, software e hardware, com comunicação majoritariamente através do protocolo HTTP.

No primeiro momento foi amplamente utilizado o formato XML para troca de mensagens, destacando-se os serviços SOAP.

### Vantagens Apontadas na Aula

- Linguagem comum;
- Integração;
- Reutilização de implementação;
- Segurança;
- Custos.

## Simple Object Access Protocol ([SOAP][SOAP])

Serviços Web baseados em XML, definidos pela WSDL e XSD.
- Dados no formato XML;
- Padronizada pela W3C;
- Pode ser usado com outros protocolos de comunicação além do HTTP.

### SOAP Message

Toda comunicação é envelopada em uma mensagem composta pelas sessões Header e Body.

Ex.:
```XML
<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://www.example.org">
  <soap:Header>
  </soap:Header>
  <soap:Body>
    <m:GetStockPrice>
      <m:StockName>T</m:StockName>
    </m:GetStockPrice>
  </soap:Body>
</soap:Envelope>
```

### Web Services Description Language ([WSDL][WSDL])

Utilizada para descrever o serviço, seus métodos, argumentos e respostas, como também informações de acesso.

Para ver o exemplo de WSDL apresentado no curso, [clique aqui](http://soapclient.com/xml/soapresponder.wsdl).

### XML Schema Definition ([XSD][XSD])

Responsável por definir a estrutura (composição de tipos) dos dados do serviço. Toda a definição também é estruturada em XML.

Funciona como a documentação de como deve-se montar a SOAP Message.

### Ferramenta

Foi apresentada a ferramenta [SoapUI](https://www.soapui.org/) como facilitadora do processo de criação/manipulação de serviços SOAP. É possível [baixar](https://www.soapui.org/downloads/soapui/) a versão gratuita da ferramenta.

No curso foi demonstrado um exemplo simples de utilização de um serviço SOAP com a biblioteca [Zeep][LibZeep] da linguagem Python. Recriei o exemplo neste repositório com um virtalenv que pode ser executado. Para executar o exemplo tenha o [Python virtualenv][virtualenv] instalado. Dentro do repositório, vá para o diretório `ExemploPythonSOAP` e inicialize um ambiente virtual para Python 3, conforme as seguintes instruções.
```bash
> cd ExemploPythonSOAP
> virtualenv .
> source ./bin/activate
> cd soapclient
> pip install -r requeriments.txt
> python client.py
```

O arquivo python com o código exemplo entá no diretório `soapclient` com o nome `client.py`, você pode editar e executá-lo para ver o serviço SOAP em funcionamento.

## Representational State Transfer ([REST][REST]) 

[DIO]:https://web.digitalinnovation.one "Digital Innovation One"
[Rafael Galleani]:https://github.com/rafegal
[Natan Albuquerque]:https://github.com/albuquerq "Natan Albuquerque"
[SOAP]:https://pt.wikipedia.org/wiki/SOAP
[REST]:https://pt.wikipedia.org/wiki/REST
[WSDL]:https://pt.wikipedia.org/wiki/Web_Services_Description_Language
[XSD]:https://pt.wikipedia.org/wiki/XML_Schema
[LibZeep]:https://docs.python-zeep.org/en/master/ "Zeep: Python SOAP client"
[virtualenv]:https://virtualenv.pypa.io/en/latest