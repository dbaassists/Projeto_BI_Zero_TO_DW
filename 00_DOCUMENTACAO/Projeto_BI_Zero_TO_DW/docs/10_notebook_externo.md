# Projeto BI Zero TO DW

### 10 - Notebook Externo

### SEQ-10.1 - Função Remove Acentuação

Essa função ela varre a coluna posição a posição em busca de caracter com acentos para poder substituir.

```
def acentuacao(var):
  De   = "áéíóúàèìòùâêîôûãõäëïöüçñÿýÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÇÑŸÝ"
  Para = "aeiouaeiouaeiouaoaeioucnyyAEIOUAEIOUAEIOUAOAEIOUCNYY"
  Return = ""
  count = 0

  try:
    while count < len(var):
      letra = var[count]
      indice = De.find(letra)
      count += 1
      if indice == -1:
        Return += letra
      else:
        Return += Para[indice]
  except:
    Return = ""
    
  return Return

spark.udf.register("acentuacao", acentuacao)
```