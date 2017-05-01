from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def ask_data():

    if request.method == 'POST':
        new_line = []
        new_line.append('id')
        new_line.append(request.form['story_title'])
        new_line.append(request.form['user_story'])
        new_line.append(request.form['acc_criteria'])
        new_line.append(request.form['business_value'])
        new_line.append(request.form['estim'])
        new_line.append(request.form['status'])

        datatable_list = []
        with open("data_table.csv", "r") as data_table:
            for line in data_table:
                cut_line = line.replace("\n", "")
                line_list = cut_line.split(',')
                datatable_list.append(line_list)
        datatable_list.append(new_line)

        with open("data_table.csv", "w") as data_table_add:
            for item in datatable_list:
                line_to_csv = ','.join(item)
                data_table_add.write(line_to_csv + "\n")

        return render_template("list.html", html_datatable_list=datatable_list)
    else:
        return render_template("form.html")


@app.route('/story/<story_id>')
def update(story_id):
    return render_template('form.html', story_id=story_id)


@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def data_table():
    datatable_list = []
    with open("data_table.csv", "r") as data_table:
        for line in data_table:

            cut_line = line.replace("\n", "")
            line_list = cut_line.split(',')
            datatable_list.append(line_list)

    return render_template("list.html", html_datatable_list=datatable_list)


if __name__ == '__main__':
    app.run()

