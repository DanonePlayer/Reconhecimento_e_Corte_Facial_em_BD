from PIL import Image


def remove_fundo_preto(imagem):
    # Carregue a imagem
    img = Image.open(imagem)

    # Converta a imagem para o modo RGBA (com canal alfa para transparência)
    img = img.convert("RGBA")

    # Obtenha os dados dos pixels da imagem
    pixels = img.getdata()

    # Crie uma nova lista de pixels com o fundo preto substituído por transparente
    nova_lista_pixels = []
    for pixel in pixels:
        r, g, b, a = pixel
        if r == 0 and g == 0 and b == 0:
            # Se for preto, defina a transparência como 0 (totalmente transparente)
            a = 0
        nova_lista_pixels.append((r, g, b, a))

    # Atualize a imagem com a nova lista de pixels
    img.putdata(nova_lista_pixels)

    # Salve a imagem com o fundo preto removido
    img.save("Olhos-M\Teste-1.png", "PNG")

# Exemplo de uso
remove_fundo_preto("Olhos-M\Teste-1.png")