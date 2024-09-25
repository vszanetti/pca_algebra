This Python code implements [Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) (PCA) for image compression by applying the algorithm to the red, green, and blue channels of a BMP image separately, then reconstructing and displaying the compressed result.

The aforementioned algorithm was made through the guidance of the following pseudocode:

```
PCA (X, l):

1. Create a vector m given by the mean of the rows of X
    (i.e., each entry of m is the mean of the respective column of X).
2. Subtract the respective value of m from each entry of X, obtaining a new matrix V.
3. Calculate the matrix M = V*V (the transpose of V multiplied by V).
4. Compute the eigenvalues λ0 ≥ λ1 ≥ ⋯ 0 of M, in decreasing order.
5. Compute an orthonormal eigenbasis v0, v1, … for M, with each v[i] corresponding to λ[i].
6. Create a matrix P with v0, v1, …, v[n] as columns.
7. Compute Y = VP
8. Return m, P, and Y
```
❗This program was written exclusively for academic purposes.

***
Este código Python implementa a [Análise de Componentes Principais](https://pt.wikipedia.org/wiki/Análise_de_componentes_principais) (PCA) para compressão de imagens, aplicando o algoritmo separadamente aos canais de cor vermelho, verde e azul de uma imagem BMP, reconstruindo e visualizando o resultado comprimido.

O algoritmo supracitado foi baseado no seguinte pseudocódigo:

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
