from flask import Flask, render_template, request
import csv
import data_functions
app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def ask_data():

    if request.method == 'POST':
        file_name = "data_table.csv"
        datatable_list = data_functions.data_read(file_name)

        new_line = []
        new_line.append(data_functions.generate_id(datatable_list))
        new_line.append(request.form['story_title'])
        new_line.append(request.form['user_story'])
        new_line.append(request.form['acc_criteria'])
        new_line.append(request.form['business_value'])
        new_line.append(request.form['estim'])
        new_line.append(request.form['status'])

        datatable_list.append(new_line)

        data_functions.data_write(file_name, datatable_list)

        return render_template("list.html", html_datatable_list=datatable_list)
    else:
        return render_template("form.html")


@app.route('/story/<story_id>')
def update(story_id):
    return render_template('form.html', story_id=story_id)


@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def data_table():
    file_name = "data_table.csv"
    datatable_list = data_functions.data_read(file_name)
    return render_template("list.html", html_datatable_list=datatable_list)


if __name__ == '__main__':
    app.run()

