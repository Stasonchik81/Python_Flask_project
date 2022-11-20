from flask import Flask
from flask import render_template

app = Flask(__name__)

with open('mylists.txt', 'r', encoding="UTF-8") as file:
    my_list = list()
    for line in file.readlines():
        my_list.append(tuple(line.split()))
    # print(my_list)
list_ = my_list

@app.route("/")
def index():
    return render_template('base.html', name=list_)

if __name__ == "__main__":
    app.run()
