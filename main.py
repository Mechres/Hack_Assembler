import parser
import symbol_table
import code_module as code


def assemble(input_file, output_file, debug=False):
    # 1. Pass
    parser.constructor(input_file)
    rom_address = 0

    while parser.hasMoreCommands():
        parser.advance()
        ctype = parser.commandType()
        if ctype == "L_COMMAND":
            symbol = parser.symbol()
            if not symbol_table.contains(symbol):
                symbol_table.addEntry(symbol, rom_address)
        else:
            rom_address += 1
    
    # 2.Pass
    parser.constructor(input_file)
    ram_address = 16
    output_lines = []

    while parser.hasMoreCommands():
        parser.advance()
        ctype = parser.commandType()

        if ctype == "A_COMMAND":
            symbol = parser.symbol()
            if symbol.isdigit():
                address = int(symbol)
            else:
                if not symbol_table.contains(symbol):
                    symbol_table.addEntry(symbol, ram_address)
                    ram_address += 1
                address = int(symbol_table.getAddress(symbol))
            binary = "0" + format(address, "015b")
            output_lines.append(binary)
        elif ctype == "C_COMMAND":
            d = parser.dest()
            c = parser.comp()
            j = parser.jump()
            binary = "111" + code.comp(c) + code.dest(d) + code.jump(j)
            output_lines.append(binary)
        if debug:
            print("Parsing line:", parser.lines[parser.current_index])
            print("CommandType:", parser.commandType())
            print("Binary:", binary)
        # çıktıyı dosyaya yaz
        with open(output_file, "w") as f:
            for line in output_lines:
                f.write(line + "\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Kullanım: python main.py Prog.asm Prog.hack [debug]")
    else:
        debug = len(sys.argv) > 3 and sys.argv[3].lower() == "debug"
        assemble(sys.argv[1], sys.argv[2], debug=debug)