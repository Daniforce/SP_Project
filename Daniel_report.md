Este file serve para irmos escrevendo o relatório ao longo da realização do trabalho. Para cada ponto realizado na checklist, faça a análise correspondente aqui. Desta forma, no final do assignement é só retirar as informações daqui para completar o relatório. 

Step #1 – Encontrar o dataset
"[x] Pesquisar em repositórios (UCI, Kaggle, data.gov, Dados.gov.pt, Eurostat)" -> De entre vários datasets analisados, foram reunidos 3 como backup. O dataset escolhido como principal foi o Adult Census Income (Kaggle), por cumprir integralmente os requisitos exigidos (mais de 5000 registos e forte presença de atributos demográficos e financeiros).

Step #2 – Importação e caracterização do dataset

2.1 Importação e sanitização
"[x] Corrigir charset/encoding (UTF-8, ISO-8859-1)" -> foi importado o dataset escolhido na respetiva formatação (UFT-8 - default).
"[x] Corrigir delimitadores do CSV (;, ,, tab) e aspas" -> Confirmado o uso de vírgula ',' como separador.
"[x] Tratar duplicados e valores em falta" -> Duas secções correspondente ao tratamento de dados, tendo um de nós feito uma e a outra tarefa o outro integrante, para cumprir o requesitado.
"[x] - Importar para o ARX e confirmar tipos de dados (string, inteiro, decimal, data)" -> Colunas numéricas (age, income, capital.gain, capital.loss) configuradas como inteiros e colunas demográficas configuradas como string.
"[x] - Documentar todas as transformaçõesde sanitização" -> Registado no código Python (Sanitizing.py) e no relatório final do projeto.

2.2 Classificação dos atributos

Isto é explicado mais à frente do porquê cada uma das escolhas...

"[x] - Identificadores diretos (identifying)" -> Nenhum atributo mapeado
"[x] - Quasi-identifiers (quasi-identifying): idade, género, código postal, profissão, etc." -> age, workclass, education, marital.status, occupation, relationship, race, sex, native.country.
"[x] - Atributos sensíveis (sensitive): diagnóstico, salário, etc." -> income, capital.gain, capital.loss.
"[x] - Atributos não sensíveis (insensitive)" -> fnlwgt, education.num, hours.per.week.
