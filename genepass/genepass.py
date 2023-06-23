import random

def generate_random_password(security_level='strong',length=8, character_sets=None):
    """
    security_level:str
        explain：説明条件を勝手に決める
        options:
            - strong:英字(大小）、数字 （default）
            - god:英字(大小）、数字、記号
            - custom:なし（optionを自分で決める） 
    
    length:int
        explain:桁数
        default:8
        
    character_sets:list
        explain:パスワードを構成する要素を選択する
        default:none
        options:
            - DIGITS
            - CAPITAL_LETTER
            - SMALL_LETTER
            - SYMBOLS

    """
    #構成要素の定義
    DIGITS = "0123456789"
    CAPITAL_LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SMALL_LETTER = "abcdefghijklmnopqrstuvwxyz"
    SYMBOLS = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    valid_levels = ["strong", "god", "custom"]
    
    
    #inputの確認
    #型
    if not isinstance(length, int):
        raise TypeError("length must be an integer.")
    if not isinstance(security_level, str):
        raise TypeError("security_level must be an string.")
    #制約
    if not security_level in valid_levels:
        raise ValueError(f"Invalid security_level. Allowed values are: {', '.join(valid_levels)}.")
    if length < 4:
        raise ValueError("Invalid length.  length must be longer than 4.")
    if length > 32:
        raise ValueError("Invalid length.  length must be smaller than 32.")
    
    #処理
    if security_level=='custom':
        #制約条件
        if not isinstance(character_sets, list):
            raise TypeError("character_sets must be defined.")
        pass_chars = ''.join(character_sets)
        password = ''
        while not all(any(item in password for item in char_set) for char_set in character_sets):
            password = ''.join(random.choice(pass_chars) for x in range(length))

    elif security_level=='strong':
        #password生成
        character_sets = [DIGITS, CAPITAL_LETTER, SMALL_LETTER]
        pass_chars = ''.join(character_sets)
        password = ''
        while not all(any(item in password for item in char_set) for char_set in character_sets):
            password = ''.join(random.choice(pass_chars) for x in range(length))
        
    elif security_level=='god':
        #password生成
        character_sets = [DIGITS, CAPITAL_LETTER, SMALL_LETTER, SYMBOLS]
        pass_chars = ''.join(character_sets)
        password = ''
        while not all(any(item in password for item in char_set) for char_set in character_sets):
            password = ''.join(random.choice(pass_chars) for x in range(length))
    
    return password


def suggest_passwords(suggest_num=10, security_level='strong',length=8, character_sets=None):
    """
    suggest_num:int
        explain:提案数
        default:10
    """
    #制約
    if suggest_num < 1:
        raise ValueError("Invalid suggest_num.  suggest_num must be longer than 1.")
    if suggest_num > 100:
        raise ValueError("Invalid suggest_num.  suggest_num must be smaller than 100.")
    
    list_suggestions = []
    for i in range(suggest_num):
        list_suggestions.append(generate_random_password(security_level, length, character_sets))
        
        # TODO 
        """
        多様性を担保するためのチェックするコードが必要
        """
        
    return list_suggestions
