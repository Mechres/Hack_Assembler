
lines = []
current_index = -1

# Dosyayı aç yorumları ve boş satırları sil
def constructor(input):
    global lines, current_index
    with open(input) as f:
        lines = [line.split("//")[0].strip() for line in f.readlines()]
        lines = [line for line in lines if line != ""]
    current_index = -1

# Sonraki komut var mı kontrol et
def hasMoreCommands():
    global current_index, lines
    return current_index + 1 < len(lines)

# Sonraki komutu oku
def advance():
    global current_index, lines
    if hasMoreCommands():
        current_index +=1
        return lines[current_index]
    return None

# Komutun tipini belirle (A,C,L command)
def commandType():
    global current_index, lines
    cmd = lines[current_index]
    if cmd.startswith("@"):
        return "A_COMMAND"
    elif cmd.startswith("(") and cmd.endswith(")"):
        return "L_COMMAND"
    else:
        return "C_COMMAND"


def symbol():
    global current_index, lines
    cmd = lines[current_index]
    if commandType() == "A_COMMAND":
        # @Xxx -> Xxx
        return cmd[1:]
    elif commandType() == "L_COMMAND":
        # (Xxx) -> Xxx
        return cmd[1:-1]
    else:
        return None
    


def dest():
    global lines, current_index
    if commandType() != "C_COMMAND":
        return None
    
    cmd = lines[current_index]
    if "=" in cmd:
        return cmd.split("=")[0]
    return None

def comp():
    global lines, current_index
    if commandType() != "C_COMMAND":
        return None
    cmd = lines[current_index]
    if "=" in cmd:
        cmd = cmd.split("=")[1]
    if ";" in cmd:
        cmd = cmd.split(";")[0]
    return cmd

def jump():
    global lines, current_index
    if commandType() != "C_COMMAND":
        return None
    cmd = lines[current_index]
    if ";" in cmd:
        return cmd.split(";")[1]
    return None
