from flask import Flask, request
from helpers import build_page

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def various_tasks():
    buff = ''
    form = '''
    <form method='POST'>
    <input name="n" placeholder="Podaj liczbę" type="number" step="1" />
    <input type="submit" value="Licz!" />
    </form>
    '''
    if request.method == 'POST':
        n = int(request.form['n'])
        some_power = 2 ** n
        more_power = n ** n
        fact = 1
        if n < 0:
            fact = 'Nie ma silni dla takiej liczby :('
        elif n >= 1:
            for i in range(1,n+1):
                fact *= i
        form += """<hr>Twoja liczba: {}<br>
        2<sup>{}</sup> = {}<br>
        {}<sup>{}</sup> = {}<br>
        {}! = {}
        """.format(n, n, some_power, n, n, more_power, n, fact)
    return build_page("Różne działania",form)

if __name__ == "__main__":
    app.run()



    def build_page(title, content):
        base = '''<html>
        <head>
            <title>{}</title>
        </head>
        <body>
            <h3>{}</h3>
            <hr/>
                {}
            <hr/>
            &copy;2020
        </body>
    </html>'''
        return base.format(
            title, title, content
        )l
