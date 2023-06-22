import random

def create_random_password(length=8, security_level='strong'):
    """
    security_level:str
        説明条件を勝手に決める
        strong:英字(大小）、数字 （default）
        god:英字(大小）、数字、記号
        custom:なし（optionを自分で決める） #TODO
    
    length:int
        説明:桁数
        default:8
    """
    #構成要素の定義
    DIGITS = "0123456789"
    CAPITAL_LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SMALL_LETTER = "abcdefghijklmnopqrstuvwxyz"
    SYMBOLS = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    #inputの確認
    if not isinstance(length, int):
        raise TypeError("length must be an integer.")
    if not isinstance(security_level, str):
        raise TypeError("security_level must be an integer.")
    
    #処理
    if security_level=='custom':
        print('Under construction')
        
    elif security_level=='strong':
        #password生成
        pass_chars = DIGITS + CAPITAL_LETTER + SMALL_LETTER
        password = ''
        while not any(item in password for item in DIGITS) and not any(item in password for item in CAPITAL_LETTER) and not any(item in password for item in SMALL_LETTER):
            password = ''.join(random.choice(pass_chars) for x in range(length))
        
    elif security_level=='god':
        #password生成
        pass_chars = DIGITS + CAPITAL_LETTER + SMALL_LETTER + SYMBOLS
        password = ''
        while not any(item in password for item in DIGITS) and not any(item in password for item in CAPITAL_LETTER) and not any(item in password for item in SMALL_LETTER) and not any(item in password for item in SYMBOLS):
            password = ''.join(random.choice(pass_chars) for x in range(length))
    
    return password
