def calculate_leftover_blocks(avail_blocks):
    blocks_remaining = avail_blocks
    layer_height = 1
    blocks_required = layer_height ** 2

    while blocks_remaining >= blocks_required:
        blocks_remaining -= blocks_required
        layer_height += 1
        blocks_required = layer_height ** 2

    return blocks_remaining

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True