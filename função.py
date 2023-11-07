
def query(nome):

    query_pq = '''
    
"Aqui vai a QUERY em SQL"


    '''
    query_pf = '''
"Aqui vai a segunda QUERY em SQL" 

'''

    if nome == 'pq':
        return query_pq
    
    elif nome == 'pf':
        return query_pf

def execucao(cursor,query):
    cursor.execute(query)
    return cursor.fetchall()
