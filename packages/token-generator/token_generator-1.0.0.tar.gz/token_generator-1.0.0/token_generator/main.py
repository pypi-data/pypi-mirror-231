import os
from pathlib import Path

import typer
from PIL import Image
from rembg import remove
from typing_extensions import Annotated

app = typer.Typer()


class TokenGenerator:
    """Classe responsavel por gerar o token"""

    def __init__(self, input_path: str):
        """Inicialização da classe

        Args:
            input_path (str): caminho do arquivo de entrada que sera utilizado para gerar o token
        """
        self.input_path = input_path
        self.file_name = Path(input_path).stem
        self.path = Path(input_path).parent
        self.full_path = f'{self.path}/{self.file_name}'

    def remove_background(self):
        """Remove o background da imagem e salva o arquivo com nome <nome_da_imagem>-removed.png

        Returns:
            Image: imagem com o background removido
        """
        outputted_file_path = f'{self.full_path}-removed.png'

        image = Image.open(self.input_path)
        image_bg_removed = remove(image)
        image_bg_removed.save(outputted_file_path, 'PNG')

        return image_bg_removed

    def _resize_image(self, image_bg_removed: Image):
        """Método privado. Redimensiona a imagem para 256x256 e salva o arquivo com nome <nome_da_imagem>-resized.png

        Args:
            image_bg_removed (Image): Imagem com background removido apenas para ser redimensionada

        Returns:
            Image: Imagem redimensionada
        """
        image_bg_removed_resized = image_bg_removed.resize((256, 256))
        image_bg_removed_resized.save(f'{self.full_path}-resized.png', 'PNG')

        return image_bg_removed_resized

    def _add_token_to_image(self, image_bg_removed: Image):
        """Método privado. Adiciona a borda do token(arquivo 'border.png') à imagem e salva o arquivo com nome <nome_da_imagem>-token.png

        Args:
            image_bg_removed (Image): Imagem com background removido e redimensionada

        Returns:
            Image: Retorna a imagem com a borda do token, toda pronta para ser utilizada
        """
        border_path = os.path.join(os.path.dirname(__file__), 'border.png')
        border = Image.open(border_path)

        image_bg_removed_resized = self._resize_image(image_bg_removed)

        background = image_bg_removed_resized.convert('RGBA')
        overlay = border.convert('RGBA')

        background.paste(overlay, (0, 0), mask=overlay)
        background.save(f'{self.full_path}-token.png', 'PNG')

        return background

    def _clean_files(self):
        """Método privado. Remove os arquivos temporários criados durante a execução do script"""
        Path(f'{self.full_path}-resized.png').unlink()
        Path(f'{self.full_path}-removed.png').unlink()

    def create_token(self):
        """Método para criação do token. Chama os métodos necessários para gerar o token

        Returns:
            Image: Token criado e pronto para uso
        """
        print('Criando token...')
        image_bg_removed = self.remove_background()
        token = self._add_token_to_image(image_bg_removed)
        self._clean_files()

        return token


@app.command()
def token_generator(
    input_path: Annotated[
        str,
        typer.Argument(
            help='Caminho do arquivo de entrada junto com nome e extensão'
        ),
    ]
):
    """Gera token a partir de uma imagem, remove background, redimensiona(256x256) e adiciona a borda do token.
    Salva no mesmo caminho do arquivo de entrada com o nome <nome_da_imagem>-token.png

    Args:
        input_path (str): Caminho do arquivo de entrada junto com nome e extensão
    """
    token = TokenGenerator(input_path).create_token()

    print('Token criado com sucesso' if token else 'Erro')


@app.command()
def remove_background(
    input_path: Annotated[
        str,
        typer.Argument(
            help='Caminho do arquivo de entrada junto com nome e extensão'
        ),
    ]
):
    """Remove o background de uma imagem e transforma em .PNG.
    Salva no mesmo caminho do arquivo de entrada com o nome <nome_da_imagem>-removed.png
    Args:
        input_path (str): Caminho do arquivo de entrada junto com nome e extensão.
    """
    background_removed = TokenGenerator(input_path).remove_background()

    print('Background removido com sucesso' if background_removed else 'Erro')
