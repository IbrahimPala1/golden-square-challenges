def make_snippet(string):
    words = string.split(" ")
    if len(words) > 5:
        snippet = ' '.join(words[:5])
        return snippet + '...'
    else:
        return string 


