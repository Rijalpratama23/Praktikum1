
# Diberikan string "keluar" dengan panjang 4, seperti "<<>>", dan sebuah kata, kembalikan string baru dengan kata tersebut berada di tengah-tengah string keluar, misalnya "<<kata>>".

# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]' , 'kata') → '[[kata]]'

def make_out_word(out, word):
    return out[:2] + word + out[:2]

#Tes cases 
print(make_out_word('<<>>', 'Yay'))    
print(make_out_word('<<>>', 'WooHoo'))  
print(make_out_word('[[]]', 'kata')) 