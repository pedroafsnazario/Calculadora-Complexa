#Projeto feito por: Pedro Antonio Fernandes dos Santos Nazário

def evaluate(expression, results):
  stack = []

  operators = set(['+', '-', '*', '/', '^', '|', '%', 'RES', 'MEM'])

  def memoria(memory_value, trigger):
    global memory

   
    memory = 0
    
    if trigger is True:
     memory = memory_value
    
    


  for token in expression.split():
      if token.isdigit():
          stack.append(int(token))
      elif token in operators:
          if token == 'RES':
              if len(stack) < 1:
                  raise ValueError("Expressão inválida")
              result_index = stack.pop()
              if result_index not in results:
                  raise ValueError(f"Resultado não encontrado para linha {result_index}")
              stack.append(results[result_index])



          elif token == 'MEM':



                if len(stack) >= 1:

                  memory_value = stack.pop()

                  memoria(memory_value, True)

            
                if len(stack) < 1:
                  if 'memory' not in globals():
                    stack.append(0)
                  else:  
                    stack.append(memory)


                
                  






          elif len(stack) < 2:
              raise ValueError("Expressão inválida")
          else: 

              operand2 = stack.pop()
              operand1 = stack.pop()
              if token == '+':
                  stack.append(operand1 + operand2)
              elif token == '-':
                  stack.append(operand1 - operand2)
              elif token == '*':
                  stack.append(operand1 * operand2)
              elif token == '/':
                  stack.append(operand1 // operand2)
              elif token == '|':
                  stack.append(operand1 / operand2)
              elif token == '^':
                  stack.append(operand1 ** operand2)
              elif token == '%':
                  stack.append(operand1 % operand2)

      else:
          raise ValueError("Token inválido: {}".format(token))

  if len(stack) != 1:
      raise ValueError("Expressão inválida")
  return stack[0]


# Função para ler e resolver expressões de um arquivo
def solve_from_file(file_path):
  results = {}
  
  with open(file_path, 'r') as file:

      line_number = 1

      for line in file:

          expression = line.strip()
          # Remover os parênteses
          expression = expression.replace('(', '').replace(')', '').replace(';', '')
          result = evaluate(expression, results)

          results[line_number] = result

          print(f"L{line_number}: {result}")

          line_number += 1


# Exemplo de uso
file_path = 'teste.txt'
solve_from_file(file_path)