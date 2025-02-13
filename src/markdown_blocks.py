def markdown_to_blocks(markdown):
    blocks = []
    markdown_split = markdown.split("\n\n")
    for block in markdown_split:
        if block == "":
            continue
        block_lines = block.strip()
        blocks.append(block_lines)
            
    return blocks