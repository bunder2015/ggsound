#This is a script which will convert everything after
#.segment "CODE" in ggsound.asm to asm6 and nesasm syntax to
#help save me time converting ggsound to asm6 and nesasm each
#time I make an update and to ensure that this is a less error
#prone process. I am still updating the headers manually. I'm
#not expecting anybody else to use this file or use it for converting
#any other program, as it is nowhere near exhaustive for converting
#from ca65 to asm6 and nesasm. Just feed in ggsound.asm to run it and
#it will spit out ggsound_asm6.asm and ggsound_nesasm.asm.

import os
import sys
import re

def main():
    if len(sys.argv) != 2:
        print("%s expects one argument: input_file" % (sys.argv[0]))

    input_file = sys.argv[1]
    file_name_without_ext = os.path.splitext(input_file)[0]
    asm6_output_file = file_name_without_ext + "_asm6.asm"
    nesasm_output_file = file_name_without_ext + "_nesasm.asm"

    lines = []
    with open(input_file) as f:
        lines = f.readlines()

    asm6 = []
    nesasm = []

    scope_depth = 0
    labels = []
    for line in lines:
        if line == "\n":
            asm6.append(line)
            nesasm.append(line)
            continue
        pattern = re.compile(".*;.*")
        if pattern.match(line):
            asm6.append(line)
            nesasm.append(line)
            continue
        pattern = re.compile(".*\.ifdef.*")
        if pattern.match(line):
            asm6.append(line.replace(".ifdef", "ifdef"))
            nesasm.append(line.replace(".ifdef", "  ifdef"))
            continue
        pattern = re.compile(".*\.else.*")
        if pattern.match(line):
            asm6.append(line.replace(".else", "else"))
            nesasm.append(line.replace(".else", "  else"))
            continue
        pattern = re.compile(".*\.endif.*")
        if pattern.match(line):
            asm6.append(line.replace(".endif", "endif"))
            nesasm.append(line.replace(".endif", "  endif"))
            continue
        pattern = re.compile(".*\.byte.*")
        if pattern.match(line):
            asm6_line = line.replace(".byte", ".db")
            nesasm_line = line.replace(".byte", ".db")
            nesasm_line = nesasm_line.replace("<", "low(")
            nesasm_line = nesasm_line.replace(">", "high(")
            nesasm_line = nesasm_line.replace(",", "),")
            nesasm_line = nesasm_line.rstrip() + ")\n"
            asm6.append(asm6_line)
            nesasm.append(nesasm_line)
            continue
        pattern = re.compile(".*\.word.*")
        if pattern.match(line):
            asm6.append(line.replace(".word", ".dw"))
            nesasm.append(line.replace(".word", ".dw"))
            continue
        if line.startswith(".proc"):
            scope_depth += 1
            split_line = line.strip().split(" ")
            asm6.append("%s:\n" % split_line[1])
            nesasm.append("%s:\n" % split_line[1])
            continue
        if line.startswith(".endproc"):
            scope_depth -= 1
            continue
        pattern = re.compile(".*\.scope.*")
        if pattern.match(line):
            continue
        pattern = re.compile(".*\.endscope.*")
        if pattern.match(line):
            continue
        if line.startswith("    asl"):
            asm6.append("    %s a\n" % line.strip())
            nesasm.append("    %s a\n" % line.strip())
            continue
        pattern = re.compile("    [a-z][a-z][a-z]")
        if pattern.match(line):
            asm6.append(line)
            nesasm.append(line.replace("(", "[").replace(")", "]"))
            continue
        pattern = re.compile("[a-z0-9_]+:")
        if pattern.match(line):
            asm6_prefix = ""
            nesasm_prefix = ""
            if scope_depth > 0:
                asm6_prefix = "@"
                nesasm_prefix = "."
            asm6.append("%s%s" % (asm6_prefix, line))
            nesasm.append("%s%s" % (nesasm_prefix, line))
            labels.append(line[:-2])
            continue
        pattern = re.compile("[a-z0-9_]+ = [a-z0-9_]")
        if pattern.match(line):
            asm6.append(line)
            nesasm.append(line)
            continue
        asm6.append(line.strip() + " ;did not convert\n")
        nesasm.append(line.strip() + " ;did not convert\n")

    #Now look for usages of labels and get their prefixes in place
    for line in asm6:
        for label in labels:
            if label in line:
                pattern = re.compile("(    b.. .*)|(    jmp .*)")
                if pattern.match(line):
                    line.replace(label, "@%s" % label)
                else:
                    line = line.strip() + " ;erroneously detected label\n"
            
    with open(asm6_output_file, 'w') as f:
        for line in asm6:
            f.write(line)
    with open(nesasm_output_file, 'w') as f:
        for line in nesasm:
            f.write(line)

if __name__ == '__main__':
    main()
