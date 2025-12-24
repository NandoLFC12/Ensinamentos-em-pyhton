{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "I0bm7TVl3McI"
      },
      "source": [
        "# Exercícios\n",
        "\n",
        "### Antes de irmos para o desafio que apresentamos na última aula (que é bem mais complexo do que um exemplo simples) vamos resolver um exercício um pouco mais simples para treinar\n",
        "\n",
        "## 1. Cálculo do Percentual e da Lista de Vendedores\n",
        "\n",
        "- Queremos criar uma function que consiga identificar os vendedores que bateram uma meta, mas além disso, consigo já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta (para eu não precisar calcular manualmente depois)\n",
        "- Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas vendas. E me dar 2 respostas: uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a meta."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TIC2FSQf3McK"
      },
      "outputs": [],
      "source": [
        "meta = 10000\n",
        "vendas = {\n",
        "    'João': 15000,\n",
        "    'Julia': 27000,\n",
        "    'Marcus': 9900,\n",
        "    'Maria': 3750,\n",
        "    'Ana': 10300,\n",
        "    'Alon': 17870,\n",
        "}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "06aVCRcV3McL"
      },
      "outputs": [],
      "source": [
        "#crie sua function aqui\n",
        "def calculo_meta(meta, vendas):\n",
        "    bateram_meta = []\n",
        "    for vendedor in vendas:\n",
        "        if vendas[vendedor] >= meta:\n",
        "            bateram_meta.append(vendedor)\n",
        "    perc_baterammeta = len(bateram_meta) / len(vendas)\n",
        "    return perc_baterammeta, bateram_meta"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aqPsYUJf3McM",
        "outputId": "5a331689-de9e-4e5d-cd3d-9eab07c9c4f1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.6666666666666666\n",
            "['João', 'Julia', 'Ana', 'Alon']\n"
          ]
        }
      ],
      "source": [
        "#aplique sua function nas informações para ver se está funcionando\n",
        "p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)\n",
        "print(p_meta)\n",
        "print(vendedores_acima_meta)"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.3"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}