# Implementação do método PCA para comprimir imagens.

Execução de um trabalho de Álgebra Linear. A implementação do PCA neste código foi feita com base no pseudocódigo abaixo:

```
PCA ( X , l ):

1. Crie um vetor m dado pela média das linhas de X
    (i.e., cada entrada de m é a média da coluna respectiva de X)
2. Subtraia de cada entrada de X o valor respectivo de m, obtendo uma nova matriz V.
3. Calcule a matriz M = V*V (a (transposta de V) multiplicada por V).
4. Calcule os autovalores λ0 ≥ λ1 ≥ ⋯ 0 de M, em ordem decrescente.
5. Calcule uma autobase ortonormal v0, v1, … de para M, com cada v[i] correspondendo a λ[i].
6. Crie uma matriz P com v0, v1, …, v[n] como colunas.
7. Calcule Y = VP
8. Retorne m, P e Y
```

❗Este programa foi feito exclusivamente para um trabalho acadêmico.
