# Passamos os valores pro python
key = "110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"
# Transforma em uma lista
list_key = key.split(' ')
# Converte de octal para decimal
decimal_key = [int(i, 8) for i in list_key]
# E agora convertemos este número decimal para uma letra, a partir da função chr()
asc_key = [chr(i) for i in decimal_key]
# Transforma a lista de palavras em uma string só
asc_key = ''.join(asc_key)
print(asc_key)