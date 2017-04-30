from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def ask_data(story_id=None):
    datatable_list = []
    if request.method == 'POST':
        story_title = request.form['story_title']
        user_story = request.form['user_story']
        acc_criteria = request.form['acc_criteria']
        business_value = request.form['business_value']
        estim = request.form['estim']
        # Status
        datatable_list.append(story_title + ',' + user_story + ',' + acc_criteria + ',' + business_value + ',' + estim + '\n')
        with open("data_table.csv", "w") as data_table_add:
            for item in datatable_list:
                data_table_add.write(item)

        return render_template("list.html", html_list=datatable_list)
    else:
        return render_template("form.html", html_list=datatable_list)


@app.route('/story/<story_id>')
def update(story_id):
    return render_template('form.html', story_id=story_id)


@app.route('/list', methods=['GET'])
def data_table():
    datatable_list = []
    with open("data_table.csv", "r") as data_table:
        for line in data_table:
            datatable_list.append(line)
        
    return render_template("list.html", html_datatable_list=datatable_list)


#def get_table_from_file(file_name):
    #with open(file_name, "r") as file:
        #lines = file.readlines()
    #table = [element.replace("\n", "").split(";") for element in lines]
    #return table


if __name__ == '__main__':
    app.run()

