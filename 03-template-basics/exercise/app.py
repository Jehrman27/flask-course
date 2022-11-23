from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    username = request.args.get('username')
    lower_case = False
    upper_case = False
    end_num = False

    for x in username:
        if x.islower():
            lower_case = True
        if x.isupper():
            upper_case = True

    if username[-1].isnumeric():
        end_num = True

    report = lower_case and upper_case and end_num

    return render_template('report.html', report=report, lower_case=lower_case, upper_case=upper_case, end_num=end_num)


if __name__ == '__main__':
    app.run(debug=True)
