# genepass

generating passward randomly!

----
# Install
`pip install genepass`

----
# Usage

```python
import genepass

genepass.create_random_password()
```

----
# Option
- length
    - int : Number of characters in the generated password
    - allowed : 4-32（default:8）
- security_level
    - strong : DIGITS & CAPITAL_LETTER & SMALL_LETTER（default）
    - god    : DIGITS & CAPITAL_LETTER & SMALL_LETTER & SYMBOLS
    - custom : Under construction
 
 
    ----
