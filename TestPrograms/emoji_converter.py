def emoji_convert(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "☹️",
        ":O": "😱"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input(">")
print(emoji_convert(message))