import emoji


emoji_input = input("Input: ")
emoji_output = emoji.emojize(emoji_input, language="alias")
print(f"Output: {emoji_output}")


