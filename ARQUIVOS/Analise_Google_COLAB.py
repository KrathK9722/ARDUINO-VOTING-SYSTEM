{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOHyxtyoUIQjybpEs62HrSi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KrathK9722/ARDUINO-VOTING-SYSTEM/blob/main/ARQUIVOS/Analise_Google_COLAB.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **1 - Importação das bibliotecas:**"
      ],
      "metadata": {
        "id": "ch52YtWrQn3q"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "xYQZIpp_Qk8A"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from matplotlib.ticker import FuncFormatter"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "## 2 - **Carregamento dos dados**:"
      ],
      "metadata": {
        "id": "eNxTTmbIQ2eF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "id_arquivo = \"1iNVCXfu2iFVVHlffBz-fky7U28NhhNv9\"\n",
        "\n",
        "url = f\"https://drive.google.com/uc?export=download&id={id_arquivo}\"\n",
        "\n",
        "dados_originais = pd.read_csv(url,sep=\";\", encoding=\"latin1\")"
      ],
      "metadata": {
        "id": "CyQS-LsMQ7xB"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Sepação feita por \";\" porque o padrão estava como \",\" o que fazia com que o CSV fosse importado com somente uma coluna."
      ],
      "metadata": {
        "id": "QVOn5fWOWFlF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **3 - Visualização dos dados brutos:**"
      ],
      "metadata": {
        "id": "T1eT1vdQSZa5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_originais.head(30)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 991
        },
        "id": "_uZHDHBdScWl",
        "outputId": "7b269184-280c-4ea4-bea5-73f440f7a336"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          DATA  CO_ID  CL_ID CL_GENERO  CL_EC  CL_FHL CL_SEG  PR_ID  \\\n",
              "0   01/02/2019   1000    534         M      4       1      C     67   \n",
              "1   01/02/2019   1000    534         M      4       1      C     70   \n",
              "2   01/02/2019   1000    534         M      4       1      C    178   \n",
              "3   01/02/2019   1000    534         M      4       1      C      4   \n",
              "4   01/02/2019   1000    534         M      4       1      C    175   \n",
              "5   01/02/2019   1000    534         M      4       1      C    187   \n",
              "6   01/02/2019   1000    534         M      4       1      C    163   \n",
              "7   01/02/2019   1000    534         M      4       1      C     11   \n",
              "8   01/02/2019   1000    534         M      4       1      C     95   \n",
              "9   01/02/2019   1000    534         M      4       1      C    198   \n",
              "10  01/02/2019   1000    534         M      4       1      C    182   \n",
              "11  01/02/2019   1000    534         M      4       1      C     86   \n",
              "12  01/02/2019   1000    534         M      4       1      C    221   \n",
              "13  01/02/2019   1000    534         M      4       1      C    200   \n",
              "14  01/02/2019   1000    534         M      4       1      C     13   \n",
              "15  01/02/2019   1000    534         M      4       1      C    218   \n",
              "16  01/02/2019   1000    534         M      4       1      C     84   \n",
              "17  01/02/2019   1000    534         M      4       1      C    121   \n",
              "18  01/02/2019   1000    534         M      4       1      C    176   \n",
              "19  01/02/2019   1000    534         M      4       1      C     13   \n",
              "20  01/02/2019   1000    534         M      4       1      C    136   \n",
              "21  01/02/2019   1000    534         M      4       1      C    108   \n",
              "22  01/02/2019   1000    534         M      4       1      C     69   \n",
              "23  01/02/2019   1000    534         M      4       1      C    143   \n",
              "24  01/02/2019   1000    534         M      4       1      C    149   \n",
              "25  01/02/2019   1000    534         M      4       1      C     61   \n",
              "26  01/02/2019   1000    534         M      4       1      C     64   \n",
              "27  01/02/2019   1000    534         M      4       1      C    191   \n",
              "28  01/02/2019   1000    534         M      4       1      C    189   \n",
              "29  01/02/2019   1000    534         M      4       1      C    135   \n",
              "\n",
              "       PR_CAT               PR_NOME  Unnamed: 10  Unnamed: 11  Unnamed: 12  \\\n",
              "0     BEBIDAS  REFRIGERANTE GUARANA          NaN          NaN          NaN   \n",
              "1     BEBIDAS   REFRIGERANTE OUTROS          NaN          NaN          NaN   \n",
              "2     HIGIENE       LENCO UMEDECIDO          NaN          NaN          NaN   \n",
              "3   ALIMENTOS               ABACAXI          NaN          NaN          NaN   \n",
              "4     LIMPEZA     LIMPADOR MULTIUSO          NaN          NaN          NaN   \n",
              "5     HIGIENE      HASTES FLEXIVEIS          NaN          NaN          NaN   \n",
              "6   ALIMENTOS             MORTADELA          NaN          NaN          NaN   \n",
              "7   ALIMENTOS                AZEITE          NaN          NaN          NaN   \n",
              "8     LIMPEZA             AMACIANTE          NaN          NaN          NaN   \n",
              "9     BEBIDAS            ENERGETICO          NaN          NaN          NaN   \n",
              "10  ALIMENTOS       LATA DE ERVILHA          NaN          NaN          NaN   \n",
              "11    HIGIENE          PRESERVATIVO          NaN          NaN          NaN   \n",
              "12  ALIMENTOS                BANANA          NaN          NaN          NaN   \n",
              "13    LIMPEZA            DETERGENTE          NaN          NaN          NaN   \n",
              "14  ALIMENTOS                BANANA          NaN          NaN          NaN   \n",
              "15  ALIMENTOS    BIFE DE COXAO MOLE          NaN          NaN          NaN   \n",
              "16    HIGIENE       PAPEL HIGIENICO          NaN          NaN          NaN   \n",
              "17  ALIMENTOS                   UVA          NaN          NaN          NaN   \n",
              "18    LIMPEZA          LIMPA VIDROS          NaN          NaN          NaN   \n",
              "19  ALIMENTOS                BANANA          NaN          NaN          NaN   \n",
              "20  ALIMENTOS                RICOTA          NaN          NaN          NaN   \n",
              "21    LIMPEZA             REMOVEDOR          NaN          NaN          NaN   \n",
              "22    BEBIDAS    REFRIGERANTE LIMaO          NaN          NaN          NaN   \n",
              "23    BEBIDAS  REFRIGERANTE GUARANA          NaN          NaN          NaN   \n",
              "24  ALIMENTOS      QUEIJO MUSSARELA          NaN          NaN          NaN   \n",
              "25  ALIMENTOS              SARDINHA          NaN          NaN          NaN   \n",
              "26  ALIMENTOS                   UVA          NaN          NaN          NaN   \n",
              "27    HIGIENE                FRALDA          NaN          NaN          NaN   \n",
              "28  ALIMENTOS               GRANOLA          NaN          NaN          NaN   \n",
              "29    LIMPEZA                  RODO          NaN          NaN          NaN   \n",
              "\n",
              "    Unnamed: 13  \n",
              "0           NaN  \n",
              "1           NaN  \n",
              "2           NaN  \n",
              "3           NaN  \n",
              "4           NaN  \n",
              "5           NaN  \n",
              "6           NaN  \n",
              "7           NaN  \n",
              "8           NaN  \n",
              "9           NaN  \n",
              "10          NaN  \n",
              "11          NaN  \n",
              "12          NaN  \n",
              "13          NaN  \n",
              "14          NaN  \n",
              "15          NaN  \n",
              "16          NaN  \n",
              "17          NaN  \n",
              "18          NaN  \n",
              "19          NaN  \n",
              "20          NaN  \n",
              "21          NaN  \n",
              "22          NaN  \n",
              "23          NaN  \n",
              "24          NaN  \n",
              "25          NaN  \n",
              "26          NaN  \n",
              "27          NaN  \n",
              "28          NaN  \n",
              "29          NaN  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-11ee77a7-ab45-4f2d-b99c-f6e989e4d564\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>DATA</th>\n",
              "      <th>CO_ID</th>\n",
              "      <th>CL_ID</th>\n",
              "      <th>CL_GENERO</th>\n",
              "      <th>CL_EC</th>\n",
              "      <th>CL_FHL</th>\n",
              "      <th>CL_SEG</th>\n",
              "      <th>PR_ID</th>\n",
              "      <th>PR_CAT</th>\n",
              "      <th>PR_NOME</th>\n",
              "      <th>Unnamed: 10</th>\n",
              "      <th>Unnamed: 11</th>\n",
              "      <th>Unnamed: 12</th>\n",
              "      <th>Unnamed: 13</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>67</td>\n",
              "      <td>BEBIDAS</td>\n",
              "      <td>REFRIGERANTE GUARANA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>70</td>\n",
              "      <td>BEBIDAS</td>\n",
              "      <td>REFRIGERANTE OUTROS</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>178</td>\n",
              "      <td>HIGIENE</td>\n",
              "      <td>LENCO UMEDECIDO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>4</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>ABACAXI</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>175</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>LIMPADOR MULTIUSO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>187</td>\n",
              "      <td>HIGIENE</td>\n",
              "      <td>HASTES FLEXIVEIS</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>163</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>MORTADELA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>11</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>AZEITE</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>95</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>AMACIANTE</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>198</td>\n",
              "      <td>BEBIDAS</td>\n",
              "      <td>ENERGETICO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>182</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>LATA DE ERVILHA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>86</td>\n",
              "      <td>HIGIENE</td>\n",
              "      <td>PRESERVATIVO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>221</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>BANANA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>200</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>DETERGENTE</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>13</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>BANANA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>218</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>BIFE DE COXAO MOLE</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>84</td>\n",
              "      <td>HIGIENE</td>\n",
              "      <td>PAPEL HIGIENICO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>121</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>UVA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>176</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>LIMPA VIDROS</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>13</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>BANANA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>136</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>RICOTA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>108</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>REMOVEDOR</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>69</td>\n",
              "      <td>BEBIDAS</td>\n",
              "      <td>REFRIGERANTE LIMaO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>143</td>\n",
              "      <td>BEBIDAS</td>\n",
              "      <td>REFRIGERANTE GUARANA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>149</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>QUEIJO MUSSARELA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>61</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>SARDINHA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>64</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>UVA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>27</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>191</td>\n",
              "      <td>HIGIENE</td>\n",
              "      <td>FRALDA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>189</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>GRANOLA</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>135</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>RODO</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-11ee77a7-ab45-4f2d-b99c-f6e989e4d564')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-11ee77a7-ab45-4f2d-b99c-f6e989e4d564 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-11ee77a7-ab45-4f2d-b99c-f6e989e4d564');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "dados_originais"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **3.1 - Quantide de Colunas e linhas**"
      ],
      "metadata": {
        "id": "mw0MlQITSu-U"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "linhas, colunas = dados_originais.shape\n",
        "\n",
        "print(f\"O número de colunas da tabela é {colunas} e o número total de linhas/registros é {linhas}.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yTAyrzKlS0Wy",
        "outputId": "5c42d15e-1e60-432b-d80e-aeb2d3c23004"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O número de colunas da tabela é 14 e o número total de linhas/registros é 830000.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "-----\n",
        "\n",
        "### O QUE É CADA COLUNA?\n",
        "\n",
        "1. DATA: Data da compra;\n",
        "2. CO_ID: Identificação do número de compra (número da nota fiscal);\n",
        "3. CL_ID: Identificação do cliente (número do cliente);\n",
        "4. CL_GENERO: Sexo biológico informado pelo cliente;\n",
        "5. CL_EC: Estado civil do cliente:\n",
        "    \n",
        "    1: Casado ou união estával;\n",
        "    \n",
        "    2: Divorciado;\n",
        "    \n",
        "    3: Separado;\n",
        "    \n",
        "    4: Solteiro;\n",
        "    \n",
        "    5: Viúvo.\n",
        "6. CL_FHL: Número de filhos do cliente;\n",
        "7. CL_SEG: Segmentação econômica do cliente (classe A, B ou C);\n",
        "8. PR_ID: Código do produto (SKU) adquirido;\n",
        "9. PR_CAT: Categoria do produto adquirido;\n",
        "10. PR_NOME: Nome do produto adquirido.\n",
        "\n",
        "\n",
        "Demais colunas não contem dados e devem ser removidas no processo de limpeza.\n",
        "\n",
        "***`Informações retiradas do documento de analise exploratoria da base de varejo.csv`***\n",
        "\n",
        "-----"
      ],
      "metadata": {
        "id": "8xL_QWCouRvq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **3.2 - Tipos de dados e outras informações:**"
      ],
      "metadata": {
        "id": "EjGu6HZDSlcj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_originais.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q1hZdqq8Sh_U",
        "outputId": "4981d101-3768-45b3-bf81-14edacd1863b"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 830000 entries, 0 to 829999\n",
            "Data columns (total 14 columns):\n",
            " #   Column       Non-Null Count   Dtype  \n",
            "---  ------       --------------   -----  \n",
            " 0   DATA         830000 non-null  object \n",
            " 1   CO_ID        830000 non-null  int64  \n",
            " 2   CL_ID        830000 non-null  int64  \n",
            " 3   CL_GENERO    830000 non-null  object \n",
            " 4   CL_EC        830000 non-null  int64  \n",
            " 5   CL_FHL       830000 non-null  int64  \n",
            " 6   CL_SEG       830000 non-null  object \n",
            " 7   PR_ID        830000 non-null  int64  \n",
            " 8   PR_CAT       830000 non-null  object \n",
            " 9   PR_NOME      830000 non-null  object \n",
            " 10  Unnamed: 10  0 non-null       float64\n",
            " 11  Unnamed: 11  0 non-null       float64\n",
            " 12  Unnamed: 12  0 non-null       float64\n",
            " 13  Unnamed: 13  0 non-null       float64\n",
            "dtypes: float64(4), int64(5), object(5)\n",
            "memory usage: 88.7+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**4 - Limpeza e Validação dos dados**"
      ],
      "metadata": {
        "id": "vXs_ed2y0Se7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Copia do banco de dados original para garantir que os dados originais não sejam modificados e possam ser acessados assim como vieram, permitindo que a tabela seja modificada na nova copia."
      ],
      "metadata": {
        "id": "w9aU3ADc1349"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_modificados = pd.read_csv(url,sep=\";\", encoding=\"latin1\", na_values=[\"#N/D\"])"
      ],
      "metadata": {
        "id": "3VM05EqR1jnl"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Modificação na nova tabela para que o pandas entenda que #N/D é nulo e some ao procurar pelos valores nulos."
      ],
      "metadata": {
        "id": "Cn8_wSkY6B1a"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **4.1 - Linhas Duplicadas**"
      ],
      "metadata": {
        "id": "TGbyGKyNDVfy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "duplicados = dados_modificados.duplicated()\n",
        "print(f\"Linhas duplicadas: {duplicados.sum()}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QToTzakz2nJ9",
        "outputId": "49f7a99f-4b9f-4bfd-fc54-03d88cd2ac54"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Linhas duplicadas: 96553\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Agora que observados que existem registros duplicados precisamos entender se eles realmente são registros duplicados ou apenas registros de um mesmo produto comprado 2 vezes pela mesma pessoa."
      ],
      "metadata": {
        "id": "C0gDsj_7qcYX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "repeticoes_legitimas = dados_modificados.groupby([\"CO_ID\", \"PR_ID\"]).size()\n",
        "print(repeticoes_legitimas[repeticoes_legitimas > 1].head(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kle1l8Rpnax9",
        "outputId": "872733e5-510d-49bf-9923-e78e88db9b99"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CO_ID  PR_ID\n",
            "1000   4        2\n",
            "       11       2\n",
            "       13       2\n",
            "       69       2\n",
            "       218      2\n",
            "       225      2\n",
            "1078   21       2\n",
            "       23       2\n",
            "       25       2\n",
            "       36       2\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Aqui visualizamos registros de notas fiscais com o mesmo produto agora precisamos ver se o resto dos dados nesse registro são identicos."
      ],
      "metadata": {
        "id": "xIEIt4vAqmaF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "exemplo = dados_modificados[(dados_modificados[\"CO_ID\"] == 1000) & (dados_modificados[\"PR_ID\"] == 4)]\n",
        "print(exemplo)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EyvJj9d4oz3B",
        "outputId": "c04d9ac0-0bfa-4f2c-80c5-4be2dd17174f"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          DATA  CO_ID  CL_ID CL_GENERO  CL_EC  CL_FHL CL_SEG  PR_ID  \\\n",
            "3   01/02/2019   1000    534         M      4       1      C      4   \n",
            "40  01/02/2019   1000    534         M      4       1      C      4   \n",
            "\n",
            "       PR_CAT  PR_NOME  Unnamed: 10  Unnamed: 11  Unnamed: 12  Unnamed: 13  \n",
            "3   ALIMENTOS  ABACAXI          NaN          NaN          NaN          NaN  \n",
            "40  ALIMENTOS  ABACAXI          NaN          NaN          NaN          NaN  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Diversos dados duplicados foram encontrados isso nos trás algumas questões, podemos remover os dados supondo que são erros de registro ou levando em consideração que a tabela não tem a coluna quantidade podemos entender que as linhas duplicadas de um mesmo registro da compra de produto esta relacionado a quantidade de produtos compradas sendo cada linha um poroduto. Como solução resolvi levar em consideração a segunda opção e criar uma coluna de quantidades removendo as linhas duplicadas para facilitar a análise.\n",
        "\n",
        "Obs: Vi depois no desafio que a segunda opção era realmente a correta a se seguir."
      ],
      "metadata": {
        "id": "Q-BvyHE78GKr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_com_quantidade = dados_modificados.groupby(\n",
        "    [\"CO_ID\", \"CL_ID\",\"CL_GENERO\",\"CL_EC\",\"CL_FHL\",\"CL_SEG\", \"PR_ID\", \"PR_CAT\", \"PR_NOME\",\"DATA\"],\n",
        "    as_index=False,\n",
        "    dropna=False\n",
        ").size()\n",
        "\n",
        "dados_com_quantidade = dados_com_quantidade.rename(columns={\n",
        "    \"DATA\":\"DATA_BR\"\n",
        "})\n",
        "\n",
        "# Renomeia a coluna criada pelo .size() pra um nome mais claro\n",
        "dados_com_quantidade = dados_com_quantidade.rename(columns={\"size\": \"QUANTIDADE\"})\n",
        "coluna_data = dados_com_quantidade.pop(\"DATA_BR\")\n",
        "dados_com_quantidade[\"DATA_BR\"] = coluna_data"
      ],
      "metadata": {
        "id": "a7yXT6hjta0-"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criação de uma nova tabela com coluna quantidades juntando os itens comprados mais de uma vez pela mesma pessoa em uma só compra na coluna \"QUANTIDADE\" a partir da função groupby que automaticamente ja junta linhas iguais, nome \"DATA\" alterado para \"DATA_BR\" para facilitar o entendimento futuro e separação de data internacional e data brasileira na conversão da data para tipo DATE_TIME.\n",
        "Também mudei a posição da coluna \"DATA_BR\" para posição de ultima coluna por preferencia pessoal de organização.\n",
        "\n",
        "Observação: O comando GroupBy no pandas remove automaticamente as linhas com valores nulos então para garantir que isso não ocorresse sem as devidas verificações decidi deixar o atributo dropna como false para que o pandas não fizesse isso automaticamente, assim como removi as colunas sem nome ao criar a coluna quantidade ja que colunas sem nome são inuteis para nossa análise ainda mais sabendo que todos os seus valores eram vázios."
      ],
      "metadata": {
        "id": "MGQY5AtzxffT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_com_quantidade = dados_com_quantidade.drop_duplicates()"
      ],
      "metadata": {
        "id": "l51nSGM07b3o"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "duplicados_limpos = dados_com_quantidade.duplicated()\n",
        "print(f\"Linhas duplicadas: {duplicados_limpos.sum()}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UznbbEE_7eQZ",
        "outputId": "758c7d31-988b-45df-e2da-2dfc07323012"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Linhas duplicadas: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados_com_quantidade"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "VTFD3WgiuAGt",
        "outputId": "561629fe-cf3b-432d-b4e4-e497572009aa"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         CO_ID  CL_ID CL_GENERO  CL_EC  CL_FHL CL_SEG  PR_ID     PR_CAT  \\\n",
              "0         1000    534         M      4       1      C      4  ALIMENTOS   \n",
              "1         1000    534         M      4       1      C     11  ALIMENTOS   \n",
              "2         1000    534         M      4       1      C     13  ALIMENTOS   \n",
              "3         1000    534         M      4       1      C     23  ALIMENTOS   \n",
              "4         1000    534         M      4       1      C     24  ALIMENTOS   \n",
              "...        ...    ...       ...    ...     ...    ...    ...        ...   \n",
              "733442  919822    155         F      2       0      B    212    LIMPEZA   \n",
              "733443  919822    155         F      2       0      B    214  ALIMENTOS   \n",
              "733444  919822    155         F      2       0      B    225  ALIMENTOS   \n",
              "733445  919822    155         F      2       0      B    227  ALIMENTOS   \n",
              "733446  919822    155         F      2       0      B    228    LIMPEZA   \n",
              "\n",
              "           PR_NOME  QUANTIDADE     DATA_BR  \n",
              "0          ABACAXI           2  01/02/2019  \n",
              "1           AZEITE           2  01/02/2019  \n",
              "2           BANANA           2  01/02/2019  \n",
              "3        COGUMELOS           1  01/02/2019  \n",
              "4       COPA SUINA           1  01/02/2019  \n",
              "...            ...         ...         ...  \n",
              "733442        CERA           2  19/08/2022  \n",
              "733443      CEBOLA           1  19/08/2022  \n",
              "733444        ATUM           1  19/08/2022  \n",
              "733445       ARROZ           2  19/08/2022  \n",
              "733446   AMACIANTE           1  19/08/2022  \n",
              "\n",
              "[733447 rows x 11 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6875d8be-627b-4fc2-a40e-962f174aa1a0\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>CO_ID</th>\n",
              "      <th>CL_ID</th>\n",
              "      <th>CL_GENERO</th>\n",
              "      <th>CL_EC</th>\n",
              "      <th>CL_FHL</th>\n",
              "      <th>CL_SEG</th>\n",
              "      <th>PR_ID</th>\n",
              "      <th>PR_CAT</th>\n",
              "      <th>PR_NOME</th>\n",
              "      <th>QUANTIDADE</th>\n",
              "      <th>DATA_BR</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>4</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>ABACAXI</td>\n",
              "      <td>2</td>\n",
              "      <td>01/02/2019</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>11</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>AZEITE</td>\n",
              "      <td>2</td>\n",
              "      <td>01/02/2019</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>13</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>BANANA</td>\n",
              "      <td>2</td>\n",
              "      <td>01/02/2019</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>23</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>COGUMELOS</td>\n",
              "      <td>1</td>\n",
              "      <td>01/02/2019</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>24</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>COPA SUINA</td>\n",
              "      <td>1</td>\n",
              "      <td>01/02/2019</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>733442</th>\n",
              "      <td>919822</td>\n",
              "      <td>155</td>\n",
              "      <td>F</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>B</td>\n",
              "      <td>212</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>CERA</td>\n",
              "      <td>2</td>\n",
              "      <td>19/08/2022</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>733443</th>\n",
              "      <td>919822</td>\n",
              "      <td>155</td>\n",
              "      <td>F</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>B</td>\n",
              "      <td>214</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>CEBOLA</td>\n",
              "      <td>1</td>\n",
              "      <td>19/08/2022</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>733444</th>\n",
              "      <td>919822</td>\n",
              "      <td>155</td>\n",
              "      <td>F</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>B</td>\n",
              "      <td>225</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>ATUM</td>\n",
              "      <td>1</td>\n",
              "      <td>19/08/2022</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>733445</th>\n",
              "      <td>919822</td>\n",
              "      <td>155</td>\n",
              "      <td>F</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>B</td>\n",
              "      <td>227</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>ARROZ</td>\n",
              "      <td>2</td>\n",
              "      <td>19/08/2022</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>733446</th>\n",
              "      <td>919822</td>\n",
              "      <td>155</td>\n",
              "      <td>F</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>B</td>\n",
              "      <td>228</td>\n",
              "      <td>LIMPEZA</td>\n",
              "      <td>AMACIANTE</td>\n",
              "      <td>1</td>\n",
              "      <td>19/08/2022</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>733447 rows × 11 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6875d8be-627b-4fc2-a40e-962f174aa1a0')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-6875d8be-627b-4fc2-a40e-962f174aa1a0 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-6875d8be-627b-4fc2-a40e-962f174aa1a0');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_ee90f133-1800-4824-8b2c-f82db1c80b0d\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('dados_com_quantidade')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_ee90f133-1800-4824-8b2c-f82db1c80b0d button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('dados_com_quantidade');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "dados_com_quantidade"
            }
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "A junção dos valores duplicados se deve principalmente pela Regra De Negócio que diz que cada linha é um item comprado, por conta disso nenhuma linha duplicada é inútil e todas devem ser análisadas. Para facilitar essa análise fiz as escolhas vistas acima.\n",
        "\n",
        "Feita a limpeza agrupamento e remoção das linhas duplicadas agora seguimos para\n",
        "a validação de valores nulos."
      ],
      "metadata": {
        "id": "-NyMKxML7kY_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **4.2 - Valores Nulos**"
      ],
      "metadata": {
        "id": "2BtCjY5-Db1Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nulos = dados_com_quantidade.isna().sum()\n",
        "print(f\"Valores nulos: \\n{nulos}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xLMQhQPS4EaV",
        "outputId": "6f93fe8e-7738-45c5-a5b1-d3d8fa290370"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Valores nulos: \n",
            "CO_ID            0\n",
            "CL_ID            0\n",
            "CL_GENERO        0\n",
            "CL_EC            0\n",
            "CL_FHL           0\n",
            "CL_SEG           0\n",
            "PR_ID            0\n",
            "PR_CAT        3228\n",
            "PR_NOME       3228\n",
            "QUANTIDADE       0\n",
            "DATA_BR          0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Podemos ver que existem diversas categorias e nome de produto nulos, sabendo disso precisamos descobrir se conseguimos preencher esses valores corretamente ou se é necessários remover eles."
      ],
      "metadata": {
        "id": "fRFTPOOO-UY9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "mapa_categoria = dados_com_quantidade.dropna(subset=[\"PR_CAT\"]).drop_duplicates(\"PR_ID\").set_index(\"PR_ID\")[\"PR_CAT\"]\n",
        "\n",
        "dados_com_quantidade[\"PR_CAT\"] = dados_com_quantidade[\"PR_CAT\"].fillna(dados_com_quantidade[\"PR_ID\"].map(mapa_categoria))"
      ],
      "metadata": {
        "id": "26Qwgn-T9Vd8"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criação de um dicionário para tentar preencher as categorias e nomes nulos com o valor correto de acordo com o ID do produto procurnado produtos de mesmo ID na tabela para coletar os nomes e categorias referentes ao ID."
      ],
      "metadata": {
        "id": "schrk4o6-pD6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Pega quantos produtos unicos tem categoria única\n",
        "ids_com_nulo = dados_com_quantidade.loc[dados_com_quantidade[\"PR_CAT\"].isna(), \"PR_ID\"].unique()\n",
        "print(f\"Quantidade de produtos únicos com categoria nula: {len(ids_com_nulo)}\")\n",
        "\n",
        "# Procura quantos desses produtos tem essa categoria preenchida em outra linha\n",
        "ids_recuperaveis = dados_com_quantidade.loc[dados_com_quantidade[\"PR_ID\"].isin(ids_com_nulo) & dados_com_quantidade[\"PR_CAT\"].notna(), \"PR_ID\"].unique()\n",
        "print(f\"Desses, quantos têm categoria em outra linha: {len(ids_recuperaveis)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wmKOOELr9X5e",
        "outputId": "265f9058-a4e9-4609-e5f7-3b71f0ecbd03"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantidade de produtos únicos com categoria nula: 1\n",
            "Desses, quantos têm categoria em outra linha: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Pega quantos produtos únicos têm nome nulo\n",
        "ids_com_nulo_nome = dados_com_quantidade.loc[dados_com_quantidade[\"PR_NOME\"].isna(), \"PR_ID\"].unique()\n",
        "print(f\"Quantidade de produtos únicos com nome nulo: {len(ids_com_nulo_nome)}\")\n",
        "\n",
        "# Desses produtos, quantos têm o nome preenchido em outra linha\n",
        "ids_recuperaveis_nome = dados_com_quantidade.loc[dados_com_quantidade[\"PR_ID\"].isin(ids_com_nulo_nome) & dados_com_quantidade[\"PR_NOME\"].notna(), \"PR_ID\"].unique()\n",
        "print(f\"Desses, quantos têm nome em outra linha: {len(ids_recuperaveis_nome)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "77kULYCYAb3o",
        "outputId": "78fd5929-f1c8-4b26-86a7-02edd04714fd"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantidade de produtos únicos com nome nulo: 1\n",
            "Desses, quantos têm nome em outra linha: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ao fazer essa visualização dos IDS unicos que tem categoria e nomes nulos podemos entender que todas essas categorias nulas vem de um mesmo produto então precisamos descobrir qual é esse produto."
      ],
      "metadata": {
        "id": "6lpfV0ni_ewW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pr_id_desconhecido = dados_com_quantidade.loc[dados_com_quantidade[\"PR_CAT\"].isna(), \"PR_ID\"].unique()[0]\n",
        "print(f\"PR_ID: {pr_id_desconhecido}\")\n",
        "\n",
        "# Confirma que o nome do produto também está nulo\n",
        "print(dados_com_quantidade.loc[dados_com_quantidade[\"PR_ID\"] == pr_id_desconhecido, [\"PR_ID\", \"PR_CAT\", \"PR_NOME\"]].head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DqgaeYB9-KTd",
        "outputId": "8ef7b0e8-d113-45f0-bebb-a41e4a827d54"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "PR_ID: 107\n",
            "     PR_ID PR_CAT PR_NOME\n",
            "93     107    NaN     NaN\n",
            "190    107    NaN     NaN\n",
            "548    107    NaN     NaN\n",
            "730    107    NaN     NaN\n",
            "791    107    NaN     NaN\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Agora que descobrimos o produto entendemos que esse produto em especifíco esta com algum problema em seus registros que faz com que o seu nome e categoria não estejam informados. Por isso para facilitar visualizações futuras vamos trocar os dados nesses espaços por \"Sem Categoria\" e por \"Sem Nome\" para que qualquer um consiga entender ao visualizar os dados."
      ],
      "metadata": {
        "id": "z0rd5D9iAo_2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_limpos = dados_com_quantidade.copy()\n",
        "linhas, colunas = dados_limpos.shape\n",
        "categorias_corrigidas = False\n",
        "nomes_corrigidos = False\n",
        "n_linha=0\n",
        "for i in range(linhas):\n",
        "  if pd.isna(dados_limpos.loc[i, \"PR_CAT\"]) and categorias_corrigidas == False:\n",
        "    dados_limpos[\"PR_CAT\"] = dados_limpos[\"PR_CAT\"].fillna(\"Sem Categoria\")\n",
        "    categorias_corrigidas = True\n",
        "  if pd.isna(dados_limpos.loc[i, \"PR_NOME\"]) and nomes_corrigidos == False:\n",
        "    dados_limpos[\"PR_NOME\"] = dados_limpos[\"PR_NOME\"].fillna(\"Sem Nome\")\n",
        "    nomes_corrigidos = True\n",
        "  if categorias_corrigidas == True and nomes_corrigidos == True:\n",
        "    print(\"Correção concluida\")\n",
        "  else:\n",
        "    n_linha += 1\n",
        "    continue\n",
        "  print(f\"Número de linhas válidadas até a conclusão: {n_linha}\")\n",
        "  break"
      ],
      "metadata": {
        "id": "WVuPgAa6BAyH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bbf7d0e0-ebd9-47f3-9056-2940b04205f8"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Correção concluida\n",
            "Número de linhas válidadas até a conclusão: 93\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Validação feita para procurar se algum valor em categoria ou em nome é nulo mesmo e após isso trocar todos os valores vazios por um aviso de \"Sem Categoria\" ou \"Sem Nome\" com um if final para verificar se as alterações ja foram feitas e cancelar o loop que levaria muito tempo para passar por todos os valores considerando o grande número de registros.\n",
        "\n",
        "Obs: Essa etapa poderia ter sido feita utilizando apenas \"dados_limpos[\"PR_CAT\"] = dados_limpos[\"PR_CAT\"].fillna(\"Sem Categoria\")\" e \"dados_limpos[\"PR_NOME\"] = dados_limpos[\"PR_NOME\"].fillna(\"Sem Nome\")\" no entanto como o documento pede que seja feito o uso de If e Else achei interessante criar um loop que diga quantas linhas precisaram ser validadas para encontrar ao menos um nome nulo e uma categoria nula."
      ],
      "metadata": {
        "id": "sYLIWhzC2N_s"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(dados_limpos.loc[dados_com_quantidade[\"PR_ID\"] == pr_id_desconhecido, [\"PR_ID\", \"PR_CAT\", \"PR_NOME\"]].head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WO_IHwWb2IoS",
        "outputId": "2afd597a-a471-4485-bec8-28e4a8b83b77"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     PR_ID         PR_CAT   PR_NOME\n",
            "93     107  Sem Categoria  Sem Nome\n",
            "190    107  Sem Categoria  Sem Nome\n",
            "548    107  Sem Categoria  Sem Nome\n",
            "730    107  Sem Categoria  Sem Nome\n",
            "791    107  Sem Categoria  Sem Nome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nulos = dados_limpos.isna().sum()\n",
        "print(f\"Valores nulos: \\n{nulos}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iHUNVH7J7ofc",
        "outputId": "c945c5a7-67d2-4b27-c350-08377501577b"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Valores nulos: \n",
            "CO_ID         0\n",
            "CL_ID         0\n",
            "CL_GENERO     0\n",
            "CL_EC         0\n",
            "CL_FHL        0\n",
            "CL_SEG        0\n",
            "PR_ID         0\n",
            "PR_CAT        0\n",
            "PR_NOME       0\n",
            "QUANTIDADE    0\n",
            "DATA_BR       0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Podemos ver que a alteração dos valores foi muito bem sucedida. Após a limpeza e validação de valores nulos e duplicados precisamos validas e converter as Datas de Registro."
      ],
      "metadata": {
        "id": "I5Mk6EqpCWII"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **4.3 - Conversão e Validação das Datas**"
      ],
      "metadata": {
        "id": "xy8yoMEdDxq5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_data = dados_limpos.copy()\n",
        "\n",
        "dados_data[\"DATA_INT\"] = pd.to_datetime(dados_data[\"DATA_BR\"], format=\"%d/%m/%Y\", errors=\"coerce\")"
      ],
      "metadata": {
        "id": "YWd_ueLVD1tb"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dados_data.head(3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 144
        },
        "id": "w-IEaWYBEQR1",
        "outputId": "c0ca143b-7766-45b0-92d8-8676de6533ca"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   CO_ID  CL_ID CL_GENERO  CL_EC  CL_FHL CL_SEG  PR_ID     PR_CAT  PR_NOME  \\\n",
              "0   1000    534         M      4       1      C      4  ALIMENTOS  ABACAXI   \n",
              "1   1000    534         M      4       1      C     11  ALIMENTOS   AZEITE   \n",
              "2   1000    534         M      4       1      C     13  ALIMENTOS   BANANA   \n",
              "\n",
              "   QUANTIDADE     DATA_BR   DATA_INT  \n",
              "0           2  01/02/2019 2019-02-01  \n",
              "1           2  01/02/2019 2019-02-01  \n",
              "2           2  01/02/2019 2019-02-01  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-dc03df22-dbe6-42d5-b416-c49ec810a2c4\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>CO_ID</th>\n",
              "      <th>CL_ID</th>\n",
              "      <th>CL_GENERO</th>\n",
              "      <th>CL_EC</th>\n",
              "      <th>CL_FHL</th>\n",
              "      <th>CL_SEG</th>\n",
              "      <th>PR_ID</th>\n",
              "      <th>PR_CAT</th>\n",
              "      <th>PR_NOME</th>\n",
              "      <th>QUANTIDADE</th>\n",
              "      <th>DATA_BR</th>\n",
              "      <th>DATA_INT</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>4</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>ABACAXI</td>\n",
              "      <td>2</td>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>2019-02-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>11</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>AZEITE</td>\n",
              "      <td>2</td>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>2019-02-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1000</td>\n",
              "      <td>534</td>\n",
              "      <td>M</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>13</td>\n",
              "      <td>ALIMENTOS</td>\n",
              "      <td>BANANA</td>\n",
              "      <td>2</td>\n",
              "      <td>01/02/2019</td>\n",
              "      <td>2019-02-01</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-dc03df22-dbe6-42d5-b416-c49ec810a2c4')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-dc03df22-dbe6-42d5-b416-c49ec810a2c4 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-dc03df22-dbe6-42d5-b416-c49ec810a2c4');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "dados_data"
            }
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "datas_invalidas = dados_data[\"DATA_INT\"].isna().sum()\n",
        "print(f\"Datas inválidas: {datas_invalidas}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bHVyvG15EIva",
        "outputId": "e68541c2-2f7d-4e98-cdf1-81555f515a96"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Datas inválidas: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Após validar as datas agora e converter elas separando em DATA_BR(STRING) que facilita entendimento de brasileiros e DATA_INT(DATE_TIME) em formato internacional que facilita análises podemos ir para a próxima etapa que é o agrupamento de informações relevantes e separação correta dos dados para análise."
      ],
      "metadata": {
        "id": "eOiS81JMENV3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **6 - Agrupamento de Dados**"
      ],
      "metadata": {
        "id": "NfyRvQc7Dl6q"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **AGRUPAMENTO DE COMPRAS:**"
      ],
      "metadata": {
        "id": "iVWZFTd758Tm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "compras_agrupadas = dados_data.groupby(\"CO_ID\", as_index=False).agg(\n",
        "    CL_ID=(\"CL_ID\", \"first\"),           # O cliente é sempre o mesmo então podemos pegar somente o primeiro\n",
        "    DATA_INT=(\"DATA_INT\", \"first\"),       # A data da compra também é a mesma então podemos pegar o primeiro\n",
        "    QTD_TOTAL_ITENS=(\"QUANTIDADE\", \"sum\"),      # Soma quantidade total de itens comprados\n",
        "    QTD_PRODUTOS_DIFERENTES=(\"PR_ID\", \"nunique\"),# Soma quantidade de itens diferentes na compra\n",
        "    PRODUTOS=(\"PR_NOME\", list),         # Lista o nome de todos os produtos comprados\n",
        "    DATA_COMPRA=(\"DATA_INT\", \"first\")\n",
        ")\n",
        "\n",
        "compras_agrupadas.head(10).style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 676
        },
        "id": "F8KP9PTsDqwA",
        "outputId": "b7c01822-b825-43b3-8501-02f5f16ee25a"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b4916a0>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_60422\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_60422_level0_col0\" class=\"col_heading level0 col0\" >CO_ID</th>\n",
              "      <th id=\"T_60422_level0_col1\" class=\"col_heading level0 col1\" >CL_ID</th>\n",
              "      <th id=\"T_60422_level0_col2\" class=\"col_heading level0 col2\" >DATA_INT</th>\n",
              "      <th id=\"T_60422_level0_col3\" class=\"col_heading level0 col3\" >QTD_TOTAL_ITENS</th>\n",
              "      <th id=\"T_60422_level0_col4\" class=\"col_heading level0 col4\" >QTD_PRODUTOS_DIFERENTES</th>\n",
              "      <th id=\"T_60422_level0_col5\" class=\"col_heading level0 col5\" >PRODUTOS</th>\n",
              "      <th id=\"T_60422_level0_col6\" class=\"col_heading level0 col6\" >DATA_COMPRA</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row0_col0\" class=\"data row0 col0\" >1000</td>\n",
              "      <td id=\"T_60422_row0_col1\" class=\"data row0 col1\" >534</td>\n",
              "      <td id=\"T_60422_row0_col2\" class=\"data row0 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row0_col3\" class=\"data row0 col3\" >52</td>\n",
              "      <td id=\"T_60422_row0_col4\" class=\"data row0 col4\" >46</td>\n",
              "      <td id=\"T_60422_row0_col5\" class=\"data row0 col5\" >['ABACAXI', 'AZEITE', 'BANANA', 'COGUMELOS', 'COPA SUINA', 'CORACAO DE FRANGO', 'PATE', 'QUEIJO MUSSARELA', 'SARDINHA', 'UVA', 'REFRIGERANTE COLA', 'REFRIGERANTE GUARANA', 'REFRIGERANTE LARANJA', 'REFRIGERANTE LIMaO', 'REFRIGERANTE OUTROS', 'PAPEL HIGIENICO', 'PRESERVATIVO', 'REPELENTE', 'AMACIANTE', 'REMOVEDOR', 'UVA', 'TIRA MANCHA', 'SABONETE', 'RODO', 'RICOTA', 'REFRIGERANTE GUARANA', 'QUEIJO MUSSARELA', 'PATE', 'PALMITO', 'MORTADELA', 'LIMPADOR MULTIUSO', 'LIMPA VIDROS', 'LENCO UMEDECIDO', 'LATA DE ERVILHA', 'KETCHUP', 'HASTES FLEXIVEIS', 'GRANOLA', 'FRALDA', 'ENERGETICO', 'DETERGENTE', 'COGUMELOS', 'BIFE DE COXAO MOLE', 'BANANA', 'ATUM', 'ARROZ INTEGRAL', 'ALMONDEGA']</td>\n",
              "      <td id=\"T_60422_row0_col6\" class=\"data row0 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row1_col0\" class=\"data row1 col0\" >1040</td>\n",
              "      <td id=\"T_60422_row1_col1\" class=\"data row1 col1\" >279</td>\n",
              "      <td id=\"T_60422_row1_col2\" class=\"data row1 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row1_col3\" class=\"data row1 col3\" >15</td>\n",
              "      <td id=\"T_60422_row1_col4\" class=\"data row1 col4\" >15</td>\n",
              "      <td id=\"T_60422_row1_col5\" class=\"data row1 col5\" >['CAFE', 'LEITE CONDENSADO', 'MAMAO PAPAYA', 'OVOS', 'SALGADINHOS DE MILHO', 'ESCOVA DE DENTE', 'ALCOOL', 'AMACIANTE', 'LUSTRA MOVEIS', 'SABAO', 'RACAO UMIDA PARA GATOS', 'QUEIJO MUSSARELA', 'MORDEDOR', 'LEITE', 'CONDICIONADOR']</td>\n",
              "      <td id=\"T_60422_row1_col6\" class=\"data row1 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row2_col0\" class=\"data row2 col0\" >1078</td>\n",
              "      <td id=\"T_60422_row2_col1\" class=\"data row2 col1\" >290</td>\n",
              "      <td id=\"T_60422_row2_col2\" class=\"data row2 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row2_col3\" class=\"data row2 col3\" >82</td>\n",
              "      <td id=\"T_60422_row2_col4\" class=\"data row2 col4\" >63</td>\n",
              "      <td id=\"T_60422_row2_col5\" class=\"data row2 col5\" >['CHUPETA', 'ACHOCOLATADO', 'ALHO', 'BANANA', 'BATATA', 'BISCOITO', 'CAFE', 'CENOURA', 'CHA', 'COGUMELOS', 'CORACAO DE FRANGO', 'FILE DE PEIXE', 'LATA DE ERVILHA', 'LATA DE MILHO', 'LIMAO', 'MAMAO', 'OVOS', 'PALMITO', 'QUEIJO MUSSARELA', 'SALGADINHO', 'SNACKS', 'TOMATE', 'FIO DENTAL', 'HIDRATANTE', 'LENCO UMEDECIDO', 'PAPEL HIGIENICO', 'SHAMPOO', 'AGUA SANITARIA', 'DESINFETANTE', 'LIMPA VIDROS', 'LUSTRA MOVEIS', 'ODORIZADOR', 'Sem Nome', 'RODO', 'TIRA MANCHA', 'RACAO SECA PARA CAES', 'RACAO UMIDA PARA CAES', 'TOMATE', 'TIRA MANCHA', 'TINTURAS', 'SARDINHA', 'RICOTA', 'REQUEIJAO', 'REFRIGERANTE COLA', 'RACAO UMIDA PARA GATOS', 'QUEIJO DE CABRA', 'PROTETOR SOLAR', 'PATE', 'PASTA DE DENTE', 'PALMITO', 'ODORIZADOR', 'LUSTRA MOVEIS', 'LINGUICA', 'LIMPADOR PERFUMADO', 'LEITE', 'GEL', 'FRALDA', 'FIXADOR', 'DETERGENTE', 'CHUPETA', 'CENOURA', 'CAFE', 'ATUM']</td>\n",
              "      <td id=\"T_60422_row2_col6\" class=\"data row2 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row3_col0\" class=\"data row3 col0\" >1082</td>\n",
              "      <td id=\"T_60422_row3_col1\" class=\"data row3 col1\" >323</td>\n",
              "      <td id=\"T_60422_row3_col2\" class=\"data row3 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row3_col3\" class=\"data row3 col3\" >71</td>\n",
              "      <td id=\"T_60422_row3_col4\" class=\"data row3 col4\" >62</td>\n",
              "      <td id=\"T_60422_row3_col5\" class=\"data row3 col5\" >['ALMONDEGA', 'AZEITE', 'CAFE', 'DANETTE', 'FILE DE PEIXE', 'LATA DE ERVILHA', 'LEITE CONDENSADO', 'MACARRAO INSTANTANEO', 'MAMAO', 'OVOS', 'PAPINHA INFANTIL', 'PATE', 'PRESUNTO COZIDO', 'PRESUNTO COZIDO', 'SALGADINHO', 'REFRIGERANTE LARANJA', 'REFRIGERANTE LIMaO', 'REFRIGERANTE OUTROS', 'FIO DENTAL', 'FRALDA', 'HASTES FLEXIVEIS', 'PAPEL HIGIENICO', 'PASTA DE DENTE', 'ALCOOL', 'AMACIANTE', 'CERA', 'DESENGORDURANTE', 'SABAO', 'SABAO EM PO', 'TIRA MANCHA', 'VASSOURA', 'RACAO SECA PARA GATOS', 'TOMATE', 'TIRA LIMO', 'TINTURAS', 'TALCO', 'SABAO', 'RODO', 'REFRIGERANTE LIMaO', 'REFRIGERANTE LARANJA', 'REFRIGERANTE GUARANA', 'RACAO UMIDA PARA CAES', 'PRESERVATIVO', 'PASTA DE DENTE', 'PAPINHA INFANTIL', 'PALMITO', 'MODELADOR', 'LUSTRA MOVEIS', 'LINGUICA', 'LEITE', 'INSETICIDA', 'HASTES FLEXIVEIS', 'GEL', 'FEIJAO', 'ENERGETICO', 'DESINFETANTE', 'CREME', 'CERA', 'CENOURA', 'BATATA', 'AMACIANTE', 'ALMONDEGA']</td>\n",
              "      <td id=\"T_60422_row3_col6\" class=\"data row3 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row4_col0\" class=\"data row4 col0\" >1103</td>\n",
              "      <td id=\"T_60422_row4_col1\" class=\"data row4 col1\" >957</td>\n",
              "      <td id=\"T_60422_row4_col2\" class=\"data row4 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row4_col3\" class=\"data row4 col3\" >6</td>\n",
              "      <td id=\"T_60422_row4_col4\" class=\"data row4 col4\" >6</td>\n",
              "      <td id=\"T_60422_row4_col5\" class=\"data row4 col5\" >['BATATA DOCE', 'DANETTE', 'DOCE', 'PROTETOR SOLAR', 'Sem Nome', 'LATA DE ERVILHA']</td>\n",
              "      <td id=\"T_60422_row4_col6\" class=\"data row4 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row5_col0\" class=\"data row5 col0\" >1121</td>\n",
              "      <td id=\"T_60422_row5_col1\" class=\"data row5 col1\" >49</td>\n",
              "      <td id=\"T_60422_row5_col2\" class=\"data row5 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row5_col3\" class=\"data row5 col3\" >64</td>\n",
              "      <td id=\"T_60422_row5_col4\" class=\"data row5 col4\" >54</td>\n",
              "      <td id=\"T_60422_row5_col5\" class=\"data row5 col5\" >['ABACAXI', 'AZEITONA', 'BATATA DOCE', 'BROCOLIS', 'CENOURA', 'COPA SUINA', 'DOCE', 'HAMBUGUER', 'LATA DE MILHO', 'MAMAO PAPAYA', 'PAO DE FORMA', 'PATE', 'UVA', 'ENERGETICO', 'ESCOVA DE DENTE', 'HASTES FLEXIVEIS', 'LENCO UMEDECIDO', 'PROTETOR SOLAR', 'TALCO', 'TINTURAS', 'AGUA SANITARIA', 'BALDE', 'DESINFETANTE', 'DETERGENTE', 'LIMPA VIDROS', 'REMOVEDOR', 'VASSOURA', 'RACAO SECA PARA CAES', 'RACAO UMIDA PARA GATOS', 'TIRA MANCHA', 'TINTURAS', 'SHAMPOO', 'SARDINHA', 'RACAO UMIDA PARA CAES', 'RACAO SECA PARA CAES', 'PROTETOR SOLAR', 'PAO DE FORMA', 'PALMITO', 'OVOS', 'MORDEDOR', 'MAMAO', 'MACARRAO', 'LINGUICA', 'LIMPADOR PERFUMADO', 'LEITE', 'IOGURTE', 'INSETICIDA', 'COPA SUINA', 'COGUMELOS', 'BISCOITO', 'BATATA', 'BALDE', 'AZEITONA', 'ARROZ INTEGRAL']</td>\n",
              "      <td id=\"T_60422_row5_col6\" class=\"data row5 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row6_col0\" class=\"data row6 col0\" >1188</td>\n",
              "      <td id=\"T_60422_row6_col1\" class=\"data row6 col1\" >906</td>\n",
              "      <td id=\"T_60422_row6_col2\" class=\"data row6 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row6_col3\" class=\"data row6 col3\" >78</td>\n",
              "      <td id=\"T_60422_row6_col4\" class=\"data row6 col4\" >67</td>\n",
              "      <td id=\"T_60422_row6_col5\" class=\"data row6 col5\" >['CHUPETA', 'ABACAXI', 'BROCOLIS', 'CAFE', 'CORACAO DE FRANGO', 'DANETTE', 'FEIJAO', 'LATA DE ERVILHA', 'LEITE CONDENSADO', 'LIMAO', 'MACARRAO', 'MAMAO', 'PALMITO', 'PAO DE FORMA', 'QUEIJO DE CABRA', 'QUEIJO MUSSARELA', 'REQUEIJAO', 'SALGADINHOS DE MILHO', 'SNACKS', 'UVA', 'CONDICIONADOR', 'ESCOVA DE DENTE', 'FIO DENTAL', 'FRALDA', 'HASTES FLEXIVEIS', 'PRESERVATIVO', 'PROTETOR SOLAR', 'SHAMPOO', 'TALCO', 'TINTURAS', 'AGUA SANITARIA', 'AMACIANTE', 'BALDE', 'INSETICIDA', 'LIMPADOR MULTIUSO', 'ALIMENTO PARA PASSARO', 'RACAO SECA PARA GATOS', 'RACAO UMIDA PARA GATOS', 'UVA', 'SABONETE', 'SABAO', 'RODO', 'RICOTA', 'REPELENTE', 'REFRIGERANTE OUTROS', 'RACAO UMIDA PARA GATOS', 'RACAO SECA PARA CAES', 'PALMITO', 'OVOS', 'MORTADELA', 'MACARRAO INSTANTANEO', 'LIMPADOR MULTIUSO', 'LIMAO', 'KETCHUP', 'HIDRATANTE', 'FIO DENTAL', 'FEIJAO', 'ENXAGUANTE BUCAL', 'ENERGETICO', 'DOCE', 'DESENGORDURANTE', 'CORACAO DE FRANGO', 'COPA SUINA', 'CEBOLA', 'BROCOLIS', 'BATATA DOCE', 'ARROZ INTEGRAL']</td>\n",
              "      <td id=\"T_60422_row6_col6\" class=\"data row6 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row7_col0\" class=\"data row7 col0\" >1200</td>\n",
              "      <td id=\"T_60422_row7_col1\" class=\"data row7 col1\" >653</td>\n",
              "      <td id=\"T_60422_row7_col2\" class=\"data row7 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row7_col3\" class=\"data row7 col3\" >81</td>\n",
              "      <td id=\"T_60422_row7_col4\" class=\"data row7 col4\" >70</td>\n",
              "      <td id=\"T_60422_row7_col5\" class=\"data row7 col5\" >['CHUPETA', 'ABACATE', 'ABACAXI', 'ALMONDEGA', 'AZEITONA', 'COGUMELOS', 'CORACAO DE FRANGO', 'COXA E SOBRECOXA DE FRANGO', 'KETCHUP', 'LATA DE ERVILHA', 'LINGUICA', 'MACARRAO', 'MACARRAO INSTANTANEO', 'MAMAO', 'MANGA', 'MORTADELA', 'OVOS', 'PRESUNTO COZIDO', 'SALGADINHOS DE MILHO', 'REFRIGERANTE GUARANA', 'REFRIGERANTE LARANJA', 'ABSORVENTE', 'CONDICIONADOR', 'ESCOVA DE DENTE', 'FIXADOR', 'FRALDA', 'GEL', 'PAPEL HIGIENICO', 'PROTETOR SOLAR', 'REPELENTE', 'TINTURAS', 'ALCOOL', 'AMACIANTE', 'DESENGORDURANTE', 'LIMPA VIDROS', 'LIMPADOR PERFUMADO', 'REMOVEDOR', 'TIRA MANCHA', 'RACAO SECA PARA CAES', 'UVA', 'TALCO', 'SHAMPOO', 'SARDINHA', 'SALGADINHOS DE MILHO', 'SABONETE', 'SABAO', 'REFRIGERANTE LARANJA', 'PAO DE FORMA', 'PALMITO', 'MAMAO PAPAYA', 'LINGUICA', 'LIMAO', 'LEITE', 'LATA DE ERVILHA', 'IOGURTE', 'INSETICIDA', 'HIDRATANTE', 'GRANOLA', 'GEL', 'FIXADOR', 'FIO DENTAL', 'FILE DE PEIXE', 'DETERGENTE', 'COXA E SOBRECOXA DE FRANGO', 'CEBOLA', 'BIFE DE COXAO MOLE', 'BANANA', 'ATUM', 'ARROZ', 'AMACIANTE']</td>\n",
              "      <td id=\"T_60422_row7_col6\" class=\"data row7 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row8_col0\" class=\"data row8 col0\" >1240</td>\n",
              "      <td id=\"T_60422_row8_col1\" class=\"data row8 col1\" >842</td>\n",
              "      <td id=\"T_60422_row8_col2\" class=\"data row8 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row8_col3\" class=\"data row8 col3\" >37</td>\n",
              "      <td id=\"T_60422_row8_col4\" class=\"data row8 col4\" >33</td>\n",
              "      <td id=\"T_60422_row8_col5\" class=\"data row8 col5\" >['ABACAXI', 'BISCOITO', 'CHA', 'PATE', 'SNACKS', 'ENERGETICO', 'REFRIGERANTE LARANJA', 'PASTA DE DENTE', 'ALCOOL', 'BALDE', 'LIMPADOR PERFUMADO', 'LUSTRA MOVEIS', 'ALIMENTO PARA PASSARO', 'RACAO SECA PARA GATOS', 'RACAO UMIDA PARA GATOS', 'TINTURAS', 'SABAO', 'RICOTA', 'REMOVEDOR', 'RACAO SECA PARA CAES', 'PROTETOR SOLAR', 'PRESUNTO COZIDO', 'OVOS', 'MODELADOR', 'LUSTRA MOVEIS', 'LIMPADOR MULTIUSO', 'LATA DE ERVILHA', 'ENXAGUANTE BUCAL', 'CREME', 'CONDICIONADOR', 'BISCOITO', 'BIFE DE COXAO MOLE', 'ARROZ INTEGRAL']</td>\n",
              "      <td id=\"T_60422_row8_col6\" class=\"data row8 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_60422_row9_col0\" class=\"data row9 col0\" >1293</td>\n",
              "      <td id=\"T_60422_row9_col1\" class=\"data row9 col1\" >616</td>\n",
              "      <td id=\"T_60422_row9_col2\" class=\"data row9 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_60422_row9_col3\" class=\"data row9 col3\" >8</td>\n",
              "      <td id=\"T_60422_row9_col4\" class=\"data row9 col4\" >8</td>\n",
              "      <td id=\"T_60422_row9_col5\" class=\"data row9 col5\" >['ACHOCOLATADO', 'LATA DE ERVILHA', 'MAMAO PAPAYA', 'ENERGETICO', 'CERA', 'TALCO', 'SHAMPOO', 'LEITE CONDENSADO']</td>\n",
              "      <td id=\"T_60422_row9_col6\" class=\"data row9 col6\" >2019-02-01 00:00:00</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Compreensão da RN relacionada a CO_ID fazendo agrupamento dos itens de uma mesma compra para uso dem análises posteriores."
      ],
      "metadata": {
        "id": "02Bb65Pk7o5t"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **AGRUPAMENTO DE CLIENTES:**"
      ],
      "metadata": {
        "id": "3aAWOi-G7gHq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "clientes = dados_data.groupby(\"CL_ID\",as_index=False).agg(\n",
        "    GENERO=(\"CL_GENERO\", \"first\"),\n",
        "    ESTADO_CIVIL=(\"CL_EC\", \"first\"),\n",
        "    NUMERO_FILHOS=(\"CL_FHL\", \"first\"),\n",
        "    SEGMENTO_ECONOMICO=(\"CL_SEG\", \"first\")\n",
        ")\n",
        "\n",
        "clientes.head(10).style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 364
        },
        "id": "2SNrIJ139z7Q",
        "outputId": "bf6def85-f8c0-4810-f730-82ba6701c4b5"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b74b390>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_97aeb\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_97aeb_level0_col0\" class=\"col_heading level0 col0\" >CL_ID</th>\n",
              "      <th id=\"T_97aeb_level0_col1\" class=\"col_heading level0 col1\" >GENERO</th>\n",
              "      <th id=\"T_97aeb_level0_col2\" class=\"col_heading level0 col2\" >ESTADO_CIVIL</th>\n",
              "      <th id=\"T_97aeb_level0_col3\" class=\"col_heading level0 col3\" >NUMERO_FILHOS</th>\n",
              "      <th id=\"T_97aeb_level0_col4\" class=\"col_heading level0 col4\" >SEGMENTO_ECONOMICO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row0_col0\" class=\"data row0 col0\" >1</td>\n",
              "      <td id=\"T_97aeb_row0_col1\" class=\"data row0 col1\" >M</td>\n",
              "      <td id=\"T_97aeb_row0_col2\" class=\"data row0 col2\" >1</td>\n",
              "      <td id=\"T_97aeb_row0_col3\" class=\"data row0 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row0_col4\" class=\"data row0 col4\" >C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row1_col0\" class=\"data row1 col0\" >2</td>\n",
              "      <td id=\"T_97aeb_row1_col1\" class=\"data row1 col1\" >M</td>\n",
              "      <td id=\"T_97aeb_row1_col2\" class=\"data row1 col2\" >3</td>\n",
              "      <td id=\"T_97aeb_row1_col3\" class=\"data row1 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row1_col4\" class=\"data row1 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row2_col0\" class=\"data row2 col0\" >3</td>\n",
              "      <td id=\"T_97aeb_row2_col1\" class=\"data row2 col1\" >F</td>\n",
              "      <td id=\"T_97aeb_row2_col2\" class=\"data row2 col2\" >4</td>\n",
              "      <td id=\"T_97aeb_row2_col3\" class=\"data row2 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row2_col4\" class=\"data row2 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row3_col0\" class=\"data row3 col0\" >4</td>\n",
              "      <td id=\"T_97aeb_row3_col1\" class=\"data row3 col1\" >M</td>\n",
              "      <td id=\"T_97aeb_row3_col2\" class=\"data row3 col2\" >4</td>\n",
              "      <td id=\"T_97aeb_row3_col3\" class=\"data row3 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row3_col4\" class=\"data row3 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row4_col0\" class=\"data row4 col0\" >5</td>\n",
              "      <td id=\"T_97aeb_row4_col1\" class=\"data row4 col1\" >F</td>\n",
              "      <td id=\"T_97aeb_row4_col2\" class=\"data row4 col2\" >4</td>\n",
              "      <td id=\"T_97aeb_row4_col3\" class=\"data row4 col3\" >3</td>\n",
              "      <td id=\"T_97aeb_row4_col4\" class=\"data row4 col4\" >C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row5_col0\" class=\"data row5 col0\" >6</td>\n",
              "      <td id=\"T_97aeb_row5_col1\" class=\"data row5 col1\" >F</td>\n",
              "      <td id=\"T_97aeb_row5_col2\" class=\"data row5 col2\" >2</td>\n",
              "      <td id=\"T_97aeb_row5_col3\" class=\"data row5 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row5_col4\" class=\"data row5 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row6_col0\" class=\"data row6 col0\" >7</td>\n",
              "      <td id=\"T_97aeb_row6_col1\" class=\"data row6 col1\" >M</td>\n",
              "      <td id=\"T_97aeb_row6_col2\" class=\"data row6 col2\" >1</td>\n",
              "      <td id=\"T_97aeb_row6_col3\" class=\"data row6 col3\" >3</td>\n",
              "      <td id=\"T_97aeb_row6_col4\" class=\"data row6 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row7_col0\" class=\"data row7 col0\" >8</td>\n",
              "      <td id=\"T_97aeb_row7_col1\" class=\"data row7 col1\" >F</td>\n",
              "      <td id=\"T_97aeb_row7_col2\" class=\"data row7 col2\" >3</td>\n",
              "      <td id=\"T_97aeb_row7_col3\" class=\"data row7 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row7_col4\" class=\"data row7 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row8_col0\" class=\"data row8 col0\" >9</td>\n",
              "      <td id=\"T_97aeb_row8_col1\" class=\"data row8 col1\" >F</td>\n",
              "      <td id=\"T_97aeb_row8_col2\" class=\"data row8 col2\" >2</td>\n",
              "      <td id=\"T_97aeb_row8_col3\" class=\"data row8 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row8_col4\" class=\"data row8 col4\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_97aeb_row9_col0\" class=\"data row9 col0\" >10</td>\n",
              "      <td id=\"T_97aeb_row9_col1\" class=\"data row9 col1\" >M</td>\n",
              "      <td id=\"T_97aeb_row9_col2\" class=\"data row9 col2\" >1</td>\n",
              "      <td id=\"T_97aeb_row9_col3\" class=\"data row9 col3\" >0</td>\n",
              "      <td id=\"T_97aeb_row9_col4\" class=\"data row9 col4\" >B</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **AGRUPAMENTO GERAL DOS DADOS COM COMPRAS AGRUPADAS E DADOS DOS CLIENTES:**"
      ],
      "metadata": {
        "id": "QGzMobOgGu_C"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "clientes = clientes.reset_index()\n",
        "\n",
        "dados_gerais = pd.merge(\n",
        "    compras_agrupadas,\n",
        "    clientes,\n",
        "    on=\"CL_ID\",\n",
        "    how=\"left\"\n",
        ")\n",
        "dados_gerais.head(10).style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 763
        },
        "id": "F8ONYGfJDi8F",
        "outputId": "bee8a2da-d67a-4ca2-d070-e248ea170299"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b6139d0>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_3403f\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_3403f_level0_col0\" class=\"col_heading level0 col0\" >CO_ID</th>\n",
              "      <th id=\"T_3403f_level0_col1\" class=\"col_heading level0 col1\" >CL_ID</th>\n",
              "      <th id=\"T_3403f_level0_col2\" class=\"col_heading level0 col2\" >DATA_INT</th>\n",
              "      <th id=\"T_3403f_level0_col3\" class=\"col_heading level0 col3\" >QTD_TOTAL_ITENS</th>\n",
              "      <th id=\"T_3403f_level0_col4\" class=\"col_heading level0 col4\" >QTD_PRODUTOS_DIFERENTES</th>\n",
              "      <th id=\"T_3403f_level0_col5\" class=\"col_heading level0 col5\" >PRODUTOS</th>\n",
              "      <th id=\"T_3403f_level0_col6\" class=\"col_heading level0 col6\" >DATA_COMPRA</th>\n",
              "      <th id=\"T_3403f_level0_col7\" class=\"col_heading level0 col7\" >index</th>\n",
              "      <th id=\"T_3403f_level0_col8\" class=\"col_heading level0 col8\" >GENERO</th>\n",
              "      <th id=\"T_3403f_level0_col9\" class=\"col_heading level0 col9\" >ESTADO_CIVIL</th>\n",
              "      <th id=\"T_3403f_level0_col10\" class=\"col_heading level0 col10\" >NUMERO_FILHOS</th>\n",
              "      <th id=\"T_3403f_level0_col11\" class=\"col_heading level0 col11\" >SEGMENTO_ECONOMICO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row0_col0\" class=\"data row0 col0\" >1000</td>\n",
              "      <td id=\"T_3403f_row0_col1\" class=\"data row0 col1\" >534</td>\n",
              "      <td id=\"T_3403f_row0_col2\" class=\"data row0 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row0_col3\" class=\"data row0 col3\" >52</td>\n",
              "      <td id=\"T_3403f_row0_col4\" class=\"data row0 col4\" >46</td>\n",
              "      <td id=\"T_3403f_row0_col5\" class=\"data row0 col5\" >['ABACAXI', 'AZEITE', 'BANANA', 'COGUMELOS', 'COPA SUINA', 'CORACAO DE FRANGO', 'PATE', 'QUEIJO MUSSARELA', 'SARDINHA', 'UVA', 'REFRIGERANTE COLA', 'REFRIGERANTE GUARANA', 'REFRIGERANTE LARANJA', 'REFRIGERANTE LIMaO', 'REFRIGERANTE OUTROS', 'PAPEL HIGIENICO', 'PRESERVATIVO', 'REPELENTE', 'AMACIANTE', 'REMOVEDOR', 'UVA', 'TIRA MANCHA', 'SABONETE', 'RODO', 'RICOTA', 'REFRIGERANTE GUARANA', 'QUEIJO MUSSARELA', 'PATE', 'PALMITO', 'MORTADELA', 'LIMPADOR MULTIUSO', 'LIMPA VIDROS', 'LENCO UMEDECIDO', 'LATA DE ERVILHA', 'KETCHUP', 'HASTES FLEXIVEIS', 'GRANOLA', 'FRALDA', 'ENERGETICO', 'DETERGENTE', 'COGUMELOS', 'BIFE DE COXAO MOLE', 'BANANA', 'ATUM', 'ARROZ INTEGRAL', 'ALMONDEGA']</td>\n",
              "      <td id=\"T_3403f_row0_col6\" class=\"data row0 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row0_col7\" class=\"data row0 col7\" >533</td>\n",
              "      <td id=\"T_3403f_row0_col8\" class=\"data row0 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row0_col9\" class=\"data row0 col9\" >4</td>\n",
              "      <td id=\"T_3403f_row0_col10\" class=\"data row0 col10\" >1</td>\n",
              "      <td id=\"T_3403f_row0_col11\" class=\"data row0 col11\" >C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row1_col0\" class=\"data row1 col0\" >1040</td>\n",
              "      <td id=\"T_3403f_row1_col1\" class=\"data row1 col1\" >279</td>\n",
              "      <td id=\"T_3403f_row1_col2\" class=\"data row1 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row1_col3\" class=\"data row1 col3\" >15</td>\n",
              "      <td id=\"T_3403f_row1_col4\" class=\"data row1 col4\" >15</td>\n",
              "      <td id=\"T_3403f_row1_col5\" class=\"data row1 col5\" >['CAFE', 'LEITE CONDENSADO', 'MAMAO PAPAYA', 'OVOS', 'SALGADINHOS DE MILHO', 'ESCOVA DE DENTE', 'ALCOOL', 'AMACIANTE', 'LUSTRA MOVEIS', 'SABAO', 'RACAO UMIDA PARA GATOS', 'QUEIJO MUSSARELA', 'MORDEDOR', 'LEITE', 'CONDICIONADOR']</td>\n",
              "      <td id=\"T_3403f_row1_col6\" class=\"data row1 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row1_col7\" class=\"data row1 col7\" >278</td>\n",
              "      <td id=\"T_3403f_row1_col8\" class=\"data row1 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row1_col9\" class=\"data row1 col9\" >1</td>\n",
              "      <td id=\"T_3403f_row1_col10\" class=\"data row1 col10\" >2</td>\n",
              "      <td id=\"T_3403f_row1_col11\" class=\"data row1 col11\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row2_col0\" class=\"data row2 col0\" >1078</td>\n",
              "      <td id=\"T_3403f_row2_col1\" class=\"data row2 col1\" >290</td>\n",
              "      <td id=\"T_3403f_row2_col2\" class=\"data row2 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row2_col3\" class=\"data row2 col3\" >82</td>\n",
              "      <td id=\"T_3403f_row2_col4\" class=\"data row2 col4\" >63</td>\n",
              "      <td id=\"T_3403f_row2_col5\" class=\"data row2 col5\" >['CHUPETA', 'ACHOCOLATADO', 'ALHO', 'BANANA', 'BATATA', 'BISCOITO', 'CAFE', 'CENOURA', 'CHA', 'COGUMELOS', 'CORACAO DE FRANGO', 'FILE DE PEIXE', 'LATA DE ERVILHA', 'LATA DE MILHO', 'LIMAO', 'MAMAO', 'OVOS', 'PALMITO', 'QUEIJO MUSSARELA', 'SALGADINHO', 'SNACKS', 'TOMATE', 'FIO DENTAL', 'HIDRATANTE', 'LENCO UMEDECIDO', 'PAPEL HIGIENICO', 'SHAMPOO', 'AGUA SANITARIA', 'DESINFETANTE', 'LIMPA VIDROS', 'LUSTRA MOVEIS', 'ODORIZADOR', 'Sem Nome', 'RODO', 'TIRA MANCHA', 'RACAO SECA PARA CAES', 'RACAO UMIDA PARA CAES', 'TOMATE', 'TIRA MANCHA', 'TINTURAS', 'SARDINHA', 'RICOTA', 'REQUEIJAO', 'REFRIGERANTE COLA', 'RACAO UMIDA PARA GATOS', 'QUEIJO DE CABRA', 'PROTETOR SOLAR', 'PATE', 'PASTA DE DENTE', 'PALMITO', 'ODORIZADOR', 'LUSTRA MOVEIS', 'LINGUICA', 'LIMPADOR PERFUMADO', 'LEITE', 'GEL', 'FRALDA', 'FIXADOR', 'DETERGENTE', 'CHUPETA', 'CENOURA', 'CAFE', 'ATUM']</td>\n",
              "      <td id=\"T_3403f_row2_col6\" class=\"data row2 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row2_col7\" class=\"data row2 col7\" >289</td>\n",
              "      <td id=\"T_3403f_row2_col8\" class=\"data row2 col8\" >F</td>\n",
              "      <td id=\"T_3403f_row2_col9\" class=\"data row2 col9\" >1</td>\n",
              "      <td id=\"T_3403f_row2_col10\" class=\"data row2 col10\" >0</td>\n",
              "      <td id=\"T_3403f_row2_col11\" class=\"data row2 col11\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row3_col0\" class=\"data row3 col0\" >1082</td>\n",
              "      <td id=\"T_3403f_row3_col1\" class=\"data row3 col1\" >323</td>\n",
              "      <td id=\"T_3403f_row3_col2\" class=\"data row3 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row3_col3\" class=\"data row3 col3\" >71</td>\n",
              "      <td id=\"T_3403f_row3_col4\" class=\"data row3 col4\" >62</td>\n",
              "      <td id=\"T_3403f_row3_col5\" class=\"data row3 col5\" >['ALMONDEGA', 'AZEITE', 'CAFE', 'DANETTE', 'FILE DE PEIXE', 'LATA DE ERVILHA', 'LEITE CONDENSADO', 'MACARRAO INSTANTANEO', 'MAMAO', 'OVOS', 'PAPINHA INFANTIL', 'PATE', 'PRESUNTO COZIDO', 'PRESUNTO COZIDO', 'SALGADINHO', 'REFRIGERANTE LARANJA', 'REFRIGERANTE LIMaO', 'REFRIGERANTE OUTROS', 'FIO DENTAL', 'FRALDA', 'HASTES FLEXIVEIS', 'PAPEL HIGIENICO', 'PASTA DE DENTE', 'ALCOOL', 'AMACIANTE', 'CERA', 'DESENGORDURANTE', 'SABAO', 'SABAO EM PO', 'TIRA MANCHA', 'VASSOURA', 'RACAO SECA PARA GATOS', 'TOMATE', 'TIRA LIMO', 'TINTURAS', 'TALCO', 'SABAO', 'RODO', 'REFRIGERANTE LIMaO', 'REFRIGERANTE LARANJA', 'REFRIGERANTE GUARANA', 'RACAO UMIDA PARA CAES', 'PRESERVATIVO', 'PASTA DE DENTE', 'PAPINHA INFANTIL', 'PALMITO', 'MODELADOR', 'LUSTRA MOVEIS', 'LINGUICA', 'LEITE', 'INSETICIDA', 'HASTES FLEXIVEIS', 'GEL', 'FEIJAO', 'ENERGETICO', 'DESINFETANTE', 'CREME', 'CERA', 'CENOURA', 'BATATA', 'AMACIANTE', 'ALMONDEGA']</td>\n",
              "      <td id=\"T_3403f_row3_col6\" class=\"data row3 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row3_col7\" class=\"data row3 col7\" >322</td>\n",
              "      <td id=\"T_3403f_row3_col8\" class=\"data row3 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row3_col9\" class=\"data row3 col9\" >1</td>\n",
              "      <td id=\"T_3403f_row3_col10\" class=\"data row3 col10\" >3</td>\n",
              "      <td id=\"T_3403f_row3_col11\" class=\"data row3 col11\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row4_col0\" class=\"data row4 col0\" >1103</td>\n",
              "      <td id=\"T_3403f_row4_col1\" class=\"data row4 col1\" >957</td>\n",
              "      <td id=\"T_3403f_row4_col2\" class=\"data row4 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row4_col3\" class=\"data row4 col3\" >6</td>\n",
              "      <td id=\"T_3403f_row4_col4\" class=\"data row4 col4\" >6</td>\n",
              "      <td id=\"T_3403f_row4_col5\" class=\"data row4 col5\" >['BATATA DOCE', 'DANETTE', 'DOCE', 'PROTETOR SOLAR', 'Sem Nome', 'LATA DE ERVILHA']</td>\n",
              "      <td id=\"T_3403f_row4_col6\" class=\"data row4 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row4_col7\" class=\"data row4 col7\" >956</td>\n",
              "      <td id=\"T_3403f_row4_col8\" class=\"data row4 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row4_col9\" class=\"data row4 col9\" >2</td>\n",
              "      <td id=\"T_3403f_row4_col10\" class=\"data row4 col10\" >3</td>\n",
              "      <td id=\"T_3403f_row4_col11\" class=\"data row4 col11\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row5_col0\" class=\"data row5 col0\" >1121</td>\n",
              "      <td id=\"T_3403f_row5_col1\" class=\"data row5 col1\" >49</td>\n",
              "      <td id=\"T_3403f_row5_col2\" class=\"data row5 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row5_col3\" class=\"data row5 col3\" >64</td>\n",
              "      <td id=\"T_3403f_row5_col4\" class=\"data row5 col4\" >54</td>\n",
              "      <td id=\"T_3403f_row5_col5\" class=\"data row5 col5\" >['ABACAXI', 'AZEITONA', 'BATATA DOCE', 'BROCOLIS', 'CENOURA', 'COPA SUINA', 'DOCE', 'HAMBUGUER', 'LATA DE MILHO', 'MAMAO PAPAYA', 'PAO DE FORMA', 'PATE', 'UVA', 'ENERGETICO', 'ESCOVA DE DENTE', 'HASTES FLEXIVEIS', 'LENCO UMEDECIDO', 'PROTETOR SOLAR', 'TALCO', 'TINTURAS', 'AGUA SANITARIA', 'BALDE', 'DESINFETANTE', 'DETERGENTE', 'LIMPA VIDROS', 'REMOVEDOR', 'VASSOURA', 'RACAO SECA PARA CAES', 'RACAO UMIDA PARA GATOS', 'TIRA MANCHA', 'TINTURAS', 'SHAMPOO', 'SARDINHA', 'RACAO UMIDA PARA CAES', 'RACAO SECA PARA CAES', 'PROTETOR SOLAR', 'PAO DE FORMA', 'PALMITO', 'OVOS', 'MORDEDOR', 'MAMAO', 'MACARRAO', 'LINGUICA', 'LIMPADOR PERFUMADO', 'LEITE', 'IOGURTE', 'INSETICIDA', 'COPA SUINA', 'COGUMELOS', 'BISCOITO', 'BATATA', 'BALDE', 'AZEITONA', 'ARROZ INTEGRAL']</td>\n",
              "      <td id=\"T_3403f_row5_col6\" class=\"data row5 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row5_col7\" class=\"data row5 col7\" >48</td>\n",
              "      <td id=\"T_3403f_row5_col8\" class=\"data row5 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row5_col9\" class=\"data row5 col9\" >2</td>\n",
              "      <td id=\"T_3403f_row5_col10\" class=\"data row5 col10\" >0</td>\n",
              "      <td id=\"T_3403f_row5_col11\" class=\"data row5 col11\" >C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row6_col0\" class=\"data row6 col0\" >1188</td>\n",
              "      <td id=\"T_3403f_row6_col1\" class=\"data row6 col1\" >906</td>\n",
              "      <td id=\"T_3403f_row6_col2\" class=\"data row6 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row6_col3\" class=\"data row6 col3\" >78</td>\n",
              "      <td id=\"T_3403f_row6_col4\" class=\"data row6 col4\" >67</td>\n",
              "      <td id=\"T_3403f_row6_col5\" class=\"data row6 col5\" >['CHUPETA', 'ABACAXI', 'BROCOLIS', 'CAFE', 'CORACAO DE FRANGO', 'DANETTE', 'FEIJAO', 'LATA DE ERVILHA', 'LEITE CONDENSADO', 'LIMAO', 'MACARRAO', 'MAMAO', 'PALMITO', 'PAO DE FORMA', 'QUEIJO DE CABRA', 'QUEIJO MUSSARELA', 'REQUEIJAO', 'SALGADINHOS DE MILHO', 'SNACKS', 'UVA', 'CONDICIONADOR', 'ESCOVA DE DENTE', 'FIO DENTAL', 'FRALDA', 'HASTES FLEXIVEIS', 'PRESERVATIVO', 'PROTETOR SOLAR', 'SHAMPOO', 'TALCO', 'TINTURAS', 'AGUA SANITARIA', 'AMACIANTE', 'BALDE', 'INSETICIDA', 'LIMPADOR MULTIUSO', 'ALIMENTO PARA PASSARO', 'RACAO SECA PARA GATOS', 'RACAO UMIDA PARA GATOS', 'UVA', 'SABONETE', 'SABAO', 'RODO', 'RICOTA', 'REPELENTE', 'REFRIGERANTE OUTROS', 'RACAO UMIDA PARA GATOS', 'RACAO SECA PARA CAES', 'PALMITO', 'OVOS', 'MORTADELA', 'MACARRAO INSTANTANEO', 'LIMPADOR MULTIUSO', 'LIMAO', 'KETCHUP', 'HIDRATANTE', 'FIO DENTAL', 'FEIJAO', 'ENXAGUANTE BUCAL', 'ENERGETICO', 'DOCE', 'DESENGORDURANTE', 'CORACAO DE FRANGO', 'COPA SUINA', 'CEBOLA', 'BROCOLIS', 'BATATA DOCE', 'ARROZ INTEGRAL']</td>\n",
              "      <td id=\"T_3403f_row6_col6\" class=\"data row6 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row6_col7\" class=\"data row6 col7\" >905</td>\n",
              "      <td id=\"T_3403f_row6_col8\" class=\"data row6 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row6_col9\" class=\"data row6 col9\" >2</td>\n",
              "      <td id=\"T_3403f_row6_col10\" class=\"data row6 col10\" >0</td>\n",
              "      <td id=\"T_3403f_row6_col11\" class=\"data row6 col11\" >A</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row7_col0\" class=\"data row7 col0\" >1200</td>\n",
              "      <td id=\"T_3403f_row7_col1\" class=\"data row7 col1\" >653</td>\n",
              "      <td id=\"T_3403f_row7_col2\" class=\"data row7 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row7_col3\" class=\"data row7 col3\" >81</td>\n",
              "      <td id=\"T_3403f_row7_col4\" class=\"data row7 col4\" >70</td>\n",
              "      <td id=\"T_3403f_row7_col5\" class=\"data row7 col5\" >['CHUPETA', 'ABACATE', 'ABACAXI', 'ALMONDEGA', 'AZEITONA', 'COGUMELOS', 'CORACAO DE FRANGO', 'COXA E SOBRECOXA DE FRANGO', 'KETCHUP', 'LATA DE ERVILHA', 'LINGUICA', 'MACARRAO', 'MACARRAO INSTANTANEO', 'MAMAO', 'MANGA', 'MORTADELA', 'OVOS', 'PRESUNTO COZIDO', 'SALGADINHOS DE MILHO', 'REFRIGERANTE GUARANA', 'REFRIGERANTE LARANJA', 'ABSORVENTE', 'CONDICIONADOR', 'ESCOVA DE DENTE', 'FIXADOR', 'FRALDA', 'GEL', 'PAPEL HIGIENICO', 'PROTETOR SOLAR', 'REPELENTE', 'TINTURAS', 'ALCOOL', 'AMACIANTE', 'DESENGORDURANTE', 'LIMPA VIDROS', 'LIMPADOR PERFUMADO', 'REMOVEDOR', 'TIRA MANCHA', 'RACAO SECA PARA CAES', 'UVA', 'TALCO', 'SHAMPOO', 'SARDINHA', 'SALGADINHOS DE MILHO', 'SABONETE', 'SABAO', 'REFRIGERANTE LARANJA', 'PAO DE FORMA', 'PALMITO', 'MAMAO PAPAYA', 'LINGUICA', 'LIMAO', 'LEITE', 'LATA DE ERVILHA', 'IOGURTE', 'INSETICIDA', 'HIDRATANTE', 'GRANOLA', 'GEL', 'FIXADOR', 'FIO DENTAL', 'FILE DE PEIXE', 'DETERGENTE', 'COXA E SOBRECOXA DE FRANGO', 'CEBOLA', 'BIFE DE COXAO MOLE', 'BANANA', 'ATUM', 'ARROZ', 'AMACIANTE']</td>\n",
              "      <td id=\"T_3403f_row7_col6\" class=\"data row7 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row7_col7\" class=\"data row7 col7\" >652</td>\n",
              "      <td id=\"T_3403f_row7_col8\" class=\"data row7 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row7_col9\" class=\"data row7 col9\" >2</td>\n",
              "      <td id=\"T_3403f_row7_col10\" class=\"data row7 col10\" >0</td>\n",
              "      <td id=\"T_3403f_row7_col11\" class=\"data row7 col11\" >C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row8_col0\" class=\"data row8 col0\" >1240</td>\n",
              "      <td id=\"T_3403f_row8_col1\" class=\"data row8 col1\" >842</td>\n",
              "      <td id=\"T_3403f_row8_col2\" class=\"data row8 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row8_col3\" class=\"data row8 col3\" >37</td>\n",
              "      <td id=\"T_3403f_row8_col4\" class=\"data row8 col4\" >33</td>\n",
              "      <td id=\"T_3403f_row8_col5\" class=\"data row8 col5\" >['ABACAXI', 'BISCOITO', 'CHA', 'PATE', 'SNACKS', 'ENERGETICO', 'REFRIGERANTE LARANJA', 'PASTA DE DENTE', 'ALCOOL', 'BALDE', 'LIMPADOR PERFUMADO', 'LUSTRA MOVEIS', 'ALIMENTO PARA PASSARO', 'RACAO SECA PARA GATOS', 'RACAO UMIDA PARA GATOS', 'TINTURAS', 'SABAO', 'RICOTA', 'REMOVEDOR', 'RACAO SECA PARA CAES', 'PROTETOR SOLAR', 'PRESUNTO COZIDO', 'OVOS', 'MODELADOR', 'LUSTRA MOVEIS', 'LIMPADOR MULTIUSO', 'LATA DE ERVILHA', 'ENXAGUANTE BUCAL', 'CREME', 'CONDICIONADOR', 'BISCOITO', 'BIFE DE COXAO MOLE', 'ARROZ INTEGRAL']</td>\n",
              "      <td id=\"T_3403f_row8_col6\" class=\"data row8 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row8_col7\" class=\"data row8 col7\" >841</td>\n",
              "      <td id=\"T_3403f_row8_col8\" class=\"data row8 col8\" >M</td>\n",
              "      <td id=\"T_3403f_row8_col9\" class=\"data row8 col9\" >5</td>\n",
              "      <td id=\"T_3403f_row8_col10\" class=\"data row8 col10\" >2</td>\n",
              "      <td id=\"T_3403f_row8_col11\" class=\"data row8 col11\" >B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3403f_row9_col0\" class=\"data row9 col0\" >1293</td>\n",
              "      <td id=\"T_3403f_row9_col1\" class=\"data row9 col1\" >616</td>\n",
              "      <td id=\"T_3403f_row9_col2\" class=\"data row9 col2\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row9_col3\" class=\"data row9 col3\" >8</td>\n",
              "      <td id=\"T_3403f_row9_col4\" class=\"data row9 col4\" >8</td>\n",
              "      <td id=\"T_3403f_row9_col5\" class=\"data row9 col5\" >['ACHOCOLATADO', 'LATA DE ERVILHA', 'MAMAO PAPAYA', 'ENERGETICO', 'CERA', 'TALCO', 'SHAMPOO', 'LEITE CONDENSADO']</td>\n",
              "      <td id=\"T_3403f_row9_col6\" class=\"data row9 col6\" >2019-02-01 00:00:00</td>\n",
              "      <td id=\"T_3403f_row9_col7\" class=\"data row9 col7\" >615</td>\n",
              "      <td id=\"T_3403f_row9_col8\" class=\"data row9 col8\" >F</td>\n",
              "      <td id=\"T_3403f_row9_col9\" class=\"data row9 col9\" >1</td>\n",
              "      <td id=\"T_3403f_row9_col10\" class=\"data row9 col10\" >2</td>\n",
              "      <td id=\"T_3403f_row9_col11\" class=\"data row9 col11\" >C</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Dados utéis para visualizações gerais como compras por segmento, genero, estado civil e cliente, assim como dados mais detalhados como quantidade de itens totais comprados ou itens diferentes."
      ],
      "metadata": {
        "id": "dMVN0ETeHOmm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **AGRUPAMENTO DE DADOS POR SEGMENTO:**"
      ],
      "metadata": {
        "id": "HnxuzTSMHfy-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "resumo_segmento = dados_gerais.groupby(\"SEGMENTO_ECONOMICO\", as_index=False).agg(\n",
        "    NUMERO_DE_CLIENTES=(\"CL_ID\", \"nunique\"),\n",
        "    QUANTIDADE_COMPRAS=(\"CO_ID\", \"nunique\"),\n",
        "    QUANTIDADE_TOTAL_DE_ITENS=(\"QTD_TOTAL_ITENS\", \"sum\")\n",
        ")\n",
        "\n",
        "# Já que produtos foi colocado como list e Produtos unicos não pode ser apenas somado precisamos separar de outra forma\n",
        "produtos_unicos_segmento = dados_gerais.explode(\"PRODUTOS\").groupby(\n",
        "    \"SEGMENTO_ECONOMICO\", as_index=False\n",
        ")[\"PRODUTOS\"].nunique().rename(columns={\"PRODUTOS\": \"QUANTIDADE_DE_ITENS_UNICOS\"})\n",
        "\n",
        "# O Número de filhos precisa ser calculado por cliente único, para que não conte o mesmo cliente uma vez por compra que ele fez\n",
        "clientes_unicos = dados_gerais.drop_duplicates(subset=\"CL_ID\")\n",
        "filhos_segmento = clientes_unicos.groupby(\"SEGMENTO_ECONOMICO\", as_index=False)[\"NUMERO_FILHOS\"].sum()\n",
        "\n",
        "# União dos produtos únicos com os resumo de segmento e número de filhos\n",
        "dados_segmento = pd.merge(resumo_segmento, produtos_unicos_segmento, on=\"SEGMENTO_ECONOMICO\")\n",
        "dados_segmento = pd.merge(dados_segmento, filhos_segmento, on=\"SEGMENTO_ECONOMICO\")\n",
        "dados_segmento.style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 144
        },
        "id": "yB3YRwR4AIGI",
        "outputId": "1e063f3b-bf1b-4db0-e5c7-bb4c87e323af"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b613890>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_8924e\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_8924e_level0_col0\" class=\"col_heading level0 col0\" >SEGMENTO_ECONOMICO</th>\n",
              "      <th id=\"T_8924e_level0_col1\" class=\"col_heading level0 col1\" >NUMERO_DE_CLIENTES</th>\n",
              "      <th id=\"T_8924e_level0_col2\" class=\"col_heading level0 col2\" >QUANTIDADE_COMPRAS</th>\n",
              "      <th id=\"T_8924e_level0_col3\" class=\"col_heading level0 col3\" >QUANTIDADE_TOTAL_DE_ITENS</th>\n",
              "      <th id=\"T_8924e_level0_col4\" class=\"col_heading level0 col4\" >QUANTIDADE_DE_ITENS_UNICOS</th>\n",
              "      <th id=\"T_8924e_level0_col5\" class=\"col_heading level0 col5\" >NUMERO_FILHOS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_8924e_row0_col0\" class=\"data row0 col0\" >A</td>\n",
              "      <td id=\"T_8924e_row0_col1\" class=\"data row0 col1\" >84</td>\n",
              "      <td id=\"T_8924e_row0_col2\" class=\"data row0 col2\" >1492</td>\n",
              "      <td id=\"T_8924e_row0_col3\" class=\"data row0 col3\" >67736</td>\n",
              "      <td id=\"T_8924e_row0_col4\" class=\"data row0 col4\" >118</td>\n",
              "      <td id=\"T_8924e_row0_col5\" class=\"data row0 col5\" >89</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8924e_row1_col0\" class=\"data row1 col0\" >B</td>\n",
              "      <td id=\"T_8924e_row1_col1\" class=\"data row1 col1\" >645</td>\n",
              "      <td id=\"T_8924e_row1_col2\" class=\"data row1 col2\" >11843</td>\n",
              "      <td id=\"T_8924e_row1_col3\" class=\"data row1 col3\" >530163</td>\n",
              "      <td id=\"T_8924e_row1_col4\" class=\"data row1 col4\" >118</td>\n",
              "      <td id=\"T_8924e_row1_col5\" class=\"data row1 col5\" >724</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8924e_row2_col0\" class=\"data row2 col0\" >C</td>\n",
              "      <td id=\"T_8924e_row2_col1\" class=\"data row2 col1\" >271</td>\n",
              "      <td id=\"T_8924e_row2_col2\" class=\"data row2 col2\" >5136</td>\n",
              "      <td id=\"T_8924e_row2_col3\" class=\"data row2 col3\" >232101</td>\n",
              "      <td id=\"T_8924e_row2_col4\" class=\"data row2 col4\" >118</td>\n",
              "      <td id=\"T_8924e_row2_col5\" class=\"data row2 col5\" >323</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Esses dados são extremamente importantes podemos ver informações detalhadas de cada um dos segmentos o que ajuda a entender o cliente alvo/pessoas que mais compram e a importância delas para o varejo."
      ],
      "metadata": {
        "id": "zH0iJcmWMQW2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total_produtos_catalogo = dados_gerais.explode(\"PRODUTOS\")[\"PRODUTOS\"].nunique()\n",
        "print(total_produtos_catalogo)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W7yG5wzaJpyV",
        "outputId": "c6c74ab9-70e6-424a-9bef-f804ae462ed0"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "118\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Verificação da quantidade total de produtos no catalogo para garantir que a informação recebida em QUANTIDADE_DE_ITENS_UNICOS por segmento esta correta."
      ],
      "metadata": {
        "id": "sv8QpwH1MoTA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **AGRUPAMENTO DE DADOS POR GENERO:**\n"
      ],
      "metadata": {
        "id": "9EcUVcBXM0VL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Mesmo código utilizado em dados de segmento para agilizar o processo de análise\n",
        "resumo_genero = dados_gerais.groupby(\"GENERO\", as_index=False).agg(\n",
        "    NUMERO_DE_CLIENTES=(\"CL_ID\", \"nunique\"),\n",
        "    QUANTIDADE_COMPRAS=(\"CO_ID\", \"nunique\"),\n",
        "    QUANTIDADE_TOTAL_DE_ITENS=(\"QTD_TOTAL_ITENS\", \"sum\")\n",
        ")\n",
        "\n",
        "produtos_unicos_genero = dados_gerais.explode(\"PRODUTOS\").groupby(\n",
        "    \"GENERO\", as_index=False\n",
        ")[\"PRODUTOS\"].nunique().rename(columns={\"PRODUTOS\": \"QUANTIDADE_DE_ITENS_UNICOS\"})\n",
        "\n",
        "clientes_unicos_genero = dados_gerais.drop_duplicates(subset=\"CL_ID\")\n",
        "filhos_genero = clientes_unicos_genero.groupby(\"GENERO\", as_index=False)[\"NUMERO_FILHOS\"].sum()\n",
        "\n",
        "# União dos produtos únicos com o resumo de gênero e número de filhos\n",
        "dados_genero = pd.merge(resumo_genero, produtos_unicos_genero, on=\"GENERO\")\n",
        "dados_genero = pd.merge(dados_genero, filhos_genero, on=\"GENERO\")\n",
        "dados_genero.style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 113
        },
        "id": "S5kMXaX9M-Qa",
        "outputId": "6923a148-0e1d-4504-82e0-1a5e312957ae"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b6134d0>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_6c448\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_6c448_level0_col0\" class=\"col_heading level0 col0\" >GENERO</th>\n",
              "      <th id=\"T_6c448_level0_col1\" class=\"col_heading level0 col1\" >NUMERO_DE_CLIENTES</th>\n",
              "      <th id=\"T_6c448_level0_col2\" class=\"col_heading level0 col2\" >QUANTIDADE_COMPRAS</th>\n",
              "      <th id=\"T_6c448_level0_col3\" class=\"col_heading level0 col3\" >QUANTIDADE_TOTAL_DE_ITENS</th>\n",
              "      <th id=\"T_6c448_level0_col4\" class=\"col_heading level0 col4\" >QUANTIDADE_DE_ITENS_UNICOS</th>\n",
              "      <th id=\"T_6c448_level0_col5\" class=\"col_heading level0 col5\" >NUMERO_FILHOS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_6c448_row0_col0\" class=\"data row0 col0\" >F</td>\n",
              "      <td id=\"T_6c448_row0_col1\" class=\"data row0 col1\" >519</td>\n",
              "      <td id=\"T_6c448_row0_col2\" class=\"data row0 col2\" >9615</td>\n",
              "      <td id=\"T_6c448_row0_col3\" class=\"data row0 col3\" >432576</td>\n",
              "      <td id=\"T_6c448_row0_col4\" class=\"data row0 col4\" >118</td>\n",
              "      <td id=\"T_6c448_row0_col5\" class=\"data row0 col5\" >561</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_6c448_row1_col0\" class=\"data row1 col0\" >M</td>\n",
              "      <td id=\"T_6c448_row1_col1\" class=\"data row1 col1\" >481</td>\n",
              "      <td id=\"T_6c448_row1_col2\" class=\"data row1 col2\" >8856</td>\n",
              "      <td id=\"T_6c448_row1_col3\" class=\"data row1 col3\" >397424</td>\n",
              "      <td id=\"T_6c448_row1_col4\" class=\"data row1 col4\" >118</td>\n",
              "      <td id=\"T_6c448_row1_col5\" class=\"data row1 col5\" >575</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Agrupado da mesma forma que SEGMENTO ECONÔMICO facilita na visualização de dados específicos e entendimento dos clientes."
      ],
      "metadata": {
        "id": "Y5SakPRVdDu_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **AGRUPAMENTO POR ESTADO CIVIL:**"
      ],
      "metadata": {
        "id": "UsHoiNnJbeQP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Traduzindo estados civis\n",
        "mapa_estado_civil = {\n",
        "    1: \"Casado ou União Estável\",\n",
        "    2: \"Divorciado\",\n",
        "    3: \"Separado\",\n",
        "    4: \"Solteiro\",\n",
        "    5: \"Viúvo\"\n",
        "}\n",
        "dados_gerais[\"ESTADO_CIVIL\"] = dados_gerais[\"ESTADO_CIVIL\"].map(mapa_estado_civil)\n",
        "\n",
        "resumo_estado_civil = dados_gerais.groupby(\"ESTADO_CIVIL\", as_index=False).agg(\n",
        "    NUMERO_DE_CLIENTES=(\"CL_ID\", \"nunique\"),\n",
        "    QUANTIDADE_COMPRAS=(\"CO_ID\", \"nunique\"),\n",
        "    QUANTIDADE_TOTAL_DE_ITENS=(\"QTD_TOTAL_ITENS\", \"sum\")\n",
        ")\n",
        "\n",
        "produtos_unicos_estado_civil = dados_gerais.explode(\"PRODUTOS\").groupby(\n",
        "    \"ESTADO_CIVIL\", as_index=False\n",
        ")[\"PRODUTOS\"].nunique().rename(columns={\"PRODUTOS\": \"QUANTIDADE_DE_ITENS_UNICOS\"})\n",
        "\n",
        "clientes_unicos_ec = dados_gerais.drop_duplicates(subset=\"CL_ID\")\n",
        "filhos_estado_civil = clientes_unicos_ec.groupby(\"ESTADO_CIVIL\", as_index=False)[\"NUMERO_FILHOS\"].sum()\n",
        "\n",
        "dados_estado_civil = pd.merge(resumo_estado_civil, produtos_unicos_estado_civil, on=\"ESTADO_CIVIL\")\n",
        "dados_estado_civil = pd.merge(dados_estado_civil, filhos_estado_civil, on=\"ESTADO_CIVIL\")\n",
        "dados_estado_civil.style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 207
        },
        "id": "Q-1Aq3kXYfoN",
        "outputId": "ca96aab1-02c9-441f-adc0-18bc17fcaae7"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b613b10>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_3e659\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_3e659_level0_col0\" class=\"col_heading level0 col0\" >ESTADO_CIVIL</th>\n",
              "      <th id=\"T_3e659_level0_col1\" class=\"col_heading level0 col1\" >NUMERO_DE_CLIENTES</th>\n",
              "      <th id=\"T_3e659_level0_col2\" class=\"col_heading level0 col2\" >QUANTIDADE_COMPRAS</th>\n",
              "      <th id=\"T_3e659_level0_col3\" class=\"col_heading level0 col3\" >QUANTIDADE_TOTAL_DE_ITENS</th>\n",
              "      <th id=\"T_3e659_level0_col4\" class=\"col_heading level0 col4\" >QUANTIDADE_DE_ITENS_UNICOS</th>\n",
              "      <th id=\"T_3e659_level0_col5\" class=\"col_heading level0 col5\" >NUMERO_FILHOS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_3e659_row0_col0\" class=\"data row0 col0\" >Casado ou União Estável</td>\n",
              "      <td id=\"T_3e659_row0_col1\" class=\"data row0 col1\" >233</td>\n",
              "      <td id=\"T_3e659_row0_col2\" class=\"data row0 col2\" >4290</td>\n",
              "      <td id=\"T_3e659_row0_col3\" class=\"data row0 col3\" >194873</td>\n",
              "      <td id=\"T_3e659_row0_col4\" class=\"data row0 col4\" >118</td>\n",
              "      <td id=\"T_3e659_row0_col5\" class=\"data row0 col5\" >295</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3e659_row1_col0\" class=\"data row1 col0\" >Divorciado</td>\n",
              "      <td id=\"T_3e659_row1_col1\" class=\"data row1 col1\" >238</td>\n",
              "      <td id=\"T_3e659_row1_col2\" class=\"data row1 col2\" >4377</td>\n",
              "      <td id=\"T_3e659_row1_col3\" class=\"data row1 col3\" >194990</td>\n",
              "      <td id=\"T_3e659_row1_col4\" class=\"data row1 col4\" >118</td>\n",
              "      <td id=\"T_3e659_row1_col5\" class=\"data row1 col5\" >297</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3e659_row2_col0\" class=\"data row2 col0\" >Separado</td>\n",
              "      <td id=\"T_3e659_row2_col1\" class=\"data row2 col1\" >250</td>\n",
              "      <td id=\"T_3e659_row2_col2\" class=\"data row2 col2\" >4762</td>\n",
              "      <td id=\"T_3e659_row2_col3\" class=\"data row2 col3\" >213742</td>\n",
              "      <td id=\"T_3e659_row2_col4\" class=\"data row2 col4\" >118</td>\n",
              "      <td id=\"T_3e659_row2_col5\" class=\"data row2 col5\" >299</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3e659_row3_col0\" class=\"data row3 col0\" >Solteiro</td>\n",
              "      <td id=\"T_3e659_row3_col1\" class=\"data row3 col1\" >251</td>\n",
              "      <td id=\"T_3e659_row3_col2\" class=\"data row3 col2\" >4551</td>\n",
              "      <td id=\"T_3e659_row3_col3\" class=\"data row3 col3\" >202618</td>\n",
              "      <td id=\"T_3e659_row3_col4\" class=\"data row3 col4\" >118</td>\n",
              "      <td id=\"T_3e659_row3_col5\" class=\"data row3 col5\" >203</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_3e659_row4_col0\" class=\"data row4 col0\" >Viúvo</td>\n",
              "      <td id=\"T_3e659_row4_col1\" class=\"data row4 col1\" >28</td>\n",
              "      <td id=\"T_3e659_row4_col2\" class=\"data row4 col2\" >491</td>\n",
              "      <td id=\"T_3e659_row4_col3\" class=\"data row4 col3\" >23777</td>\n",
              "      <td id=\"T_3e659_row4_col4\" class=\"data row4 col4\" >118</td>\n",
              "      <td id=\"T_3e659_row4_col5\" class=\"data row4 col5\" >42</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Agrupamento por estado civil, denovo utilizando mesmo método do agrupamento por genero e do agrupamento por segmento mas dessa vez traduzindo os códigos de estado civil para seus respectivos nomes."
      ],
      "metadata": {
        "id": "NftLoi6hdU0g"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **EVOLUÇÃO DE COMPRAS AO LONGO DO TEMPO (por mês):**"
      ],
      "metadata": {
        "id": "sIJi3-2dbbQJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados_gerais[\"MES_ANO\"] = dados_gerais[\"DATA_INT\"].dt.to_period(\"M\")\n",
        "\n",
        "resumo_mensal = dados_gerais.groupby(\"MES_ANO\", as_index=False).agg(\n",
        "    QUANTIDADE_COMPRAS=(\"CO_ID\", \"nunique\"),\n",
        "    QUANTIDADE_TOTAL_DE_ITENS=(\"QTD_TOTAL_ITENS\", \"sum\")\n",
        ")\n",
        "\n",
        "resumo_mensal.head(10).style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 364
        },
        "id": "--42KWUYYizU",
        "outputId": "b6a682f2-a2bf-4660-c5cc-c529d018d6a6"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b4e42d0>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_f10fd\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_f10fd_level0_col0\" class=\"col_heading level0 col0\" >MES_ANO</th>\n",
              "      <th id=\"T_f10fd_level0_col1\" class=\"col_heading level0 col1\" >QUANTIDADE_COMPRAS</th>\n",
              "      <th id=\"T_f10fd_level0_col2\" class=\"col_heading level0 col2\" >QUANTIDADE_TOTAL_DE_ITENS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row0_col0\" class=\"data row0 col0\" >2019-01</td>\n",
              "      <td id=\"T_f10fd_row0_col1\" class=\"data row0 col1\" >171</td>\n",
              "      <td id=\"T_f10fd_row0_col2\" class=\"data row0 col2\" >7368</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row1_col0\" class=\"data row1 col0\" >2019-02</td>\n",
              "      <td id=\"T_f10fd_row1_col1\" class=\"data row1 col1\" >402</td>\n",
              "      <td id=\"T_f10fd_row1_col2\" class=\"data row1 col2\" >18336</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row2_col0\" class=\"data row2 col0\" >2019-03</td>\n",
              "      <td id=\"T_f10fd_row2_col1\" class=\"data row2 col1\" >257</td>\n",
              "      <td id=\"T_f10fd_row2_col2\" class=\"data row2 col2\" >11051</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row3_col0\" class=\"data row3 col0\" >2019-04</td>\n",
              "      <td id=\"T_f10fd_row3_col1\" class=\"data row3 col1\" >410</td>\n",
              "      <td id=\"T_f10fd_row3_col2\" class=\"data row3 col2\" >18337</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row4_col0\" class=\"data row4 col0\" >2019-05</td>\n",
              "      <td id=\"T_f10fd_row4_col1\" class=\"data row4 col1\" >711</td>\n",
              "      <td id=\"T_f10fd_row4_col2\" class=\"data row4 col2\" >31811</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row5_col0\" class=\"data row5 col0\" >2019-06</td>\n",
              "      <td id=\"T_f10fd_row5_col1\" class=\"data row5 col1\" >493</td>\n",
              "      <td id=\"T_f10fd_row5_col2\" class=\"data row5 col2\" >22084</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row6_col0\" class=\"data row6 col0\" >2019-07</td>\n",
              "      <td id=\"T_f10fd_row6_col1\" class=\"data row6 col1\" >274</td>\n",
              "      <td id=\"T_f10fd_row6_col2\" class=\"data row6 col2\" >12184</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row7_col0\" class=\"data row7 col0\" >2019-08</td>\n",
              "      <td id=\"T_f10fd_row7_col1\" class=\"data row7 col1\" >420</td>\n",
              "      <td id=\"T_f10fd_row7_col2\" class=\"data row7 col2\" >17900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row8_col0\" class=\"data row8 col0\" >2019-09</td>\n",
              "      <td id=\"T_f10fd_row8_col1\" class=\"data row8 col1\" >436</td>\n",
              "      <td id=\"T_f10fd_row8_col2\" class=\"data row8 col2\" >19122</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_f10fd_row9_col0\" class=\"data row9 col0\" >2019-10</td>\n",
              "      <td id=\"T_f10fd_row9_col1\" class=\"data row9 col1\" >242</td>\n",
              "      <td id=\"T_f10fd_row9_col2\" class=\"data row9 col2\" >10245</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabela de evolução da compra ao longo dos meses, muito util para criação de gráficos e compreender oque mudou nas vendar do estabelecimento ou empresa como um todo."
      ],
      "metadata": {
        "id": "C4R5C74ddjGF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **PRODUTOS MAIS VENDIDOS (ranking geral):**"
      ],
      "metadata": {
        "id": "Iy2NzQArbWlB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "produtos_explodido = dados_gerais.explode(\"PRODUTOS\")\n",
        "\n",
        "top_10_produtos = produtos_explodido.groupby(\"PRODUTOS\", as_index=False).agg(\n",
        "    QUANTIDADE_VENDIDA=(\"CO_ID\", \"count\")   # quantas vezes aquele produto apareceu em compras\n",
        ").sort_values(\"QUANTIDADE_VENDIDA\", ascending=False).head(10)\n",
        "\n",
        "top_10_produtos.style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 364
        },
        "id": "7udpP-cZYkLF",
        "outputId": "2c37a70f-850d-4b16-a79a-e3a369750985"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b4e4190>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_79feb\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_79feb_level0_col0\" class=\"col_heading level0 col0\" >PRODUTOS</th>\n",
              "      <th id=\"T_79feb_level0_col1\" class=\"col_heading level0 col1\" >QUANTIDADE_VENDIDA</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row0_col0\" class=\"data row0 col0\" >PRESUNTO COZIDO</td>\n",
              "      <td id=\"T_79feb_row0_col1\" class=\"data row0 col1\" >12719</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row1_col0\" class=\"data row1 col0\" >SARDINHA</td>\n",
              "      <td id=\"T_79feb_row1_col1\" class=\"data row1 col1\" >6610</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row2_col0\" class=\"data row2 col0\" >BANANA</td>\n",
              "      <td id=\"T_79feb_row2_col1\" class=\"data row2 col1\" >6518</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row3_col0\" class=\"data row3 col0\" >ESCOVA DE DENTE</td>\n",
              "      <td id=\"T_79feb_row3_col1\" class=\"data row3 col1\" >6518</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row4_col0\" class=\"data row4 col0\" >GEL</td>\n",
              "      <td id=\"T_79feb_row4_col1\" class=\"data row4 col1\" >6517</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row5_col0\" class=\"data row5 col0\" >PAPINHA INFANTIL</td>\n",
              "      <td id=\"T_79feb_row5_col1\" class=\"data row5 col1\" >6515</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row6_col0\" class=\"data row6 col0\" >MODELADOR</td>\n",
              "      <td id=\"T_79feb_row6_col1\" class=\"data row6 col1\" >6505</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row7_col0\" class=\"data row7 col0\" >CERA</td>\n",
              "      <td id=\"T_79feb_row7_col1\" class=\"data row7 col1\" >6502</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row8_col0\" class=\"data row8 col0\" >CEBOLA</td>\n",
              "      <td id=\"T_79feb_row8_col1\" class=\"data row8 col1\" >6501</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_79feb_row9_col0\" class=\"data row9 col0\" >LIMPADOR PERFUMADO</td>\n",
              "      <td id=\"T_79feb_row9_col1\" class=\"data row9 col1\" >6501</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Bom para saber o que mais gira dentro do estoque."
      ],
      "metadata": {
        "id": "zr50nuW3d77L"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **TICKET MÉDIO (itens por compra) POR GÊNERO E SEGMENTO JUNTOS:**"
      ],
      "metadata": {
        "id": "1nj5unzLbSQW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "resumo_genero_segmento = dados_gerais.groupby(\n",
        "    [\"GENERO\", \"SEGMENTO_ECONOMICO\"], as_index=False\n",
        ").agg(\n",
        "    QUANTIDADE_COMPRAS=(\"CO_ID\", \"nunique\"),\n",
        "    QUANTIDADE_TOTAL_DE_ITENS=(\"QTD_TOTAL_ITENS\", \"sum\")\n",
        ")\n",
        "\n",
        "# Calcula o ticket médio (itens por compra) como coluna nova\n",
        "resumo_genero_segmento[\"MEDIA_ITENS_POR_COMPRA\"] = (\n",
        "    resumo_genero_segmento[\"QUANTIDADE_TOTAL_DE_ITENS\"] / resumo_genero_segmento[\"QUANTIDADE_COMPRAS\"]\n",
        ").round(2)\n",
        "\n",
        "resumo_genero_segmento.style.hide(axis=\"index\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        },
        "id": "w8jV-dwJYlX5",
        "outputId": "356b0734-1d15-465d-cb9c-14b2929825f6"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7af49b4e4550>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "</style>\n",
              "<table id=\"T_8728b\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th id=\"T_8728b_level0_col0\" class=\"col_heading level0 col0\" >GENERO</th>\n",
              "      <th id=\"T_8728b_level0_col1\" class=\"col_heading level0 col1\" >SEGMENTO_ECONOMICO</th>\n",
              "      <th id=\"T_8728b_level0_col2\" class=\"col_heading level0 col2\" >QUANTIDADE_COMPRAS</th>\n",
              "      <th id=\"T_8728b_level0_col3\" class=\"col_heading level0 col3\" >QUANTIDADE_TOTAL_DE_ITENS</th>\n",
              "      <th id=\"T_8728b_level0_col4\" class=\"col_heading level0 col4\" >MEDIA_ITENS_POR_COMPRA</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td id=\"T_8728b_row0_col0\" class=\"data row0 col0\" >F</td>\n",
              "      <td id=\"T_8728b_row0_col1\" class=\"data row0 col1\" >A</td>\n",
              "      <td id=\"T_8728b_row0_col2\" class=\"data row0 col2\" >700</td>\n",
              "      <td id=\"T_8728b_row0_col3\" class=\"data row0 col3\" >32875</td>\n",
              "      <td id=\"T_8728b_row0_col4\" class=\"data row0 col4\" >46.960000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8728b_row1_col0\" class=\"data row1 col0\" >F</td>\n",
              "      <td id=\"T_8728b_row1_col1\" class=\"data row1 col1\" >B</td>\n",
              "      <td id=\"T_8728b_row1_col2\" class=\"data row1 col2\" >5946</td>\n",
              "      <td id=\"T_8728b_row1_col3\" class=\"data row1 col3\" >264308</td>\n",
              "      <td id=\"T_8728b_row1_col4\" class=\"data row1 col4\" >44.450000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8728b_row2_col0\" class=\"data row2 col0\" >F</td>\n",
              "      <td id=\"T_8728b_row2_col1\" class=\"data row2 col1\" >C</td>\n",
              "      <td id=\"T_8728b_row2_col2\" class=\"data row2 col2\" >2969</td>\n",
              "      <td id=\"T_8728b_row2_col3\" class=\"data row2 col3\" >135393</td>\n",
              "      <td id=\"T_8728b_row2_col4\" class=\"data row2 col4\" >45.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8728b_row3_col0\" class=\"data row3 col0\" >M</td>\n",
              "      <td id=\"T_8728b_row3_col1\" class=\"data row3 col1\" >A</td>\n",
              "      <td id=\"T_8728b_row3_col2\" class=\"data row3 col2\" >792</td>\n",
              "      <td id=\"T_8728b_row3_col3\" class=\"data row3 col3\" >34861</td>\n",
              "      <td id=\"T_8728b_row3_col4\" class=\"data row3 col4\" >44.020000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8728b_row4_col0\" class=\"data row4 col0\" >M</td>\n",
              "      <td id=\"T_8728b_row4_col1\" class=\"data row4 col1\" >B</td>\n",
              "      <td id=\"T_8728b_row4_col2\" class=\"data row4 col2\" >5897</td>\n",
              "      <td id=\"T_8728b_row4_col3\" class=\"data row4 col3\" >265855</td>\n",
              "      <td id=\"T_8728b_row4_col4\" class=\"data row4 col4\" >45.080000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td id=\"T_8728b_row5_col0\" class=\"data row5 col0\" >M</td>\n",
              "      <td id=\"T_8728b_row5_col1\" class=\"data row5 col1\" >C</td>\n",
              "      <td id=\"T_8728b_row5_col2\" class=\"data row5 col2\" >2167</td>\n",
              "      <td id=\"T_8728b_row5_col3\" class=\"data row5 col3\" >96708</td>\n",
              "      <td id=\"T_8728b_row5_col4\" class=\"data row5 col4\" >44.630000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ótimo para entender quanto cada tipo de cliente normalmente compra. Por essa tabela, vemos que o ticket\n",
        "médio entre os grupos é bastante parecido, ainda assim o Segmento Econômico A do gênero Feminino se\n",
        "destaca com o maior ticket médio, chegando a quase 47 itens por compra. Como a Classe A representa a\n",
        "faixa de maior renda entre as três (segundo a segmentação econômica da base), isso sugere que clientes\n",
        "de maior poder aquisitivo tendem a comprar mais itens por vez. Por outro lado, na mesma tabela vemos que\n",
        "a quantidade de compras efetuadas pelo Segmento A é a menor entre os três grupos, ou seja, esse\n",
        "segmento compra com menos frequência, porém em maior volume por compra, um padrão coerente com um\n",
        "perfil de consumidor de maior renda que concentra suas compras em vez de fracioná-las."
      ],
      "metadata": {
        "id": "8LmJIIbyeCGr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Agora que agrupamos alguns valores importantes podemos seguir e visualizar as informações estatísticas da coluna de número de filhos."
      ],
      "metadata": {
        "id": "5oJAf-vnXLRW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **7 - Estatísticas**"
      ],
      "metadata": {
        "id": "jPGDBWiGX9Ge"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Estatísticas descritivas da coluna NUMERO_FILHOS, calculadas a partir de clientes únicos\n",
        "filhos = clientes[\"NUMERO_FILHOS\"]\n",
        "\n",
        "media = filhos.mean()\n",
        "mediana = filhos.median()\n",
        "desvio_padrao = filhos.std()\n",
        "moda = filhos.mode()[0]        # mode() pode retornar mais de um valor se houver empate, pega o primeiro\n",
        "maximo = filhos.max()\n",
        "minimo = filhos.min()\n",
        "contagem = filhos.count()\n",
        "q1 = filhos.quantile(0.25)\n",
        "q2 = filhos.quantile(0.50)\n",
        "q3 = filhos.quantile(0.75)\n",
        "\n",
        "print(f\"Média: {media:.2f}\")\n",
        "print(f\"Mediana: {mediana}\")\n",
        "print(f\"Desvio Padrão: {desvio_padrao:.2f}\")\n",
        "print(f\"Moda: {moda}\")\n",
        "print(f\"Máximo: {maximo}\")\n",
        "print(f\"Mínimo: {minimo}\")\n",
        "print(f\"Número de clientes: {contagem}\")\n",
        "print(f\"1º Quartil (25%): {q1}\")\n",
        "print(f\"2º Quartil (50%): {q2}\")\n",
        "print(f\"3º Quartil (75%): {q3}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rtdEjUSBXdpB",
        "outputId": "e089a114-b0fe-4b74-8222-92d005c5d90d"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Média: 1.14\n",
            "Mediana: 0.0\n",
            "Desvio Padrão: 1.41\n",
            "Moda: 0\n",
            "Máximo: 4\n",
            "Mínimo: 0\n",
            "Número de clientes: 1000\n",
            "1º Quartil (25%): 0.0\n",
            "2º Quartil (50%): 0.0\n",
            "3º Quartil (75%): 2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Essas estatísticas poderiam ter sido feitas utilizando apenas o .describe(), mas para fins de melhor\n",
        "visualização e para incluir a moda (que o .describe() não calcula), preferi separar valor por valor com print."
      ],
      "metadata": {
        "id": "Kxf4gVQCXg8o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Estatísticas descritivas da coluna NUMERO_FILHOS, calculadas a partir de clientes únicos\n",
        "estatisticas_compra_segmento = dados_segmento[\"QUANTIDADE_COMPRAS\"]\n",
        "\n",
        "media = estatisticas_compra_segmento.mean()\n",
        "mediana = estatisticas_compra_segmento.median()\n",
        "desvio_padrao = estatisticas_compra_segmento.std()\n",
        "moda = estatisticas_compra_segmento.mode()[0]        # mode() pode retornar mais de um valor se houver empate, pega o primeiro\n",
        "maximo = estatisticas_compra_segmento.max()\n",
        "minimo = estatisticas_compra_segmento.min()\n",
        "contagem = estatisticas_compra_segmento.count()\n",
        "q1 = estatisticas_compra_segmento.quantile(0.25)\n",
        "q2 = estatisticas_compra_segmento.quantile(0.50)\n",
        "q3 = estatisticas_compra_segmento.quantile(0.75)\n",
        "\n",
        "print(f\"Média de compras por Segmento: {media:.2f}\")\n",
        "print(f\"Mediana: {mediana}\")\n",
        "print(f\"Desvio Padrão: {desvio_padrao:.2f}\")\n",
        "print(f\"Moda: {moda}\")\n",
        "print(f\"Máximo: {maximo}\")\n",
        "print(f\"Mínimo: {minimo}\")\n",
        "print(f\"Número de segmentos: {contagem}\")\n",
        "print(f\"1º Quartil (25%): {q1}\")\n",
        "print(f\"2º Quartil (50%): {q2}\")\n",
        "print(f\"3º Quartil (75%): {q3}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nk8zhkGiMFsB",
        "outputId": "46634f95-4491-4dcc-c0e9-0b926355e0ba"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Média de compras por Segmento: 6157.00\n",
            "Mediana: 5136.0\n",
            "Desvio Padrão: 5250.49\n",
            "Moda: 1492\n",
            "Máximo: 11843\n",
            "Mínimo: 1492\n",
            "Número de segmentos: 3\n",
            "1º Quartil (25%): 3314.0\n",
            "2º Quartil (50%): 5136.0\n",
            "3º Quartil (75%): 8489.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **7.5 - GRÁFICOS**"
      ],
      "metadata": {
        "id": "wcHSinH5MlBW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "plt.figure(figsize=(12, 5))\n",
        "\n",
        "# Transformando PERIOD em\n",
        "resumo_mensal['MES_ANO_STR'] = resumo_mensal['MES_ANO'].astype(str)\n",
        "\n",
        "# Criando linha de evolução\n",
        "sns.lineplot(data=resumo_mensal, x='MES_ANO_STR', y='QUANTIDADE_COMPRAS', marker='o', linewidth=2.5, color='royalblue')\n",
        "\n",
        "# Ajuste dos textos\n",
        "plt.title('Evolução Mensal das Compras ao Longo do Tempo', fontsize=14, fontweight='bold', pad=15)\n",
        "plt.xlabel('Mês / Ano', fontsize=12)\n",
        "plt.ylabel('Quantidade de Compras', fontsize=12)\n",
        "\n",
        "# Posicionar as datas na diagonal para caber no gráfico\n",
        "plt.xticks(rotation=45, ha='right')\n",
        "\n",
        "plt.grid(True, linestyle='--', alpha=0.6)\n",
        "plt.tight_layout()  #Aumenta o tamanho do espaço para garantir que nada seja cortado\n",
        "\n",
        "# Exibir o gráfico\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "LW4lopHmMsLM",
        "outputId": "b42041e4-a958-4dc9-8725-17cdd02fa684"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x500 with 1 Axes>"
            ],
            "image/png": "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73//K7PLcRxGjhyJ6dOno7i4GDk5OXC5XKisrMQ777wDt9uNL774Au+99x4uuuiiqOvNC2MMV111FTo7O8XfXbx4MYYPH4733nsPX375ZdBjs7OzMWfOHIwdOxY5OTkwmUxobGzE+++/j5qaGtjtdixduhSffPJJTHUQDEEQZCsLTpw4EZMnT47o2N27d+Oyyy5Db28vACAvLw9XXHEFOI7Dyy+/jMOHD6O3txdXXHEFJk+e3GeqKgDs3bsXeXl5+M1vfoPq6mq8++67AICqqipcfvnlKCwsxJIlS7Bx40ax/r766iusX78e06dPD6hrzZo1uOyyyzB06FC89957qKysBAB8+OGHePXVVwMuInD48GEcPnwYp59+OmbOnIlDhw5h8ODBAJLXNgBgMBgwadIkHH/88cjPz0dWVha6urrwzTffYM2aNQCABx54QPwNQBtj4iWXXILt27eLn3/2s59h3LhxWL16NdatWwcAeO+997B8+XLcc889AW18/fXXOO2003DCCSfggw8+wNatWwH0bf+nnnoK//vf/8TjjjnmGJx33nnYvHkzPvzww6Aaly9fjrffflv8PH36dMyZMwc7duzAO++8AwDYsWMHLrnkEvznP/8JW+Z3330Xb775pvj5qKOOwkUXXYT6+nq8+uqrQY9LZnu9+eabWL58ufh57ty5mDlzJhobG/Hyyy+js7MT//vf/3DLLbfgueeeC2hj06ZNmDFjBs444wy89dZbYt9/4IEHAACnnHIKTj75ZPzjH/9AQ0MDAPl4HsheUVERfvWrX6GjowMvvPACent7IQgCrr32WsyZMwc2mw1utxsXXHAB6urqAAB6vR6XXXYZSkpK8MEHH2Dbtm0APP3juOOOS8jiIQRBECFJtleMIAhioOH/1jvYn/TNdXV1tSzSaOvWrYwxxnp7e2XRFNKpHxMnThS3Dx8+nHV3d4vf/fWvf5X9ljRSSelIqeOOO07cnpGRwaqqqmTHdXZ2ssbGRtk2nufZd999x1566SX2pz/9iT322GN93pjX1NQwxhg7fPiwbOrcRRddJLMlfeOv1+vZ4cOHQzcQ69tGH330keyt+apVq9hRRx3FALD8/HzmcDiCRko99dRT4vacnBzZdJPOzk6Wn58vfv/UU0+J30mjZgCwDz74QPzuT3/6k+w7u93OGPNMp/Jumzt3bp9yORwOVldX12d7Y2Mj+9e//sX++te/sj/+8Y/sscceY0cffbRo66qrrhL3jSVSat26dbJj7rrrLvG79vZ2WRSZf6QUY56Ij6+++oq98MIL7Mknn2SPPfYYu/LKK8Vj0tLSxKk0sdaBP01NTTLNF198cdhjvNx0002yKAbv+coYY1u3bpVFOUmjFfzb/Ouvvxa/Kyoqkn23ceNGxhhjdrudGY1Gcfuf//xn8Rj/c/ahhx4Sv/Ov95kzZ4rfSSOlALCbb745aFmT0TZSqqqq2Jtvvsn+8pe/iH03PT1d/J1XXnlF3DfWMTEU0mPCRUr9+OOPsv1/85vfiN+53W42Y8YM8bvc3FzG8zxjrO94dMEFF4iRbc3NzbLxT9r+0qg0//L69zXveczzPMvNzRW3z5gxQxYp+Zvf/EZ23I8//hi2jubOnSvub7PZZGPgQw89FPTaoUZ7SQkVKXXssceK311++eWy795++23xO4PBICuPVNO4cePEvv/ZZ5/Jvps4caJYr3//+98DjueMySOljEajbErs66+/LjvuH//4B2OMsffff1+2/a9//at4THd3t6zcEydOjLreCIIglIacUgRBEAkmFqcUY4zNnj1b/O53v/sdY4yxf/3rX7KHGIfDwRjz5BGROrHuuOMOma3Ozs6gD0dKOqX8dfzqV78KWz+ff/45Gzp0aNj6+fbbbxljjH3yySey7f/+979l9v7973/Lvv/kk0/CagjklKqrq2MGg4EBnikj3u9+//vf96k36cNpuGkw0j+p40P60FhUVCTT9+mnn8qO8+akqq2tZWlpabKHokWLFrF77rmHvf/++7KHHcY8DyhLliwJOBVM+jdnzhzxmFicUn/5y19kx/jnU5I6MfydUq+99lrIqY/eP+9UomjrIBjxOKWmTp0qHjdlypQ+30+ZMkX8furUqeJ2aZsPHz5cdozUYTFixAjZd9L+KJ2y5n/Oeh25XqT1brFYxO3+TqlgjtxktQ1jnn54wgknhP1t73TneMbEUEiPCeeU8nekbN++Xfb9M888I/u+oqKCMdZ3PPLPBzR48OA+7e8/Nde/vGvXrg14HldUVMi2e6cre9m+fbvse6nDIxh5eXlBz6P9+/fL7AW7dijVXlKCOaX8fzvc36effioeK91+3333idurqqpk30nP09WrVwcczxmTO6VOPfVUmX632y1zSF933XWM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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "O Gráfico nos mostra uma estabilização por volta de 300 a 400 compras mensais a partir do mês 2 de 2022 e uma queda estrema no mês 09, o gráfico de evolução anual é bem instável mas podemos ver que nos anos de 2020 e 2021 tivemos um pico das compras durante o período do mês 09 a 10, no entanto, no ano de 2022 o contrário pode se visualizado assim como ja comentado anteriormente. Ainda não é possivel fazer nenhuma análise mais profunda desse gráfico por conta de sua alta imprevisibilidade e por conta do não conhecimento da causa dessa quedra abrubta, precisamos análisr outros dados antes de conclusões precipitadas, honestamente o melhor seria ter o conhecimento da estratégia utilizada pela empresa ou seu funcionamento durante esses meses de queda, para que fosse possivel entender as causas."
      ],
      "metadata": {
        "id": "eNqUMrQ8PU-h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Criar a coluna MES_ANO no formato string a partir de dados_data para o gráfico\n",
        "dados_data['MES_ANO_STR'] = dados_data['DATA_INT'].dt.to_period('M').astype(str)\n",
        "\n",
        "# 2. Agrupar por Mês e por Categoria de Produto, contando a quantidade total de itens vendidos\n",
        "evolucao_categoria = dados_data.groupby(['MES_ANO_STR', 'PR_CAT']).agg(\n",
        "    QUANTIDADE_ITENS=('QUANTIDADE', 'sum')\n",
        ").reset_index()\n",
        "\n",
        "# 3. Configurar o gráfico de linhas aberto por categoria\n",
        "plt.figure(figsize=(15, 6))\n",
        "sns.lineplot(\n",
        "    data=evolucao_categoria,\n",
        "    x='MES_ANO_STR',\n",
        "    y='QUANTIDADE_ITENS',\n",
        "    hue='PR_CAT',       # Isso cria uma linha de cor diferente para cada categoria!\n",
        "    marker='o',\n",
        "    linewidth=2\n",
        ")\n",
        "\n",
        "# Configurações estéticas\n",
        "plt.title('Evolução Mensal de Itens Vendidos por Categoria de Produto', fontsize=14, fontweight='bold', pad=15)\n",
        "plt.xlabel('Mês / Ano', fontsize=12)\n",
        "plt.ylabel('Total de Itens Vendidos', fontsize=12)\n",
        "plt.xticks(rotation=45, ha='right')\n",
        "plt.grid(True, linestyle='--', alpha=0.5)\n",
        "plt.legend(title='Categorias', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move a legenda para fora do gráfico\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 607
        },
        "id": "Q_cmWA3ZRJ7t",
        "outputId": "42c43549-fa02-4355-ffb3-5c5caa74d300"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1500x600 with 1 Axes>"
            ],
            "image/png": "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ERERCYToSA/C7bffjrKyMlitVuzduxcTJkz4pVX6ReF5HlVVVV65wPpCbk1NTZ/LjVTZkahzpMoOt87haC/hlB2JzzBSZUeizj+HbLFeh192JOocqbIjUedwyo5EnSNVdiT21S7ZkVgeouzwyxVl+5ZbUVERke080uw9EREREReiI11EREREREREREREREREREREREREREQkAKIjXURERERERERERERERERERERERERERCQAoiNdpFswDAONRgOGYSJCbqTKjkSdI1V2JOocTtmRqHOkyo5EnSNVdiTqHE7ZkahzpMqORJ3DKTsSdY5U2ZGoczhlR6LOkSo7EnWOVNmRqHM4ZYdTZxEREREXDIknMYQF8WRlEREREREREREREREREREREZGeIvqWRER+XYgR6SLdgud5NDQ0hOVgkHDIjVTZkahzpMqORJ3DKTsSdY5U2ZGoc6TKjkSdwyk7EnWOVNmRqHM4ZUeizpEqOxJ1DqfsSNQ5UmVHos6RKjsSdQ6n7HDqLCIiIuJCdKSLdAsiQkNDA/p6I0O45Eaq7EjUOVJlR6LO4ZQdiTpHquxI1DlSZUeizuGUHYk6R6rsSNQ5nLIjUedIlR2JOodTdiTqHKmyI1HnSJUdiTqHU3Y4dRYRERFxITrSRURERERERERERERERERERERERERERAIgOtJFREREREREREREREREREREREREREREAiA60kW6BcMwiI6ODssJ2+GQG6myI1HnSJUdiTqHU3Yk6hypsiNR50iVHYk6h1N2JOocqbIjUedwyo5EnSNVdiTqHE7ZkahzpMqORJ0jVXYk6hxO2eHUWURERMQFQ2ICqbAgnqwsIiIiIiIiIiIiIiIiIiIiItJTRN+SiMivCzEiXaRb8DyP6urqsJywHQ65kSo7EnWOVNmRqHM4ZUeizpEqOxJ1jlTZkahzOGVHos6RKjsSdQ6n7EjUOVJlR6LO4ZQdiTpHquxI1DlSZUeizuGUHU6dRURERFyIjnSRbkFEaG1tDcsJ2+GQG6myI1HnSJUdiTqHU3Yk6hypsiNR50iVHYk6h1N2JOocqbIjUedwyo5EnSNVdiTqHE7ZkahzpMqORJ0jVXYk6hxO2eHUWURERMSF6EgXERERERERERERERERERERERERERERCYD0l1bgt4prFbStre0X1qRv4TgOBoMBbW1tkEgk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njxJarWaZsyYQadOneq1vM4UFBRQamoqLV68mJYsWUJSqZTuueeeXss9ceIERUdH09/+9jf3PY7jei2XSNA5JyeHxo4dS5mZmZSZmUkbNmzoE9lHjx6l9PR0mj17Nk2ePJkYhqGvvvqqT2QTEa1evZoYhqGcnBzatWtXn8g8cuQIaTQauuuuu/pEXmfOnj1LCQkJdN9995HFYulT2UeOHCGlUknXXnstzZw5kx5++GEi6n09OXbsGMXHx9PKlSvp1ltvJZlMRk8++WRfqOweY2bNmkUzZ84klmXpmmuuob179/Za9rFjx0iv19P06dNp6tSpJJFIaMWKFfTNN9/0WvaJEydIKpV61BGe53stt6CggLKysmjy5MmUl5dHMpmM3n///V7LJQqfzkTh1fvo0aOUkpJCixcvpqVLlxLLsvTqq6/2iewHH3yQGIahtLQ0+uCDD/qsTbr6kL7o+7tSXFxMycnJdP/99/fZGEDUYYPceuuttHLlSrrmmmvIZDL1SR05fvw4xcbG0urVq+mxxx6j5OTkPiubY8eOUVxcHC1atIguueQSksvlNHv2bFq3bl2v5LrG3AULFtDFF19MOp2O5s+fT6+//nqvdQ7XfIAovHOCSLRDItEGIQqfHRKJNghR+OwQ0QbxJpzjuYiIiEhPER3p/0eprq6mSZMm0axZsyg2NpYuv/zyPjGeS0tLKScnh/7whz+Qw+EgIqKXX36ZkpOT6dy5c72SXVxcTFlZWfTQQw+57/35z3+m2267jex2e69kuzh8+DCtWrWKHnvsMUpNTaW//e1v1NLS0iuZZ86cIYVC4TbgbDYbrV+/nl577TXasGEDGQyGHsv+6quvaPHixW65f/7zn+mSSy6hm2++md59990eyz148CBFRUXRH//4RyIiev/990mv19Pu3buJqHdGqNFopAsvvJDuvvtu973PP/+cLrnkEqqrq+txebS3t9P8+fPpgQcecN8rKyujmJgYSk5O7pWB63A46K677qKrr77afa+iooIeeOABGjZsmMf/2V3q6upo+vTpdNFFF1FqairNnDmTTp482WN5nSkvL6e8vDy677773Pe2bNlCarWajhw50iu5o0ePpoEDB1JsbKxH2fZ2gnLu3DlKS0ujBx54gJqbm6mgoIDWrFlDy5cvJ4PB0CvD/MyZM5Senk4PPfQQWa1WampqosWL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ra104MABt1FbUVFBycnJXs70nixgHDx40CNixsXgwYPdCzs9obCwkD744AMiEurak08+2SeTWLvdTs8//zw988wzROTpLMjKyqLy8vIe60wkTBg6t+O//e1vxLIsXXXVVXTrrbcSwzAe0To9obCwkGbOnOl+f9lll5FCoaC4uLgeOQ62bdtGgwYNossvv5zy8/Np/vz59NNPP9H+/fvpmWeeIYZherSI4yrbRx55hG666Sb64osvaN68eVRXV+f+HVOnTqVLL72027Kbmpq8+nur1UqXX345TZkyxUuH7lBaWkpqtZoefvhhOnr0KD3xxBOkUqnoscceo2eeeYbGjRtHF1xwgXvC3x0OHz5MDMPQ1q1b3ffOnTtHCxcupPfff58YhqFXXnml23J5nqf29naaMWOGu37Z7XZ3m3alX+pp6q/z5897pAZ4//33SaFQ9DoqbO3atR4pE4gEJ2dGRkavoxDLysrCojNRePU+e/Ys/fDDD+73f/3rX0kikdCtt95KjzzyCMXGxtKll17a4wXn1tZWmj59uttRf+edd5JUKiW9Xk/79+/vkcz9+/fT/PnzaeHChTR48GBauHAhHTx4kEpLS2ndunUkk8l6tOju4vXXX6fly5fThx9+6GGDVVZW0jXXXEPz5s2jxsbGbsnsHFzA8zw5HA568MEHafjw4W6nf0/rR01NDeXm5tL1119PX3/9NT3yyCOkVqvpmWeeoffee4+uuuoqmj59eo8CHIqKikipVNLatWvd90pLS2nChAnunX0uR1ao8DxPNpuNVq1aRStXriSLxUIcx7nH2LNnz9KECRPcUb3dJVzzAaLwzgki0Q6JRBuEKDx2SKTaIEThs0NEG8SbcI7nIiIiIr1BdKT/H8ZlYLquO3fu9IhEsdls9OKLL9J3333XLbmuwdJ1dTgclJ2d7SFn69atPYqAcsmsr6+nO++80yMa4NixY8QwDG3ZsqXbcok6ymH69On03nvvEZEQEabT6Sg5OZn+/e9/98g5QyRsrXZFrZ0+fdrjsy+++IJYlqWzZ892W25BQQGlpKTQsGHDaP78+R6fuQy9nkSgEHlPQFpbWyktLY3uvPPOHsnrzI8//kjz58+nyy+/nAYOHEhvvPGG+7Pq6mrKyMjoUYTLv//9b2IYhm688UZ65JFHSKvVurdCf/TRR9S/f39qamrq0eRq3759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WSy9L+/Xrx8risLu7u4O3VxParbEfYHEzlpmS+ysZTaOQSo2GwBAC5hI15F7d0KmHfClS5f49OnTnJuby7179+bg4GBu1KgR9+7dm729vW3eJEarXGTro7OW2ZXROSsri3fv3n3f41OmTOG6deuqWpNPanZppqvK8vPzOScnh7/77jtu0KABd+7cmSMiIjgmJobd3d1VrbWObP111jJbYmfm//3MXb9+nXNzc+97/rnnnmMfHx+H1vXUKrsiOufk5PDly5f59OnT3KpVK+7YsSO3a9eOBw4cyLVr13boZmESsyV21jJbYmcts025165dMy9lwPy/16z4+HiH9uWSsyXuCyR21jJbYmcts3EMUrHZAABawUS6Dph2yqarUg0Gg/mxs2fPsp+fH7/99tvMzHzz5k3+6aef+F//+hevXLnS6l3LtcpFtj4663k8li9fbvF3kpOTWVEUm1dTScwu6yoQU+6ZM2e4UaNGvH37dma++ymABQsW8JgxYzg+Pt7mQS2y5XfGeNif7efnxykpKRbPv/3226woCh88eLBSsrXsXBbTibEp23QDzevXr/Mnn3zC06dP55dffpmPHz9eLbIldtYyW2JnLbNNuaZ9+bp16yyeX7FiharjBD1ll9frdUVmS+ysZbbEzlpmV1Tn8t6fS80GANASJtKFO3bsGL/wwgs8aNAgnjx5Mv/yyy/m5y5evMju7u48fvx4NhqNZd4MqKJzka2PzlpmV5XOpd2+fZvPDZJh6AAAGIVJREFUnz+vu+zjx49zQkICjxo1ilesWMF//PGH+blz586xj48Px8bGstFoNJ8wm/4NW2OPbPmdMR6OZY8dO9biZ9FoNPLOnTttvsmnVbaWnTMyMvjEiRNlPnfhwgX29vbmcePGOfR6LTFbYmctsyV21jLbntzSTp48yWfOnNFldnp6Oi9fvpynTp3KqampnJ2dbX7u/PnzXK9ePYdfr7XKltgZ41F9xsPR/bnUbACAyoCJdMGOHj3KderU4bi4OH7hhRd4yJAh7OLiwitWrOCCggI+cOAAz5w50+4TCK1yka2PzlpmS+wsNTstLY29vLw4KiqKu3Xrxl26dOHGjRvzt99+y8zMiYmJHB8f/8B1C+99HNkPzpbYGeNRftlqaJWtZedjx45x06ZNOTo6mo8ePXrf85s2beLp06dXm2yJnbXMlthZy2yJ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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "O padrão de compras da empresa possui uma imprevisibilidade natural, com picos históricos recorrentes (como no final de 2020 e 2021). A anomalia severa de setembro de 2022 afeta todas as categorias simultaneamente, o que aponta para um problema de integridade técnica na base de dados ou parada do sistema de registros, e não uma mudança de comportamento do consumidor. É interessante o conhecimento dessas informações para confirmar com a empresa e entender qual pode ter sido a real causa desta queda. No entanto, como já vimos anteriormente, podemos ver que a empresa já tem um pequeno histórico de banco desorganizado ou com falta de informações, já que anteriormente a limpeza de diversos dados foi necessária, assim como a exclusão de colunas que nem nome tinham; ou seja, nada impede que essa queda abrupta seja realmente um problema no sistema de registros."
      ],
      "metadata": {
        "id": "-QEkdemGRiVp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# Configuração global de estilo para os gráficos ficarem limpos e profissionais\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "plt.rcParams['font.family'] = 'sans-serif'\n",
        "\n",
        "# ==============================================================================\n",
        "# 1. GRÁFICO DE IMPACTO: Comparativo Anual de Vendas Mensais (Linhas Sobrepostas)\n",
        "# ==============================================================================\n",
        "plt.figure(figsize=(12, 5))\n",
        "\n",
        "# Criando colunas auxiliares de Mês e Ano isolados para a sobreposição\n",
        "dados_data['ANO_MUITO_ISOLADO'] = dados_data['DATA_INT'].dt.year\n",
        "dados_data['MES_MUITO_ISOLADO'] = dados_data['DATA_INT'].dt.month\n",
        "\n",
        "# Agrupando para contar as compras únicas por Ano e Mês\n",
        "comparativo_anual = dados_data.groupby(['ANO_MUITO_ISOLADO', 'MES_MUITO_ISOLADO'])['CO_ID'].nunique().reset_index()\n",
        "\n",
        "sns.lineplot(\n",
        "    data=comparativo_anual,\n",
        "    x='MES_MUITO_ISOLADO',\n",
        "    y='CO_ID',\n",
        "    hue='ANO_MUITO_ISOLADO',\n",
        "    marker='o',\n",
        "    linewidth=2,\n",
        "    palette='tab10'\n",
        ")\n",
        "\n",
        "plt.title('Comparativo Mensal de Compras: Sazonalidade vs. Apagão de 2022', fontsize=13, fontweight='bold', pad=15)\n",
        "plt.xlabel('Mês do Ano', fontsize=11)\n",
        "plt.ylabel('Quantidade de Compras Únicas', fontsize=11)\n",
        "plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])\n",
        "plt.legend(title='Ano')\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 501
        },
        "id": "0qVRxXmMTHzA",
        "outputId": "6bbb6cb5-6315-4e37-9cf9-27146d0f35a9"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x500 with 1 Axes>"
            ],
            "image/png": "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TNSqVcuqrddee41PP/2UqKgo6tevX+T5kpKSCA0Nxdvbm3nz5mGy8S6SSkCJiIiIiIgUQ5XRo8g+eRK/554leeUqTox7ptDixXnp6WQfOULWxVPlChb8vmhHqmIzGHCsWvWf5NKlU+UqVbrh1ylS1njc0+2aRiDlpafjNWiQZc2ni3kNGgRAnY2f3LD4ipKTk8PEiRM5ePAga9aswe+SZFetWrWoXbs2W7dutZomFx0dTUhICE4XrcO2ePFili9fzqxZswgJCSnyfBcuXCAsLIzs7GzeffddKlasWDIXdgVKQImIiIiIiBSDwWTCb8rzJK94l4S337YctyxenJeHS8MGHA8fdW3turj8M0Xukqlyppo1cLDhgt8iNwMHV1e8h4YB+Ws+2WMXvGnTpvHNN98wYcIEzp8/z549eyxlDRo0wMnJiVGjRhEREYG/vz/BwcFER0cTExPDqlX/rF+1adMmZs+eTZ8+fahZs6ZVO/7+/nh5eQEwatQo/vjjD1555RVOnjzJyZMnLfWaNm1a0pcLKAElIiIiIiJSbMYKFUhavbrIsqTVq7ntqy8xVq5MbnKy9fO8va2nytUqGMlUC8cqVUrdgt8i5Z2DszPeT4biM3wYuampGN3dMefk2CT5BLBz504AZs6cWahs+/bt1KxZk169epGenk5UVBSLFy8mICCAefPmERQUVKidjRs3snHjRqt2pk+fTr9+/azqFeyyd7H9+/ffmIu6CiWgREREREREiik3JeWKixfnnjtH5cGDcHByzp8y5++PqUZNjBUr2DhSEbmagnXbHP8eJWSw4ZpIX3zxBRkZGbi4uGC8wlpt/fv3p3///pctnzFjBjNmzLjq+WyVZLoSJaBERERERESKyejhceXFi318qDJihB0iExEp3RzsHYCIiIiIiEhZYc7JsSxSfCmvQYMw5+TYOCIRkbJBI6BERERERESKqTQsXiwiUhYpASUiIiIiInINChYv9h42lJyUFBw9PCA3V8knEZEr0BQ8ERERERGRa+Tg6kpGTg4HTp8mIyfHspixiIgUTQkoERERERGR65SRkWHvEEREygQloERERERERESkzDCbzfYO4aZxI/taCSgRERERERERKfVMJhMAaWlpdo7k5lHQ1wV9/29oEXIRERERERERKfWMRiOVKlUiPj4eADc3NwwGg52juj65ublkZmYC+ddV2pjNZtLS0oiPj6dSpUo3JEYloERERERERESkTKhatSqAJQlVVuXl5ZGTk4OjoyMODqV3clqlSpUsff5vKQElIiIiIiIiImWCwWCgWrVq+Pr6kp2dbe9wrlt6ejqHDh3C398f11K6i6bJZLqho7OUgBIRERERERGRMsVoNJbKqWvFlZeXB4CzszMuLi52jsY2Su84LxERERERERERKReUgBIRERERERERkRKlBJSIiIiIiIiIiJQog9lsNts7iLLi559/xmw24+TkZO9Q/hWz2Ux2djYmk6nMbllZFqifbUd9bTvqa9tRX9uG+tl21Ne2o762HfW17aivbUP9bDvlpa+zsrIwGAw0a9bsqnW1CPk1KMsviosZDIYyn0QrC9TPtqO+th31te2or21D/Ww76mvbUV/bjvradtTXtqF+tp3y0tcGg6HYuRKNgBIRERERERERkRKlNaBERERERERERKREKQElIiIiIiIiIiIlSgkoEREREREREREpUUpAiYiIiIiIiIhIiVICSkRERERERERESpQSUCIiIiIiIiIiUqKUgBIRERERERERkRKlBJSIiIiIiIiIiJQoJaBERERERERERKREKQElIiIiIiIiIiIlSgkoEREREREREREpUUpAlSORkZEEBQXZO4xyLzIyksDAwEJ/evXqZe/Qyo2CPm7Tpg15eXmFygcMGEBgYCCTJk2yQ3TlW58+fQgMDGT37t1Wx3/44QcCAwP57bff7BRZ+VASr+3jx48TGBjI1q1bb2So5YJ+L9re9fS5/p+K73L3aLnxNm7cyAMPPEDz5s1p1qwZ3bt357nnniMxMfGa2tm3bx+RkZGkp6eXUKTlw8aNGxkwYABBQUEEBQXx0EMP8fHHH19XW5GRkfz88883NsAyrOC9x8CBAwuVvfLKK3Ts2NEOUZVPF39OrF+/Ps2bN6d37968/PLLHDx40N7hlQqO9g5ApCxycXFhxYoVhY7JjWMymUhOTubHH38kODjYcvzEiRPs2bMHNzc3O0ZXPh04cID9+/cDsGnTJu688047R1Q+3ejXtq+vL2vXrqV27do3OFIRKU10j7adqKgoZs+ezZAhQxg9ejRms5kDBw6wadMm4uPj8fb2LnZb+/btY968eQwcOBBXV9cSjLrsmjZtGqtXr+b+++9n5MiRGAwGtm3bxqRJk/jtt9+YMmXK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typbvHgx0dHRTJ48uVjXVBDH0qVL+d///kfr1q0ByMnJ4YsvvqB58+bFakNERETKNyWgRERERIrQpEkTFixYcMU6o0eP5oEHHiA0NJQHH3wQHx8fEhIS2LVrF3feeSe9evVi7ty5nD17lhYtWuDt7c2ff/7JN998w5AhQy7bbtu2bWnYsCHjx48nIiICd3d3Fi9eTMWKFa3qDRkyhA0bNvDEE08wYsQIMjMzefPNN6lWrRp9+/a9bPubN2/mzjvvpHPnzoXKzp8/z8iRI/n222+t1nS6kvbt29OkSRPGjx/PM888g4+PDytXriQ+Pp65c+cWqw0REREp35SAEhEREblOt9xyC+vXr+fNN9/kpZdeIi0tjSpVqnDXXXcRGBgI5I9mWrFiBZ9++innz5+natWqhIaGMmLEiMu2azAYWLBgAVOnTuWFF17Aw8ODQYMGkZCQwPbt2y31qlWrxsqVK5k5cyYRERE4ODjQqlUrJk2aVChZVWDv3r0cPnyY0NDQIsvbtm2Ll5cXmzZtKnYCymg0snjxYmbOnMnrr79OWloaDRs2ZNmyZTRq1KhYbYiIiEj5ZjCbzWZ7ByEiIiIiIiIiIuWXdsETEREREREREZESpQSUiIiIiIiIiIiUKCWgRERERERERESkRCkBJSIiIiIiIiIiJUoJKBERERERERERKVFKQImIiIiIiIiISIlSAkpEREREREREREqUElAiIiIiIiIiIlKilIASEREREREREZESpQSUiIiIiIiIiIiUKCWgRERERERERESkRCkBJSIiIiIiIiIiJer/ASZkWKVFjb9BAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Esse gráfico nos mostra mais uma vez e prova que essa queda provavelmente não decorre de uma questão sazonal e sim de um problema interno da empresa."
      ],
      "metadata": {
        "id": "Z7sn3xi-UAKH"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **8 - INSIGHTS FINAIS**\n"
      ],
      "metadata": {
        "id": "F5GHD-E2MfUk"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "--IiTRPAUI-V"
      }
    }
  ]
}