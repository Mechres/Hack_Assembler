# Hack Assembler

## Overview
The Hack Assembler is a simple assembler for the Hack computer architecture. It translates assembly language code into machine code, allowing users to write programs in a human-readable format and convert them into a format that the Hack computer can execute.

## Features
- **Assembly to Machine Code Translation**: Converts Hack assembly language into binary machine code.
- **Symbol Table Management**: Handles symbols and labels in the assembly code.
- **Parser**: Parses the assembly code and prepares it for translation.

## Files
- `Add.asm`: Example assembly code file.
- `Add.hack`: Output machine code file generated from `Add.asm`.
- `code_module.py`: Contains the main logic for the assembler.
- `main.py`: Entry point for the assembler program.
- `parser.py`: Handles parsing of assembly code.
- `symbol_table.py`: Manages the symbol table for the assembler.

## Usage
1. Write your assembly code in a `.asm` file.
2. Run the assembler using the command:
   ```bash
   python main.py <your_file.asm> <output_file.hack>
   ```
3. The output will be a `.hack` file containing the machine code.

## Requirements
- Python 3.x

## Acknowledgments
- Nand2Tetris course.