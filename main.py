import uu

def binary_to_text(filename):
    with open(filename, 'rb') as file:
        uu.decode(file, filename + '.txt')

binary_to_text('binary_file.uu')
