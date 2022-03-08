def read_file(file: str) -> str :
  with open(file, 'r') as buf:
    content = buf.read()
  
  return content
