# Descrição dos Arquivos SQL

Este repositório contém diversos scripts SQL utilizados para manipulação e análise de dados relacionados a operadoras e contas contábeis. Abaixo está uma breve descrição de cada arquivo.

## Orientação de Uso

### 1. Rode os arquivos DDL.
Rode os arquivos DDL em algum software de administração de base de dados. Neste projeto foi utilizado o **DBeaver**

### 2. Faça a transformação do Arquivo `.CSV`
Ao importar o arquivo `.CSV` para o banco de dados, ocorreu um erro de incompatibilidade de tipos porque os números decimais no arquivo usavam vírgula (",") como separador, enquanto a tabela do banco esperava ponto ("."). Isso gerou um conflito na conversão dos dados.

Execute o seguinte comando dentro do diretório do seu arquivo, utilizando o terminal `GitBash`:
```bash
  sed 's/,/./g' seu_arquivo.csv > seu_arquivo_corrigido.csv
```

### 3. Rode as queries para consultar os dados filtrados
No DBeaver, rode as queries `operadoras_maiores_despesas_trimestre.sql` e `operadoras_maiores_despesas_ano.sql` para consultar os dados.

## Arquivos DDL (Definição de Estrutura de Dados)

### `ddl_conta_contabil.sql`
Este script contém a definição da estrutura da tabela de contas contábeis, incluindo colunas, tipos de dados e restrições. Ele é utilizado para criar a tabela que armazenará informações financeiras das operadoras.

### `ddl_operadoras_ativas.sql`
Define a estrutura da tabela que armazena informações sobre as operadoras de saúde ativas. Este script é responsável por criar a tabela e estabelecer suas restrições.

## Arquivo de Importação de Dados

### `import_dados_csv.sql`
Script utilizado para importar dados de arquivos CSV para as tabelas do banco de dados. Ele contem comandos `COPY` para importar os dados para uma tabela temporária, e `INSERT` para popular as tabelas com informações operacionais e financeiras. Foi criado uma tabela temporária para tratar o erro em que o ID REG_ANS não estar presente nas duas tabelas.

## Scripts de Análise de Dados

### `operadoras_maiores_despesas_ano.sql`
Consulta que retorna as operadoras com os maiores valores de despesas ao longo de um ano. Pode ser utilizada para identificar tendências de gastos e comparar o desempenho financeiro entre diferentes operadoras.

### `operadoras_maiores_despesas_trimestre.sql`
Consulta semelhante à anterior, mas focada na análise trimestral. Esse script permite visualizar quais operadoras tiveram os maiores gastos em um período de três meses.
