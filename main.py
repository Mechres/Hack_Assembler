import parser
import symbol_table
import code_module as code


def assemble(input_file, output_file):
    # 1. Pass
    parser.constructor(input_file)
    rom_adress = 0

    while parser.hasMoreCommands():
        parser.advance()
        ctype = parser.commandType()
        if ctype == "L_COMMAND":
            symbol = parser.symbol()
            if not symbol_table.contains(symbol):
                symbol_table.addEntry(symbol, rom_adress)
        else:
            rom_adress += 1
    
    # 2.Pass
    parser.constructor(input_file)
    ram_adress = 16
    output_lines = []

    while parser.hasMoreCommands():
        parser.advance()
        ctype = parser.commandType()

        if ctype == "A_COMMAND":
            symbol = parser.symbol()
            if symbol.isdigit():
                adress = int(symbol)
            else:
                if not symbol_table.contains(symbol):
                    symbol_table.addEntry(symbol, ram_adress)
                    ram_adress += 1
                adress = symbol_table.getAdress(symbol)
            binary = "0" + format(adress, "015b")
            output_lines.append(binary)
        elif ctype == "C_COMMAND":
            d = parser.dest()
            c = parser.comp()
            j = parser.jump()
            binary = "111" + code.comp(c) + code.dest(d) + code.jump(j)
            output_lines.append(binary)
        
        # çıktıyı dosyaya yaz
        with open(output_file, "w") as f:
            for line in output_lines:
                f.write(line + "\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Kullanım: python main.py Prog.asm Prog.hack")
    else:
        assemble(sys.argv[1], sys.argv[2])