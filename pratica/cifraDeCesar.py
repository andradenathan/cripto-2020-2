def encripta_mensagem(texto, shift = 3):
        mensagem = ""

        for i in range(len(texto)):
            letra = texto[i]

            if(letra.isupper()):
                mensagem += chr((ord(letra) + shift - 65) % 26 + 65)

            else:
                mensagem += chr((ord(letra) + shift - 97) % 26 + 97)

        return mensagem


def desencripta_mensagem(mensagem_encriptada, shift = 3):
    mensagem = ""
    for i in range(len(mensagem_encriptada)):
        letra = mensagem_encriptada[i]

        if (letra.isupper()):
            mensagem += chr((ord(letra) - shift - 65) % 26 + 65)

        else:
            mensagem += chr((ord(letra) - shift - 97) % 26 + 97)

    return mensagem

