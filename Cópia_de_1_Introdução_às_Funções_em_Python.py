{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "d6fa79c4",
      "metadata": {
        "id": "d6fa79c4"
      },
      "source": [
        "# Exercícios de Introdução às Funções em Python"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "6ea92414",
      "metadata": {
        "id": "6ea92414"
      },
      "source": [
        "######  . . . . .  . . . . . . . . . . . . . . . . . . . . . ..  . . . ..  .. .  ..  . . . . ..  . . . . . .. .  . . . . . . . . . ..  . .. .  . . .. . ..  .. .  . . . . . . . . .. . .  .. . . . . . .. . . . . . . . . . . . . . . . .. . . . . . ..\n",
        ".\n",
        "..\n",
        ".\n",
        "..\n",
        ".\n",
        "..\n",
        ".\n",
        "..\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "66043de7",
      "metadata": {
        "id": "66043de7"
      },
      "source": [
        "## Introdução ao uso de funções em Python. Funções são blocos de código que nos permitem organizar e reutilizar tarefas em nossos programas. Elas são uma parte fundamental da programação e nos ajudam a escrever código mais limpo, eficiente e modular.\n",
        "\n",
        "## Para praticar o que aprendemos, temos uma série de exercícios que envolvem o uso de funções básicas para realizar cálculos simples. Vocês deverão criar funções que resolvam os problemas propostos. Lembre-se de usar nomes significativos para suas funções e variáveis, para que o código seja claro e compreensível."
      ]
    },
    {
      "cell_type": "markdown",
      "id": "a7f6647f",
      "metadata": {
        "id": "a7f6647f"
      },
      "source": [
        "## Exercício 1: Calcular a área de um retângulo\n",
        "### Situação Problema: Você está construindo um jardim retangular em sua casa. A largura do jardim é 5 metros e o comprimento é 8 metros. Qual é a área total do jardim?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "931944a6",
      "metadata": {
        "id": "931944a6",
        "outputId": "47b78325-f447-4e9a-8cbe-0b8836f20758",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "40\n"
          ]
        }
      ],
      "source": [
        "def area (largura, comprimento):\n",
        "    return largura * comprimento\n",
        "\n",
        "resultado = area(5,8)\n",
        "print(resultado)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f9684318",
      "metadata": {
        "id": "f9684318"
      },
      "source": [
        "## Exercício 2: Calcular o quadrado de um número\n",
        "### Situação Problema: Você está medindo o lado de um quadrado. O lado mede 6 metros. Qual é a área desse quadrado?"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def quadrado (numero):\n",
        "  return numero ** 2\n",
        "\n",
        "resultado = quadrado(6)\n",
        "print(resultado)"
      ],
      "metadata": {
        "id": "JNorl2gwFjux"
      },
      "id": "JNorl2gwFjux",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "id": "3f96f770",
      "metadata": {
        "id": "3f96f770"
      },
      "source": [
        "## Exercício 3: Converter Celsius para Fahrenheit\n",
        "### Situação Problema: Você está em um país onde a temperatura é medida em Fahrenheit. A temperatura atual é 25 graus Celsius. Qual é a temperatura equivalente em Fahrenheit?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "12546b18",
      "metadata": {
        "id": "12546b18",
        "outputId": "bbbe5b0c-e49b-49ef-951c-6156551a4914",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "77.0\n"
          ]
        }
      ],
      "source": [
        "def fahrenheit(celcius):\n",
        "  return celcius * 9/5\n",
        "resultado = fahrenheit(25) + 32\n",
        "print(resultado)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "535c92f1",
      "metadata": {
        "id": "535c92f1"
      },
      "source": [
        "## Exercício 4: Calcular a média de três números\n",
        "### Situação Problema: Você fez três exames e obteve as seguintes notas: 7.5, 8.0 e 6.5. Qual é a sua média nessas três provas?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c2c4fae5",
      "metadata": {
        "id": "c2c4fae5",
        "outputId": "bb2895b6-1aac-4db1-d2ca-9dcb56b12ffc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A media das notas é 17.5.\n"
          ]
        }
      ],
      "source": [
        "def calcular (num1, num2, num3):\n",
        "  num1 = float(7.5)\n",
        "  num2 = float(8.0)\n",
        "  num3 = float(6.5)\n",
        "  media = num1 + num2 + num3 //3\n",
        "  return print('A media das notas é {}.'.format(media))\n",
        "\n",
        "calcular(7.5,8.0,6.5)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "dc19120f",
      "metadata": {
        "id": "dc19120f"
      },
      "source": [
        "## Exercício 5: Calcular a hipotenusa de um triângulo retângulo\n",
        "### Situação Problema: Você está construindo uma rampa para um skatepark. As duas partes da rampa formam um ângulo reto, e as medidas dos catetos são 4 metros e 5 metros. Qual é o comprimento da rampa (hipotenusa)?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e634d60c",
      "metadata": {
        "id": "e634d60c",
        "outputId": "527c9458-d22f-4874-dab4-f6060620ccab",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "comprimento da rampa é de 6.4031242374328485m²\n"
          ]
        }
      ],
      "source": [
        "def socrates(co,ca):\n",
        "  hi2 = co ** 2 + ca ** 2\n",
        "  hi = hi2 ** 0.5\n",
        "  return print (f'comprimento da rampa é de {hi}m²')\n",
        "\n",
        "socrates(4,5)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "63fa58f9",
      "metadata": {
        "id": "63fa58f9"
      },
      "source": [
        "## Exercício 6: Calcular o perímetro de um quadrado\n",
        "### Situação Problema: Você está construindo um tapete quadrado para a sala de estar. Cada lado do tapete mede 3 metros. Qual é o perímetro total do tapete?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a2cc0651",
      "metadata": {
        "id": "a2cc0651",
        "outputId": "024761a1-e74b-4ddf-9307-aa5bb5e9fe91",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12\n"
          ]
        }
      ],
      "source": [
        "def matematica(perimetro):\n",
        "  return 4 * perimetro\n",
        "\n",
        "problema = matematica(3)\n",
        "print(problema)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "0bc6d476",
      "metadata": {
        "id": "0bc6d476"
      },
      "source": [
        "## Exercício 7: Calcular a média ponderada de três notas\n",
        "### Situação Problema: Você está estudando para três disciplinas diferentes. Suas notas são: 7.0 em Matemática, 8.5 em Ciências e 9.5 em História. Se a Matemática tem peso 2, Ciências tem peso 3 e História tem peso 5, qual é a sua média ponderada?\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "15b67f4a",
      "metadata": {
        "id": "15b67f4a",
        "outputId": "27bf673e-5728-47bc-b15a-35285f36cbff",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sua media pondera foi de 8.7\n"
          ]
        }
      ],
      "source": [
        "def ponderada(nota,nota2,nota3):\n",
        "  matematica = 2\n",
        "  ciencia = 3\n",
        "  historia = 5\n",
        "  peso1 = nota * matematica\n",
        "  peso2 = nota2 * ciencia\n",
        "  peso3 = nota3  * historia\n",
        "  resultado = peso1 + peso2 + peso3\n",
        "  pesos = matematica + ciencia + historia\n",
        "  final = resultado / pesos\n",
        "  return print('Sua media pondera foi de {}'.format(final))\n",
        "\n",
        "ponderada(7.0,8.5,9.5)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "a411f83c",
      "metadata": {
        "id": "a411f83c"
      },
      "source": [
        "## Exercício 8: Calcular a área de um círculo\n",
        "### Situação Problema: Você está pintando um alvo circular em uma parede. O raio do círculo é 2 metros. Qual é a área total que você precisa pintar?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e7a46d2d",
      "metadata": {
        "id": "e7a46d2d",
        "outputId": "bfc539ff-eae8-46b1-a803-a4b52f491c43",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A area total sera <function a at 0x7b9e684222a0>\n"
          ]
        }
      ],
      "source": [
        "def a(raio):\n",
        "  A = 3.14 * (raio ** 2)\n",
        "  return A\n",
        "\n",
        "a(2)\n",
        "print('A area total sera {}'.format(a))"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "1d16b12a",
      "metadata": {
        "id": "1d16b12a"
      },
      "source": [
        "## Exercício 9: Converter quilômetros para milhas\n",
        "### Situação Problema: Você está planejando uma viagem de carro. O percurso tem 200 quilômetros de extensão. Qual é a distância equivalente em milhas?\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1ca02ada",
      "metadata": {
        "id": "1ca02ada",
        "outputId": "5b3af6ec-ee8a-4576-dc83-cba0df6b2111",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "a distancia equivalente em milhas é 124.0\n"
          ]
        }
      ],
      "source": [
        "def matematica(conversao):\n",
        "  a = conversao // 1.609\n",
        "  return print('a distancia equivalente em milhas é {}'.format(a))\n",
        "\n",
        "matematica(200)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b19544a3",
      "metadata": {
        "id": "b19544a3"
      },
      "source": [
        "## Exercício 10: Calcular a média aritmética de quatro números\n",
        "### Situação Problema: Você está acompanhando as notas de um aluno em quatro provas: 6.5, 7.0, 8.5 e 9.0. Qual é a média aritmética dessas quatro notas?\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "10c84074",
      "metadata": {
        "id": "10c84074",
        "outputId": "bf109338-b0d1-4c1a-bf1f-dfb9bb8c8dc5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A sua media aritmética foi 7.75\n"
          ]
        }
      ],
      "source": [
        "def matematica(nota1,nota2,nota3,nota4):\n",
        "  soma = nota1 + nota2 + nota3 + nota4\n",
        "  div = soma / 4\n",
        "  return print('A sua media aritmética foi {}'.format(div))\n",
        "\n",
        "matematica(6.5,7,8.5,9)"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
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
      "version": "3.11.4"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}