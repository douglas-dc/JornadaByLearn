def calcular_media(notas):
  quantidade = len(notas) 
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno obteve média:', round(media, 2)) # round para arredondar o número (caso esteja no meio (5) arredonda sempre para o par mais próximo)
  verificar_aprovacao(media)                      # print(f'O aluno obteve média: {media:.2f}')  <= utilizando o f strings   
                                                  # print('O aluno obteve média: {:.2f}'.format(media))  <= outra forma de fazer

def verificar_aprovacao(media):
  if media >= 7:
    print('Aluno aprovado!')
  else:
    print('Aluno reprovado.')

calcular_media([8, 6, 7.5, 9])