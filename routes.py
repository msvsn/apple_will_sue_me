from flask import render_template, request, redirect, url_for, session
from math import sin, cos, tan, log, log10, e, pi, sinh, cosh, tanh, sqrt
import random

def init_routes(app):
    app.secret_key = 'your-secret-key'

    @app.route('/', methods=['GET', 'POST'])
    def calculator():
        if 'display' not in session:
            session['display'] = '0'
            session['previous'] = None
            session['operation'] = None
            session['reset_next'] = False

        if request.method == 'POST':
            current = session['display']
            button = request.form.get('button')

            if button in '0123456789':
                if session.get('reset_next', False):
                    session['display'] = button
                    session['reset_next'] = False
                else:
                    session['display'] = current + button if current != '0' else button

            elif button == '.':
                if '.' not in current:
                    session['display'] = current + '.'

            elif button in ['+', '-', '×', '÷']:
                session['previous'] = current
                session['operation'] = button
                session['reset_next'] = True

            elif button == '=':
                if session['operation'] and session['previous']:
                    try:
                        prev = float(session['previous'])
                        curr = float(current)
                        op = session['operation']

                        if op == '+':
                            result = prev + curr
                        elif op == '-':
                            result = prev - curr
                        elif op == '×':
                            result = prev * curr
                        elif op == '÷':
                            if curr == 0:
                                session['display'] = 'Cannot divide by zero'
                                session['previous'] = None
                                session['operation'] = None
                                return render_template('main.html', display=session['display'])
                            result = prev / curr

                        session['display'] = str(int(result)) if result.is_integer() else str(result)
                        session['previous'] = session['display']
                        session['operation'] = None
                    except:
                        session['display'] = 'Error'

            elif button == 'AC':
                session['display'] = '0'
                session['previous'] = None
                session['operation'] = None
                session['reset_next'] = False

            elif button == '+/-':
                try:
                    value = float(current)
                    session['display'] = str(-value)
                except:
                    session['display'] = 'Error'

            elif button == '%':
                try:
                    value = float(current)
                    session['display'] = str(value / 100)
                except:
                    session['display'] = 'Error'

            elif button == 'sin':
                try:
                    value = float(current)
                    session['display'] = str(sin(value))
                except:
                    session['display'] = 'Error'

            elif button == 'cos':
                try:
                    value = float(current)
                    session['display'] = str(cos(value))
                except:
                    session['display'] = 'Error'

            elif button == 'tan':
                try:
                    value = float(current)
                    session['display'] = str(tan(value))
                except:
                    session['display'] = 'Error'

            elif button == 'x²':
                try:
                    value = float(current)
                    session['display'] = str(value ** 2)
                except:
                    session['display'] = 'Error'

            elif button == '√':
                try:
                    value = float(current)
                    if value < 0:
                        session['display'] = 'Math Error'
                    else:
                        session['display'] = str(sqrt(value))
                except:
                    session['display'] = 'Error'

            elif button == 'ln':
                try:
                    value = float(current)
                    if value <= 0:
                        session['display'] = 'Math Error'
                    else:
                        session['display'] = str(log(value))
                except:
                    session['display'] = 'Error'

            elif button == 'π':
                session['display'] = str(pi)

            elif button == 'e':
                session['display'] = str(e)

            elif button == 'rand':
                session['display'] = str(random.random())

        return render_template('main.html', display=session['display'])