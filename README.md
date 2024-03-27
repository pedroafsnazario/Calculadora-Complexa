# Calculadora-Complexa
<h1 align="center">TDE de Construção de Interpretadores.
Contexto: uma Calculadora Exótica, capaz de ler arquivos .txt

O Arquivo lê linha por linha e vai interpretando as linhas para encontrar expressões calculaveis.

O Código é capaz de realizar expressões simples a expressões mais complexas (expressões que contêm sub-expressões)

Além disso, possui duas funções:
-MEM: Ao declarar ele pela primeira vez no .txt, ele irá armazenar o valor declarado com ele em uma "memória", e nas próximas vezes que o MEM for chamado dentro de uma expressão, ele irá substituir o 'MEM' pelo valor que está na "memória".
-RES: Este daqui ao ser chamado dentro de uma expressão, o código irá substitui-lo pelo resultado da linha X que foi chamado (exemplo: se tivesse um 2 RES em uma expressão de soma, ele irá somar o resultado da SEGUNDA linha com o valor solicitado naquela expressão)</h1>
