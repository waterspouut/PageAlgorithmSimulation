def fifo(reference_string, frame_count):
    frames = []
    result_texts = []
    for page in reference_string:
        if page in frames:
            result_texts.append(f"Data {page} is hit\n")
        elif len(frames) < frame_count:
            frames.append(page)
            result_texts.append(f"Data {page} is page fault\n")
        else:
            frames.pop(0)
            frames.append(page)
            result_texts.append(f"Data {page} migrates\n")
    return result_texts

def lru(reference_string, frame_count):
    pass 