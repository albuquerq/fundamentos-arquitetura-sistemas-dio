# Conceito de Arquitetura em Aplicações para Internet

Segunda parte do curso de Fundamentos de Arquitetura de Sistemas da [Digital Innovation One][DIO]. Aulas ministradas pelo professor [Jefferson Stachelki][professor]. O conteúdo desse documento são anotações [pessoais][Natan Albuquerque] do curso.

O conteúdo de acompanhamento das aulas pode ser encontrado [nesse repositório do github](https://github.com/jeffhsta/fundamentos_arquitetura) do professor.

Alguns conhecimentos básicos são importantes para o entendimento do conteúdo apresentado. Seguem links de leituras rápidas cobrindo alguns desses tópicos levantados pelo professor.

- [HTTP][HTTP];
- [Proxy][PROXY];
- [RES API](./VantagensDesenvolvimentoWebServices.md);
- [Docker][DOCKER];
- [Kubernets][KUBERNETES];

## Tipos de Arquitetura

Os pricipais tipos de arquiteturas são **monolito** e **microserviços**.

### Monolito

O primeiro tipo é quando existe uma única aplicação que cobre as os requisitos possuindo uma única base de códigos. Geralmente as aplicações iniciam seguindo essa arquitetura no primeiro momento. Esse tipo de aplicação é escalada com redundância de instâncias. Um proxy serve para redirecionar as requisições paras as instâncias ativas, de modo a balancear a carga dessa demanda. Conforme a figura a seguir:

![Modelo da arquitetura monolito apresentado pelo professor [Jefferson Stachelki][professor]](https://raw.githubusercontent.com/jeffhsta/fundamentos_arquitetura/master/monolito.png) Fonte: professor [Jefferson Stachelki][professor], repositório de suporte ao curso.

### Microserviços

Esse modelo de arquitetura pode ser implementado de diversas maneiras. Diferente do monolito onde existe somente uma aplicação, nesse modelo têm-se várias aplicações cada qual responsável por uma parte da operação total.

São apresentados três tipos de microserviços que foram identificados no curso como tipos 1, 2, e 3.

#### Tipo 1

Cada serviço pode ser escalado individualmente para atender a variações da demanda, de modo análogo ao monolito, porém cada serviço desse possue sua própria base de código e tem de se comunicar com os demais para que realize as operações da aplicação. Devido a o aumento da troca de mensagens entre os serviços há uma tendência ao caos conforme a aplicação vai crescendo e o número de serviços vai aumentando, o que torna mais difícil a manutenção da aplicação. A seguir, a imagem da arquitetura microserviço do tipo 1:

![Arquitetura de microserviço, template 1](https://raw.githubusercontent.com/jeffhsta/fundamentos_arquitetura/master/microservicos1.png) Fonte: professor [Jefferson Stachelki][professor], repositório de suporte ao curso.

#### Tipo 2

É uma arquitetura que ainda possue vários serviços porém os serviços não possuem comunicação direta entre eles, para isso eles se comunicam através de **Message Broker**. A vantagem desse modelo é o desacoplamento de cada serviço com os demais em relação a comunicação direta. Esse modelo fica com sua integridade submetida à integridade do message broker, de modo que se esse falhar toda a aplicação pode ser comprometida. A seguir, a imagem da arquitetura microserviço do tipo 2:

![Arquitetura de microserviço, template 2](https://raw.githubusercontent.com/jeffhsta/fundamentos_arquitetura/master/microservicos2.png) Fonte: professor [Jefferson Stachelki][professor], repositório de suporte ao curso.

#### Tipo 3

Esse estilo de arquitetura de microserviço segue um **modelo de pipeline**, esse último gerencia cada requisição recebida do proxy, estruturando cada funcionalidade como uma série de passos que são realizados pelos serviços, em ordem estabelecida conforme a programação, e que no fim resultam na realização dessa funcionalidade. É importante escolher a melhor tecnologia conforme a necessidade do domínio da aplicação, e manter os serviços simples para proporcionar uma fácil manutenção do sistema. Exemplos citados de gerenciadores de pipeline são [Camunda](https://camunda.com/) e os ofertados pelos serviços de nuvem como os da Amazon.
É importante que o serviço de pipeline saiba reverter os passos efetuados em caso de um passo falhar no meio do processamento, buscando manter a integridade da aplicação. Segue a imagem da arquitetura de microserviço do tipo 3:

![Arquitetura de microserviço, template 3](https://raw.githubusercontent.com/jeffhsta/fundamentos_arquitetura/master/microservicos3.png) Fonte: professor [Jefferson Stachelki][professor], repositório de suporte ao curso.

## Comparativo Entre as Arquiteturas

## Gerenciamento de Erros e Volume de Acessos


[DIO]:https://web.digitalinnovation.one "Digital Innovation One"
[Natan Albuquerque]:https://github.com/albuquerq "Natan Albuquerque"
[professor]:https://github.com/jeffhsta "Jefferson Stachelki"

[HTTP]:https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol"
[PROXY]:https://pt.wikipedia.org/wiki/Proxy "Proxy"
[DOCKER]:https://docs.docker.com/get-started/ "Docker"
[KUBERNETES]:https://kubernetes.io/pt/ "Kubernetes"