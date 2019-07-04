"""
======================================================================
BEFORE: contents.txt
======================================================================

1 INTRODUCING C 1

1.1 History of C 1
- Origins 1
- Standardization 2
- C-Based Languages 3

1.2 Strengths and Weaknesses of C 4
- Strengths 4
- Weaknesses 5
- Effective Use of C 6


2 C FUNDAMENTALS 9

2.1 Writing a Simple Program 9
- Program: Printing a Pun 9
- Compiling and Linking 10
- Integrated Development Environments 11

2.2 The General Form of a Simple Program 12
- Directives 12
- Functions 13
- Statements 14
- Printing Strings 14

...

======================================================================
AFTER: Create each chapter's directory & files from contents.txt
======================================================================

1 INTRODUCING C\1.1 History of C\1.1.1 Origins.txt
1 INTRODUCING C\1.1 History of C\1.1.2 Standardization.txt
1 INTRODUCING C\1.1 History of C\1.1.3 C-Based Languages.txt
1 INTRODUCING C\1.2 Strengths and Weaknesses of C\1.2.1 Strengths.txt
1 INTRODUCING C\1.2 Strengths and Weaknesses of C\1.2.2 Weaknesses.txt
1 INTRODUCING C\1.2 Strengths and Weaknesses of C\1.2.3 Effective Use of C.txt
2 C FUNDAMENTALS\2.1 Writing a Simple Program\2.1.1 Program - Printing a Pun.txt
2 C FUNDAMENTALS\2.1 Writing a Simple Program\2.1.2 Compiling and Linking.txt

...

"""

import os
import re

current: dict = {"main": "", "sub": "", "file": ""}
file_prefix_count: int = 0

# Read contents.txt
with open("contents.txt", "r") as contents:

    # Read each line in the text file
    for line in contents:

        # Remove page number
        line: str = re.sub(r"\d+$", "", line)
        # Remove leading and trailing whitespaces
        line = line.strip()

        if line != "":
            # Validate dir/file name
            line = re.sub(r"(\/)|(\&)", ", ", line)
            line = re.sub(r"(\: )|(\:) ", " - ", line)
            line = re.sub(r"(\<)", "[", line)
            line = re.sub(r"(\>)", "]", line)
            line = re.sub(r"(\")", "'", line)
            line = re.sub(r"(\*)", "x", line)

            last_sub: str = current["sub"]
            last_main: str = current["main"]
            last_file: str = current["file"]
            if re.match(r"\d+\.\d+", line):
                file_prefix_count = 0
                current["sub"] = line
            elif re.match(r"\d+", line):
                file_prefix_count = 0
                current["main"] = line
            else:
                file_prefix_count += 1
                file_prefix = re.search(r"(\d+\.\d+)", current["sub"]).group(1)
                file_prefix += f".{str(file_prefix_count)}"
                current["file"] = f"{file_prefix} {line[2:]}.txt"

            # Update file_path
            file_path: str = ""
            if current["main"] != last_main:
                file_path = current["main"]
            elif current["sub"] != last_sub:
                file_path = f"{current['main']}/{current['sub']}"
            elif current["file"] != last_file:
                file_path = f"{current['main']}/{current['sub']}/{current['file']}"

            # !!! BE CAREFUL! IF YOU ARE ABOUT TO EDIT BELOW PATH STRING, YOU MUST KNOW WHAT YOU ARE DOING NOW.
            # To locate all directories & files in the output folder
            output_path = "example/output"
            # output_path = "D:/OneDrive/ALL CODES/Study Notes/_Books_/C - KNK - C Programming A Modern Approach"
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            file_path = f"{output_path}/{file_path}"

            # Normalize path: eliminating double slashes, etc.
            os.path.normpath(file_path)

            # for Debugging
            print(file_path)

            # Notice 260 character path length
            assert (
                len(file_path) <= 256
            ), """

            << Assertion (to prevent FileNotFoundError caused by path length limit) >> 
            
            260 character path length limit is enabled in Windows!
            To disable it, follow below instruction.

            !!! BUT, BE CAREFUL! I DON'T RECOMMEND TO DO IT.
            Even if you disable it, some programs would raise some ERRORS! for example, Git doesn't support over 256 char path.
            
            1. Open regedit 
            2. Computer\\HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\FileSystem
            3. Enable LongPaths (change value from 0 to 1)
            4. Delete or Comment above assert statement

            """

            if re.search(r"\.txt$", file_path):
                try:
                    # Create directory (Even if the directory exists, don't raise exception.)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)

                    # Create text file with a whitespace.
                    with open(file_path, "w") as txt_file:
                        txt_file.write("")

                except FileNotFoundError as e:
                    print(e)
                    print(
                        """
                        
                        << Comment >> 
                        
                        Please check if the 'contents.txt' formats and characters are legal. (some special character could be hiding.
                        
                        """
                    )
