def grammar(text):
    if text == '':
        raise Exception('Error')
    return text[-1] in '.?!' and text[0] == text[0].upper()
     