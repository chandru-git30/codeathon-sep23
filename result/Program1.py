def sort_by_freq(input_str):

    # Find frequency of each character
    freq = {}
    for ch in input_str:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    # Build output string    
    output_str = ''
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for ch, count in freq_sorted:
        output_str += ch * count
    
    return output_str

def test_sort_by_freq():
    assert sort_by_freq("hello world") == "llloohe wrd"
    assert sort_by_freq("tree") == "eetr"
    assert sort_by_freq("") == ""
    assert sort_by_freq("a") == "a"
    assert sort_by_freq("ababab") == "aaabbb"
    print("All test cases passed")

test_sort_by_freq()