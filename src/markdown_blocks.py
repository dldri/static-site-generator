block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    markdown_split = markdown.split("\n\n")
    for block in markdown_split:
        if block == "":
            continue
        block_lines = block.strip()
        blocks.append(block_lines)
            
    return blocks

def block_to_block_type(block):
    #Check case for heading
    if (
            block.startswith("#")
            and block[block.count("#")] == " "
            and block.count("#") <= 6
    ):
        return block_type_heading
    
    #Check case for code
    if (
         block.startswith("```")
         and block.endswith("```")
    ):
        return block_type_code
    
    #Check case for quote and lists
    lines = block.split("\n")

    #quote
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return block_type_quote
    
    #unordered list
    is_unordered_list = True
    for line in lines:
        if not (
            line.startswith("* ")
            or line.startswith("- ")
        ):
            is_unordered_list = False
            break
    if is_unordered_list:
        return block_type_ulist
    
    #ordered lists
    is_ordered_list = True
    expected_number = 1
    for line in lines:
        if not (line.startswith(f"{expected_number}. ")):
            is_ordered_list = False
            break
        expected_number += 1
    if is_ordered_list:
        return block_type_olist
    
    return block_type_paragraph