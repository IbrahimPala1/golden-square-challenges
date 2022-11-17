def reading_time(text):
    if len(text) == 0:
        raise Exception('Error')
    else:
        words = text.split(' ')
        result = len(words) / 200
        return result 