
def text_count(text):
    word_count = {}
    for soz in text.split():
        if soz in word_count:
            word_count[soz] += 1
        else:
            word_count[soz] = 1

    kop = 0
    word_key = ""
    for key, value in word_count.items():
        if value > kop:
            kop = value
            word_key = key

    return f"Textda eng ko'p '{word_key}' so'z {kop} marta takrorlandi."


def main():
    text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro maiores ab minus distinctio natus, quasi ex quod autem quis iste, rerum error perspiciatis id dolore! Harum, adipisci laborum. Eveniet, assumenda, aut unde culpa harum voluptatum necessitatibus provident, laudantium animi veniam dolores adipisci id atque numquam magnam minima fugit magni laboriosam totam alias tenetur. Repudiandae consectetur earum, dolore, quae minima aperiam architecto blanditiis, repellendus eius asperiores sed. Iste suscipit sit doloremque voluptatum consequatur, maiores saepe officia optio omnis tempora illum, in eum eveniet quaerat voluptate tenetur eius quisquam quo aliquid ad laborum laboriosam! Quam mollitia porro tenetur, dolorum consectetur corporis aspernatur?"

    result = text_count(text)
    print(result)

main()
