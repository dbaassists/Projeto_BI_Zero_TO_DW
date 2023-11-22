# Projeto BI Zero TO DW

### 10 - Notebook Externo

### SEQ-10.1 - Função Remove Acentuação

Essa função ela varre a coluna posição a posição em busca de caracter com acentos para poder substituir.

``` {.py3 title="Função Remove Acentuação" linenums=1}
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

Para conhecer melhor seu funcionamento, deixo o link de um vídeo do meu canal que explico com maiores detalhes [Vídeo Removendo Acentuação](https://www.youtube.com/watch?v=Vr3Hq0frAA8&t=68s).

### SEQ-10.2 - Função Cria Dados Dimensão Tempo

``` {.py3 title="Função Criação Dados Dimensão Tempo" linenums=1}
def cria_dimensao_tempo(data_inicial, data_fim, dias_acrescimo):

        inicio = data_inicial

        while data_inicial <= data_fim:
                v_id_tempo = str(data_inicial.strftime("%Y%m%d"))
                v_ano = data_inicial.year
                v_mes = data_inicial.month
                v_dia = data_inicial.day

                if inicio == data_inicial:

                        spark.sql(fr"""TRUNCATE TABLE gold.DIM_TEMPO""")

                data_inicial += dias_acrescimo

                spark.sql(fr"""
                        INSERT INTO gold.DIM_TEMPO 
                        (ID_TEMPO
                        ,DATA
                        ,ANO
                        ,MES
                        ,DIA
                        ,DATA_CADASTRO
                        ,DATA_ALTERACAO) 
                        VALUES (sha2(cast({v_id_tempo} AS VARCHAR(10)),256)
                                ,CAST({v_id_tempo} AS VARCHAR(10))
                                ,{v_ano}
                                ,{v_mes}
                                ,{v_dia}
                                ,from_utc_timestamp(now(),'GMT-3')
                                ,from_utc_timestamp(now(),'GMT-3')
                                );
                        """)

```