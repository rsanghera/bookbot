def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        character_count(file_contents)   

def character_count (file_contents):
    word_count = len(file_contents.split())
    ch_ct_dict = {}
    dict_list_convert = []
    ch_lw_cs = file_contents.lower()
    for ch in ch_lw_cs:
        if ch in ch_ct_dict and ch.isalpha():
            ch_ct_dict[ch] += 1
        elif ch not in ch_ct_dict and ch.isalpha():
            ch_ct_dict.update({ch:1})
    dict_list_convert = convert_list(ch_ct_dict)
    dict_list_convert.sort(reverse=True, key=sort_on)
    report_print(dict_list_convert, word_count)

def convert_list(ch_ct_dict):
    ch_ct_list = []
    for i,j in ch_ct_dict.items():
        this_tuple = {"character":i, "number":j}
        ch_ct_list.append(this_tuple)
    return ch_ct_list    

def sort_on(dict_list_convert):
    return dict_list_convert["number"]

def report_print(dict_list_convert, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} was found in the document")
    print(" ")
    for i in dict_list_convert:
        character = i.get("character")
        number = i.get("number")
        print(f"The '{character}' character was found {number} times")
    print("--- End report ---") 

main()