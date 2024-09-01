import codecs


def delete_tags(file):
    while '<' in file:
        file_index = file[file.find('<'):file.find('>') + 1]
        file = file.replace(file_index, '')
    return file


def delete_empty_lines(file):
    lines = file.splitlines(keepends=True)
    lines = [line for line in lines if line.strip() != ""]
    return ''.join(lines)


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    html = delete_tags(html)

    html = delete_empty_lines(html)

    with codecs.open(result_file, 'w', encoding='utf-8') as file:
        file.write(html)


delete_html_tags("draft.html")
print('ok')
