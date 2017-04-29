from flask import Flask, render_template
app = Flask(__name__)


@app.route('/story')
def add_data():
    return render_template('form.html')


@app.route('/story/<story_id>')
def update(story_id):
    return render_template('form.html', story_id=story_id)


@app.route('/list')
def data_table():
    return render_template('list.html')


if __name__ == '__main__':
    app.run()