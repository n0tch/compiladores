symbol_table = ['(', ')', ',', '.', '+', '*', ';', ':=', ':', '=']

keyword_table = ['Program', 'Var', 'real', 'Const', 'Begin', 'Read', 'Write', 'End']

def valid_symbol(symbol, line, column):
  if symbol.strip() in symbol_table:
    return True
  else:
    return False

def valid_keyword(keyword, line, column):
  if keyword.strip() in keyword_table:
    return True
  else:
    return False

def ended_command(line, position):
  if(line.strip().endswith(';')):
    return True
  else:
    print("missing ';' on line {} column {}".format(position, len(line) - 1))
    return False

def invalid_symbol(symbol, line, column):
  print("invalid symbol '{}' on line {} colunm {}".format(symbol.strip(), line, column))

def read_file():
  with open('progm1.txt') as f:
    for index, line in enumerate(f.readlines()):
      ended_command(line, index)
      for column, word in enumerate(line.split(' ')):
        is_keyword = valid_keyword(word, line, column)
        if(not is_keyword and not valid_symbol(word, line, column) or word.isalnum()):
          invalid_symbol(word, index, column)

if __name__ == '__main__':
  read_file()