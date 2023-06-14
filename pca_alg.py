import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def PCA(X, l):
    #remodela a imagem
    X = X.reshape(-1, X.shape[-1])

    #obtém a média da imagem
    m = np.mean(X, axis=0)

    #subtrai a média de cada pixel na imagem
    V = X - m

    #calcula a matriz de covariância da imagem
    M = np.matmul(V.T, V)

    #calcula os autovalores e autovetores da matriz de covariância
    autovalores, autovetores = np.linalg.eig(M)

    #seleciona os principais autovetores
    P = autovetores[:, :l]

    #calcula a imagem comprimida
    Y = np.matmul(P.T, V.T)

    #retorna a média, matriz de projeção e imagem comprimida
    return m, P, Y

#lê a imagem BMP usando matplotlib
caminho_imagem = os.path.join(".", "image.bmp")
imagem = plt.imread(caminho_imagem)

#separa os canais de cor e converter para float
canal_vermelho = imagem[:, :, 0].astype(float)
canal_verde = imagem[:, :, 1].astype(float)
canal_azul = imagem[:, :, 2].astype(float)

#aplica PCA a cada canal de cor
l = 2
m_vermelho, P_vermelho, Y_vermelho = PCA(canal_vermelho, l)
m_verde, P_verde, Y_verde = PCA(canal_verde, l)
m_azul, P_azul, Y_azul = PCA(canal_azul, l)

#reconstrói as imagens comprimidas
imagem_reconstruida_vermelho = np.matmul(P_vermelho, Y_vermelho).T + m_vermelho
imagem_reconstruida_verde = np.matmul(P_verde, Y_verde).T + m_verde
imagem_reconstruida_azul = np.matmul(P_azul, Y_azul).T + m_azul

#combina os canais de cor para criar a imagem reconstruída
imagem_reconstruida = np.dstack(
    (
        imagem_reconstruida_vermelho,
        imagem_reconstruida_verde,
        imagem_reconstruida_azul,
    )
)

#plota a imagem original
plt.subplot(121)
plt.imshow(imagem)
plt.title("Imagem original")

#plota a imagem reconstruída
plt.subplot(122)
plt.imshow(imagem_reconstruida.astype(np.uint8))
plt.title("Imagem reconstruída")

#mostra as imagens, lado a lado
plt.show()

#salvar as matrizes e as imagens comprimidas
np.save("mean_red.npy", m_vermelho)
np.save("projection_matrix_red.npy", P_vermelho)
np.save("compressed_image_red.npy", Y_vermelho)

np.save("mean_green.npy", m_verde)
np.save("projection_matrix_green.npy", P_verde)
np.save("compressed_image_green.npy", Y_verde)

np.save("mean_blue.npy", m_azul)
np.save("projection_matrix_blue.npy", P_azul)
np.save("compressed_image_blue.npy", Y_azul)

#salva a imagem reconstruída como um arquivo BMP
imagem_reconstruida = np.clip(imagem_reconstruida, 0, 255).astype(np.uint8)  # Converter para uint8
caminho_imagem_reconstruida = os.path.join(".", "reconstruido.bmp")
cv2.imwrite(caminho_imagem_reconstruida, cv2.cvtColor(imagem_reconstruida, cv2.COLOR_RGB2BGR))