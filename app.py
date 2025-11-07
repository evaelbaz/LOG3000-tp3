from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Cette fonction trouve  un opérande ainsi que sa position dans la chaine donnée. Elle calcule ensuite le résultat des
    chiffres à gauche et à droite de l'opérande, utilisant celui-ci pour l'opération mathématique.
    Args:
        expr (str): Une chaîne de caractères représentant une expression mathématique, par exemple "3+5", "10/2".

    Raises:
        ValueError: Si l'expression est vide, mal formée ou si les opérandes ne sont pas des nombres.

    Returns:
        float: Le résultat de l'opération mathématique."""
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Fonction exécuté lorsque la page est visitée avec une requête POST ou GET. Dans le cas d'un POST,
    l'expression mathématique est extraite et son résultat est calculé. Dans les deux cas, la page est ensuite construite et affichée.
    
    Returns:
        str: Le contenu HTML de la page, incluant le résultat du calcul ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)