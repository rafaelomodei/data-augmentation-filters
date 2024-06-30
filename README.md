# Image Processing for Dataset Augmentation

Este projeto é uma ferramenta de processamento de imagens projetada para aumentar a base de dados de um dataset para treinamento de visão computacional. Ele aplica diferentes filtros a imagens em um diretório, criando variações que podem ser utilizadas para melhorar o desempenho de modelos de aprendizado de máquina.

## Funcionalidades

- **Filtro de Brilho**: Ajusta o brilho das imagens.
- **Filtro de Contraste**: Ajusta o contraste das imagens.
- **Filtro de Desfoque (Blur)**: Aplica um desfoque gaussiano às imagens.
- **Filtro de Saturação**: Aumenta ou diminui a saturação das cores nas imagens.

## Finalidade

O objetivo deste projeto é fornecer uma maneira fácil e eficiente de aumentar o dataset de treinamento para modelos de visão computacional. Ao aplicar diferentes filtros, você pode criar variações das imagens originais, melhorando a robustez e a generalização do modelo.

## Como Executar o Script

1. **Instale as dependências**:
   Certifique-se de que o `Pillow` esteja instalado. Use o seguinte comando:

    ```bash
        pip install Pillow
    ```
2. **Estrutura do Diretório**:
    Organize suas imagens em um diretório específico que será usado como fonte.

3. **Executar o Script**:

    Use o comando abaixo, substituindo os valores conforme necessário:Use o comando abaixo, substituindo os valores conforme necessário:
    ```bash
        python main.py --dir path/to/source_directory --filter <filter_type> --value <filter_value>
    ```
    --dir: Caminho para o diretório que contém as imagens originais.
    --filter: Tipo de filtro a ser aplicado (brightness, contrast, blur, saturation).
    --value: Valor do filtro (ajusta a intensidade do efeito).

4. **Exemplo de Uso:**:
    ```bash
        python main.py --dir images/originals --filter brightness --value 1.5
    ```
    Isso aplicará um filtro de brilho com valor 1.5 às imagens no diretório images/originals, salvando os resultados em um novo diretório com um nome que reflete o filtro e seu valor.

## Observações

Os arquivos processados serão salvos em um diretório no mesmo nível do diretório de entrada, com um nome no formato nome_original_tipo_de_filtro_valor.
Certifique-se de ajustar o valor do filtro para obter os resultados desejados.