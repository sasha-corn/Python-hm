def popular_words(text, words):
    text = text.lower().split()
    word_count = {}
    for word in words:
        word_count.setdefault(word, text.count(word))

    return word_count


popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
