# Projeto - BIG DATA I - Engenharia de Dados - Santander Coders

Repositório para desenvolvimento do projeto final do módulo de Big Data I do curso de Engenharia de Dados da ADA.

Este projeto tem como objetivo comparar as funcionalidades de duas bibliotecas de processamento de dados, o Pandas e o PySpark, em relação a velocidade e facilidade de uso para a realização de tarefas comuns. 

Foram selecionados dois conjuntos de dados, sendo um pequeno (menos de 10.000 linhas) e outro bem maior (acima de 1.000.000 linhas). As etapas de ETL (Extração, Tratamento e Carregamento) foram realizadas em ambos os conjuntos de dados, utilizando-se apenas o Pandas ou apenas o PySpark em cada etapa.

O tempo de execução das tarefas realizadas foi medido e comparado entre as duas bibliotecas, a fim de avaliar qual delas é mais rápida e eficiente.

## Grupo de desenvolvimento

Desenvolvedores responsáveis pelo desenvolvimento:

- [Cleverson Guandalin](https://github.com/CleverGnd)
- [Gustavo Guimaraes Brandão](https://github.com/GuhBrando)
- [Victor Hugo Marques Vieira](https://github.com/Victordelete)

## Instruções de uso
Para executar o projeto, é necessário ter instalado as seguintes bibliotecas:

Pandas
PySpark

É preciso também ter os datasets Netflix_movies.csv e Fraudulent_Transactions_Data.csv disponíveis na pasta "datasets".

Ambos os datasets estão disponíveis em https://www.kaggle.com/datasets/amjaads/netflix-movies e https://www.kaggle.com/datasets/chitwanmanchanda/fraudulent-transactions-data

O código deve ser executado em um ambiente Jupyter Notebook ou em um interpretador Python. Ao executar o código, serão exibidos os resultados da comparação entre o Pandas e o PySpark.

## Resultados esperados

Ao final da execução do código, será exibido o tempo de execução das tarefas realizadas em cada biblioteca, bem como a diferença percentual entre os tempos e qual biblioteca foi mais rápida.