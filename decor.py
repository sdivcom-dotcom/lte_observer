def delete_trash(input_string):
    if ':' in input_string:
        output_string = input_string.rsplit(':', 1)[0]
    else:
        output_string = input_string
    return output_string


def delete_simbol(input_string):
    input_string = input_string.decode('utf-8')
    input_string = input_string.replace(" ", "")
    output_string = input_string.replace("\n", "")
    return output_string