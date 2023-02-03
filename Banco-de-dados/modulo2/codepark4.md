# Banco de dados I - Codepark 4


>De acordo com os conceitos estudados, exiba os resultados das consultas das operações select, project, união, intersecção e diferença. Siga as instruções com base na tabela apresentada em anexo.

>- Mostre as informações apenas dos alunos aprovados. A aprovação é acima de 7,0;
>- Exiba as informações dos alunos do primeiro ano com nota maior ou igual a 8,0;
>- Exiba apenas os nomes e as notas dos alunos;
>- Crie uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor;
>- Crie uma tabela ALUNO com o primeiro e o último nome de cada;
>- Mostre o resultado da união entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
>- Exiba o resultado da intersecção entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
>- Exiba o resultado da diferença entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR. 

![imagem](Imagem01_Atividade04_BancoDeDadosI.png)

#### Resposta
___
* Mostre as informações apenas dos alunos aprovados. A aprovação é acima de 7,0;

```
σ NOTA > 7.0 (ALUNO)
```
|   P.NOME   |  U.NOME  | MATRICULA | SERIE  | DISCIPLINA | NOTA  |
| :--------: | :------: | :-------: | :----: | :--------: | :---: |
|    Luis    |  Silva   |   6215    | 1° ano | Português  |  8.0  |
|   André    | Carvalho |   4521    | 3° ano | Matematica |  9.5  |
|    Alan    |  Vilela  |   3285    | 1° ano |  Historia  |  8.0  |
| Figueiredo |  Santos  |   4598    | 2° ano | Geografia  |  9.0  |

* Exiba as informações dos alunos do primeiro ano com nota maior ou igual a 8,0;

```
σ SERIE = '1° ano' and NOTA >= 8.0 (ALUNO)
```
| P.NOME | U.NOME | MATRICULA | SERIE  | DISCIPLINA | NOTA  |
| :----: | :----: | :-------: | :----: | :--------: | :---: |
|  Luis  | Silva  |   6215    | 1° ano | Português  |  8.0  |
|  Alan  | Vilela |   3285    | 1° ano |  Historia  |  8.0  |

* Exiba apenas os nomes e as notas dos alunos;

```
π NOME, NOTA (ALUNO)
```
|  U.NOME  | NOTA  |
| :------: | :---: |
| Claudino |  7.0  |
 
|  Silva   |  8.0  |
 
| Carvalho |  9.5  |
  
|  Vilela  |  8.0  |

|  Santos  |  9.0  |

* Crie uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor;

##### PROFESSORES
|   pnome    |  unome  | disciplina |    contato    |           email           |
| :--------: | :-----: | :--------: | :-----------: | :-----------------------: |
|  Vitoria   | Martins | Matematica | 85 99191-9292 | vitoria.martins@proz.com  |
|    Luis    |  Filho  | Português  | 85 99292-9191 |    luis.filho@proz.com    |
|   André    |  Souza  | Matematica | 85 98877-6655 |   andre.sousa@proz.com    |
|    Alan    |  Brito  |  Historia  | 85 97766-4433 |    alan.brito@proz.com    |
| Figueiredo |  Costa  | Geografia  | 85 98765-4321 | figueiredo.costa@proz.com |


```
π PNOME, UMONE (PROFESSORES)
```
| PROFESSORES.pnome | PROFESSORES.uname |
| :---------------: | :---------------: |
|      Vitoria      |      Martins      |
|       Luis        |       Filho       |
|       André       |       Souza       |
|       Alan        |       Brito       |
|    Figueiredo     |       Costa       |

* Crie uma tabela ALUNO com o primeiro e o último nome de cada;

##### ALUNOS

|    pnome     |   unome    |    contato    |            email             |
| :----------: | :--------: | :-----------: | :--------------------------: |
|  "Vitoria"   | "Claudino" | 85 99191-9299 | "vitoria.claudino@gmail.com" |
|    "Luis"    |  "Silva"   | 85 99292-9199 |     "luis.silva@uol.com"     |
|   "André"    | "Carvalho" | 85 98877-5555 |     "andre.cv@yahoo.com"     |
|    "Alan"    |  "Vilela"  | 85 97766-3333 |     "alan_vi@gmail.com"      |
| "Figueiredo" |  "Santos"  | 85 98765-2121 |  "figueiredo017@gmail.com"   |

* Mostre o resultado da união entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
```
π pnome, unome (ALUNOS) ∪ π pnome, unome (PROFESSOR)
```

| ALUNOS.pnome | ALUNOS.unome |
| :----------: | :----------: |
|   Vitoria    |   Claudino   |
|     Luis     |    Silva     |
|    André     |   Carvalho   |
|     Alan     |    Vilela    |
|  Figueiredo  |    Santos    |
|   Vitoria    |   Martins    |
|     Luis     |    Filho     |
|    André     |    Souza     |
|     Alan     |    Brito     |
|  Figueiredo  |    Costa     |

* Exiba o resultado da intersecção entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR

```
π pnome, unome (ALUNOS) ∩ π pnome, unome (PROFESSOR)
```
| ALUNOS.pnome | ALUNOS.unome |
| :----------: | :----------: |

* Exiba o resultado da diferença entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR.

```
π pnome, unome (ALUNOS) - π pnome, unome (PROFESSOR)
```
| ALUNOS.pnome | ALUNOS.unome |
| :----------: | :----------: |
|   Vitoria    |   Claudino   |
|     Luis     |    Silva     |
|    André     |   Carvalho   |
|     Alan     |    Vilela    |
|  Figueiredo  |    Santos    |

