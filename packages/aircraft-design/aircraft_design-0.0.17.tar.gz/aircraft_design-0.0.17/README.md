# aircraft_design
Para instalar a biblioteca oficialmente, você pode usar o gerenciador de pacotes pip.
A seguinte linha de comando pode ser executada no terminal ou prompt de comando:
```bash
pip install aircraft-design
```
Assim, a biblioteca será baixada e instalada em seu ambiente de desenvolvimento Python. Também é possível instalar a versão mais recente diretamente do repositório GitHub, executando o comando:
```bash
pip install git+https://github.com/NisusAerodesign/aircraft-design.git
```
Feito isso, já é possível importar e utilizar a biblioteca nas suas aplicações.

## 0.1. Como instalar
Para instalar basta acessar pelo repositório da própria pipy[*](https://pypi.org/project/aircraft-design) e já estará pronto para uso.
### Projeto de Design de Aeronaves NISUS-aerodesign

O projeto aircraft-design é um esforço desenvolvido por membros da equipe de competição **NISUS-aerodesign** com o objetivo de facilitar a análise de aeronaves. A equipe utiliza a ferramenta Vortex Lattice (ou malha de vórtices, em tradução livre), desenvolvida pelo MIT[*](https://web.mit.edu/drela/Public/web/avl/), para conduzir essas análises. 

A ferramenta Vortex Lattice permite que a equipe tenha uma visão detalhada das propriedades aerodinâmicas da aeronave, como por exemplo, a geração de sustentação, arrasto e forças de inclinação. Isso permite que a equipe faça melhorias no design da aeronave, tornando-a mais eficiente e segura para voo.

[Repositório GitHub](https://github.com/NisusAerodesign/aircraft-design)
# 1. aircraft_design.Wing

A classe Wing (Asa) é responsável por criar superfícies aerodinâmicas, como asas e estabilizadores. Ela possui diversos parâmetros que podem ser ajustados para atender às necessidades específicas de cada projeto.

A tabela abaixo apresenta cada um dos parâmetros da classe Wing, incluindo seu tipo de dado, valor padrão e se é obrigatório ou não:

| Parâmetro       | Tipo de dado | Valor Padrão   |
|:---------------:|:-----------:|:-------------:|
| airfoil         | Path        | **Obrigatório** |
| wingspan        | float       | **Obrigatório** |
| mean_chord      | float       | **Obrigatório** |
| taper_ratio     | float       |            1.0 |
| transition_point| float       |            0.0 |
| alpha_angle     | float       |            0.0 |
| sweep_angle     | float       |            0.0 |
| x_position      | float       |            0.0 |
| y_position      | float       |            0.0 |
| z_position      | float       |            0.0 |
| align           | str         |           'LE' |
| name            | str         |         'wing' |
| control         | list        |         [None] |
| panel_chordwise |int          |             10 |
| panel_spanwise  |int          |             25 |

Além disso, a classe Wing possui métodos *Getters* e *Setters* para todos os seus elementos, permitindo a manipulação de seus parâmetros de forma fácil e precisa. Também podemos encontrar outros métodos importantes, como `Wing().surface -> avl.Surface` e `Wing().reference_area() -> float`, que fornecem informações valiosas sobre a superfície da asa e sua área de referência.


## 1.1. Ferramenta de plotagem

A biblioteca possui uma ferramenta de plotagem para melhor visualização da aeronave construída. Para utilizá-la, basta invocar o método plot() nas classes Wing e Aircraft.

A tabela a seguir apresenta os parâmetros que podem ser especificados na função de plotagem:

|Parâmetro|Tipo de dado              |Valor Padrão|
|:-------:|:------------------------:|:----------:|
|figure   |matplotlib.figure \| None |None        |
|axis     |matplotlib.axis   \| None |None        |
|linewidth| float                    | 1.0        |
|color    |str                       |'black'     |

Ambas as classes Wing e Aircraft podem receber uma figura e um eixo para se adequarem aos padrões de plotagem do usuário. Além disso, o plot gerado é tridimensional.

# 2. aircraft_design.Aircraft

A classe Aircraft é responsável por agrupar as superfícies aerodinâmicas e torná-las executáveis nos parâmetros da biblioteca de simulação de voo. Ela é um elemento fundamental para o projeto, pois permite a definição do avião como um todo, e é a partir dela que serão realizadas as simulações.

Abaixo seguem os principais parâmetros que compõem a classe Aircraft:

|Parâmetro      |Tipo de dado              |Valor Padrão   |
|:-------------:|:------------------------:|:-------------:|
|mach           | float                    |**Obrigatório**|
|ground_effect  | float                    |**Obrigatório**|
|reference_chord| float                    |**Obrigatório**|
|reference_span | float                    |**Obrigatório**|
|surfaces_list  | list                     |**Obrigatório**|
|ref_point_x    | float                    | 0.0           |
|ref_point_y    | float                    | 0.0           |
|ref_point_z    | float                    | 0.0           |

Além desses parâmetros, a classe Aircraft possui métodos Getters e Setters para todos eles, assim como outros métodos que podem ser necessários para realizar as simulações.

## 2.1. Gerar a geometria
Para poder executar a simulação deve ser gerada a geometria para poder ser executada.
```python
Aircraft().geometry(name:str)
```
## 2.2. Ferramenta de plotagem
A ferramenta de plotagem para o módulo **Aircraft** é totalmente compatível com o módulo **Wing**, recebendo os mesmos parâmetros.

Verificar **1.1.**

# aircraft_design.Session

A classe Session é responsável por realizar a execução do código no AVL. Para fazer isso, é necessário que sejam fornecidos os seguintes parâmetros:

|Parâmetro      |Tipo de dado              |Valor Padrão   |
|:-------------:|:------------------------:|:-------------:|
|geometry       | Aircraft.geometry        |**Obrigatório**|
|cases          | Case \|None              |           None|
|name           | str \|None               |           None|

A variável `geometry` representa a geometria da aeronave, que será utilizada pelo AVL para realizar as análises. A variável `cases` é opcional e representa os casos de simulação que serão executados no AVL. Por fim, a variável `name` é também opcional e representa o nome da sessão que está sendo executada.

Com esses parâmetros em mãos, a classe Session é capaz de realizar as simulações no AVL, gerando informações valiosas sobre o comportamento da aeronave em diferentes condições.

# aircraft_design.MultiSession

A classe MultiSession é responsável por realizar a execução de múltiplas sessões no AVL utilizando uma abordagem paralela que aproveita a capacidade de processamento dos múltiplos núcleos da CPU.

Para fazer isso, a classe MultiSession possui o seguinte parâmetro:

|Parâmetro      |Tipo de dado                        |Valor Padrão   |
|:-------------:|:----------------------------------:|:------------:|
|session_array  | list[Session]                      |**Obrigatório**|

A variável `session_array` representa a lista de sessões que serão executadas no AVL, que são objetos da classe `Session` com suas respectivas geometrias e casos de simulação.

A classe MultiSession é responsável por gerenciar os Workers, compartilhar a memória entre eles e organizar as filas de execução das sessões. Dessa forma, a classe MultiSession permite que múltiplas sessões sejam executadas em paralelo, aumentando a eficiência do processo de simulação.

A utilização da classe MultiSession é recomendada quando o número de sessões é maior ou igual ao dobro do número de núcleos da CPU, para que seja possível obter o máximo aproveitamento da capacidade de processamento do hardware.

