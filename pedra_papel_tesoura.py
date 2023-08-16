import random

def play():
    user = input("Qual sua escolha: 'p' para pedra, 'l' para papel, 't' para tesoura: \n")
    computer = random.choice(['p','l','t'])
    
    if user == computer:
        return 'É um empate!'
    
    # p > t, t > l, l > p
    if is_win(user, computer):
        return 'Você venceu!'
    
    return 'Vocẽ perdeu!'
    
def is_win(player, opponent):
    # responde quem ganhou 
    # p > t, t > l, l > p
    if (player == 'p' and opponent == 't') or (player == 't' and opponent == 'l') or(player == 'l' and opponent == 'p'):
        return True

print(play())