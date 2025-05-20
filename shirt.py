# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

import sys
import os
from PIL import Image, ImageOps


end_list = [".jpg", ".jpeg", ".png"]

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        user_input = sys.argv[1]
        user_output = sys.argv[2]
        throw, user_input_file_extension = os.path.splitext(user_input)
        throw2, user_output_file_extension = os.path.splitext(user_output)

        if (user_input_file_extension in end_list) and (user_output_file_extension in end_list):
            if user_input_file_extension == user_output_file_extension:

                try:
                    user_before = Image.open(user_input)
                except FileNotFoundError:
                    sys.exit("Input does not exist")
                else:
                    shirt = Image.open("shirt.png")
                    altered_user = ImageOps.fit(user_before, size=(600, 600))
                    altered_user.paste(shirt, shirt)
                    altered_user.save(user_output)
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")


if __name__ == "__main__":
    main()
