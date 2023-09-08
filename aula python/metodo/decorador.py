import functools

def meu_decor(funcao):
    @functools.wraps(funcao)
        def fun_que_roda_funcao(): 
            print("********Embrulho funçao do decorador********")
            funcao()
            