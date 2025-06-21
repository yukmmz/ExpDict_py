
# %% import:
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# %% settings ------------------
LibtxtParentDir = 'txts'
n_print_extra_line = 2
###--------------------------



# %% get filepath list

LibtxtDirs = [d for d in os.listdir(LibtxtParentDir) if os.path.isdir(os.path.join(LibtxtParentDir, d))]
LibtxtDirs.append('.')
# print(f"Directories in '{LibtxtParentDir}': {LibtxtDirs}")

### for each dir, find txt files
Libtxt_paths = []
for d in LibtxtDirs:
    path_tmp = os.path.join(LibtxtParentDir, d)
    txt_files = [f for f in os.listdir(path_tmp) if f.endswith('.txt')]
    for txt_file in txt_files:
        relative_path = os.path.join(path_tmp, txt_file)
        Libtxt_paths.append(relative_path)

# for idx, path in enumerate(Libtxt_paths):
#     print(f"{idx}: {path}")





# %% main operation
while True:
    word_in = input("input word(:q->quit): ")
    if word_in == ":q": break
    if word_in == "": print('no input'); continue
    n_found = 0

    for i_lib, libpath in enumerate(Libtxt_paths):
        with open(libpath, 'r', encoding='UTF-8') as fileobject:
            try:
                contents = fileobject.readlines() # list of lines
            except UnicodeDecodeError:
                print(f'\n!!!!!!!\n{libpath} is not encoded in UTF-8')
            
            word = word_in.lower()
            # Word = word[0].upper() + word[1:] #capitalizeだと，"can i_lib help" -> "Can i_lib help" になる．
            # WORD = word.upper()
            flag_title = True
            linenum = len(contents)
            
            for i_line in range(linenum):
                if word in contents[i_line].lower():
                # if (word in contents[i_line]) or (Word in contents[i_line]) or (WORD in contents[i_line]):
                    n_found += 1
                    
                    if flag_title:
                        print(f'\n==========\n{libpath}')
                        flag_title = False 

                    ### lines before the line of interest
                    for i_ext in range(n_print_extra_line, 0, -1):
                        i_line_pr = i_line - i_ext
                        if i_line_pr >= 0:
                            if contents[i_line_pr] != "\n":
                                print(contents[i_line_pr], end='')

                    ### line of interest
                    highlighted_text = contents[i_line].replace(word, f"\033[31m{word}\033[0m")
                    print(f'>>{highlighted_text}', end='')
                    
                    ### lines after the line of interest
                    for i_ext in range(1, n_print_extra_line+1, 1):
                        i_line_pr = i_line + i_ext
                        if i_line_pr <= linenum - 1:
                            if contents[i_line_pr] != "\n":
                                print(contents[i_line_pr], end='')
                         
                    print('')

    print(f'\n---{n_found} found---\n')


print('end the program')

