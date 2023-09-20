import os
from pathlib import Path

import typer
from PIL import Image
from rembg import remove

app = typer.Typer()


class TokenGenerator:
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.file_name = Path(input_path).stem
        self.path = Path(input_path).parent
        self.full_path = f'{self.path}/{self.file_name}'

    def remove_background(self):
        outputted_file_path = f'{self.full_path}-removed.png'

        image = Image.open(self.input_path)
        image_bg_removed = remove(image)
        image_bg_removed.save(outputted_file_path, 'PNG')

        return image_bg_removed

    def _resize_image(self, image_bg_removed: Image):
        image_bg_removed_resized = image_bg_removed.resize((256, 256))
        image_bg_removed_resized.save(f'{self.full_path}-resized.png', 'PNG')

        return image_bg_removed_resized

    def _add_token_to_image(self, image_bg_removed: Image):
        border_path = os.path.join(os.path.dirname(__file__), 'border.png')
        border = Image.open(border_path)

        image_bg_removed_resized = self._resize_image(image_bg_removed)

        background = image_bg_removed_resized.convert('RGBA')
        overlay = border.convert('RGBA')

        background.paste(overlay, (0, 0), mask=overlay)
        background.save(f'{self.full_path}-token.png', 'PNG')

        return background

    def _clean_files(self):
        Path(f'{self.full_path}-resized.png').unlink()
        Path(f'{self.full_path}-removed.png').unlink()

    def create_token(self):
        print('Criando token...')
        image_bg_removed = self.remove_background()
        token = self._add_token_to_image(image_bg_removed)
        self._clean_files()

        return token


@app.command()
def token_generator(input_path: str):
    token = TokenGenerator(input_path).create_token()

    print('Token criado com sucesso' if token else 'Erro')
    

@app.command()
def remove_background(input_path: str):
    background_removed = TokenGenerator(input_path).remove_background()
    
    print('Background removido com sucesso' if background_removed else 'Erro')
