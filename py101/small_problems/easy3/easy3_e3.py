# bannerizer
# write a function that takes a short line of text & prints it within a box

def display_divider():
    print('x' * 100)

def print_in_box(txt):
    width = len(txt)
    banner = f"+-{'-' * width}-+"
    empty_line = f"| {' ' * width} |"

    print(banner)
    print(empty_line)
    print(f"| {txt} |")
    print(empty_line)
    print(banner)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')

display_divider()

# further exploration; modify so it truncates message if it doesn't fit
# inside max width provided as second arg; assume no max if second arg omitted

def print_in_box2(txt, max_width=None, padding=2):
    width = len(txt) if max_width == None \
            or max_width >= len(txt) else max_width
    truncated = txt[:width] if width > 0 else ""

    pad_per_side = padding // 2
    def pad(chr, amt=pad_per_side):
        return chr * amt

    banner = f"+{pad('-')}{'-' * width}{pad('-')}+"
    empty_line = f"|{pad(' ')}{' ' * width}{pad(' ')}|"
    txt_line = f"|{pad(' ')}{truncated}{pad(' ')}|"

    print(banner)
    print(empty_line)
    print(txt_line)
    print(empty_line)
    print(banner)

print_in_box2('To boldly go where no one has gone before.')
print_in_box2('To boldly go where no one has gone before.', 0)
print_in_box2('To boldly go where no one has gone before.', 10)
print_in_box2('To boldly go where no one has gone before.', -20)
print_in_box2('To boldly go where no one has gone before.', 100)
print_in_box2('')
print_in_box2('', 0)
print_in_box2('', 10)
print_in_box2('', -20)
print_in_box2('', 100)

display_divider()

# bonus; try word-wrapping messages that are too long to fit

def chunk_strings(str_, width):
    str_chunks = []

    if width > 0:
        slice_start = 0
        slice_end = width
        while slice_start < len(str_):
            str_chunks.append(str_[slice_start:slice_end])
            slice_start = slice_end
            slice_end += width
  
    return str_chunks

# note: can chunk by splitting str into words & only add another word to a chunk
# when len(chunk) + len(word) <= max_width BUT have to decide how to handle cases
# where max_width < len(any word); len(longest word) == min_width needed for the
# longest word to have its own line/not be sliced through
def print_in_box_wrap(txt, max_width=None, padding=2):
    width = len(txt) if max_width == None \
            or max_width >= len(txt) else max_width
    str_list = chunk_strings(txt, width)

    pad_per_side = padding // 2
    def pad(chr, amt=pad_per_side):
        return chr * amt

    # NOT doing '-' * (width + padding) keeps padding independent
    # so even if width < 0, padding display will be preserved
    banner = f"+{pad('-')}{'-' * width}{pad('-')}+"
    empty_line = f"|{pad(' ')}{' ' * width}{pad(' ')}|"
    
    print(banner)
    print(empty_line)
    
    for line in str_list:
        right_pad = pad_per_side + (width - len(line))
        print(f"|{pad(' ')}{line}{pad(' ', right_pad)}|")

    print(empty_line)
    print(banner)

print_in_box_wrap('To boldly go where no one has gone before.')
print_in_box_wrap('To boldly go where no one has gone before.', 0)
print_in_box_wrap('To boldly go where no one has gone before.', 5)
print_in_box_wrap('To boldly go where no one has gone before.', 10)
print_in_box_wrap('To boldly go where no one has gone before.', 20)
print_in_box_wrap('To boldly go where no one has gone before.', -20)
print_in_box_wrap('To boldly go where no one has gone before.', 100)