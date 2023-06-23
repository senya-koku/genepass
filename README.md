# genepass

generating passward randomly!

----
# Install
`pip install genepass`

----
# Usage

```python
import genepass

#複数のパスワードをランダムで作成し提案してくれる
genepass.suggest_passwords()

#Default
genepass.suggest_passwords(suggest_num=10, security_level='strong',length=8, character_sets=None)

```

----
# Option
- suggest_num : int
    - Number of suggestion
    - allowed : 1-100(default:10)

- security_level : string
    - strong : DIGITS & CAPITAL_LETTER & SMALL_LETTER（default）
    - god    : DIGITS & CAPITAL_LETTER & SMALL_LETTER & SYMBOLS
    - custom : Under construction

- length : int
    -  Number of characters in the generated password
    - allowed : 4-32（default:8）

- character_sets : list or None
    - characters type you want need
        - DIGITS         : 数字
        - CAPITAL_LETTER : 大文字
        - SMALL_LETTER   : 小文字
        - SYMBOLS        : 記号

 
    ----
