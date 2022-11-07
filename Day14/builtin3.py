# Example 3
familia = ['Baba','Mama','Kaka','Dada']
def herufi_kubwa(jina):
    return jina.upper()

jina_herufi_kubwa = map(herufi_kubwa, familia)
print(list(jina_herufi_kubwa))

# Using lambda function
jina_herufi_kubwa = map(lambda jina: jina.upper(), familia)
print(list(jina_herufi_kubwa))
