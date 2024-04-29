from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

staff1 = 'john'
password1 = 'john@123'


def islogin():
    return staff1 in session


app.secret_key = "abc@123"

Student_list = [
    {'Name': 'Eswar', 'Age': 22, 'Rollno': 101, 'Marks': [90, 75, 80, 98, 75]},
    {'Name': 'Deva', 'Age': 21, 'Rollno': 102, 'Marks': [90, 75, 80, 88, 45]},
    {'Name': 'Siva', 'Age': 22, 'Rollno': 103, 'Marks': [90, 75, 80, 48, 95]},
    {'Name': 'Ruban', 'Age': 21, 'Rollno': 104, 'Marks': [90, 75, 80, 38, 35]},
    {'Name': 'Kiruba', 'Age': 22, 'Rollno': 105, 'Marks': [90, 85, 50, 98, 75]},
    {'Name': 'Halith', 'Age': 21, 'Rollno': 106, 'Marks': [90, 95, 90, 98, 75]},
    {'Name': 'Thenmozhi', 'Age': 22, 'Rollno': 107, 'Marks': [90, 75, 90, 98, 75]},
    {'Name': 'Abdul', 'Age': 21, 'Rollno': 108, 'Marks': [90, 75, 50, 98, 75]}
]

@app.route('/')
def navbar():
    return render_template('base.html')


@app.route('/staff/', methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        Name = request.form['name']
        Password = request.form['password']

        if Name == staff1 and Password == password1:
            return redirect(url_for('table'))
        else:
            return "invalid_credentials"
    return render_template('staff.html')


@app.route('/logout/')
def logout():
    session.pop("staff1",  None)
    return redirect(url_for('staff_login'))


@app.route('/table/', methods=['GET', 'POST'])
def table():
    if request.method == "POST":
        mark_list = []
        stu_dict = {}
        stu_dict['Name'] = request.form['Name']
        stu_dict['Age']= request.form['Age'] 
        stu_dict['Rollno']= request.form['Rollno']
        mark_list.append(request.form.get('sub1'))
        mark_list.append(request.form.get('sub2'))
        mark_list.append(request.form.get('sub3'))
        mark_list.append(request.form.get('sub4'))
        mark_list.append(request.form.get('sub5'))
        stu_dict['Marks'] = mark_list
        Student_list.append(stu_dict)
    return render_template('table.html', data=Student_list)



@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        mark_list = []
        stu_dict = {}
        stu_dict['Name'] = request.form['Name']
        stu_dict['Age']= request.form['Age'] 
        stu_dict['Rollno']= request.form['Rollno']
        mark_list.append(request.form.get('sub1'))
        mark_list.append(request.form.get('sub2'))
        mark_list.append(request.form.get('sub3'))
        mark_list.append(request.form.get('sub4'))
        mark_list.append(request.form.get('sub5'))
        stu_dict['Marks'] = mark_list

        Student_list.append(stu_dict)
        return redirect(url_for('table'))
    return render_template('add.html', data=Student_list)

@app.route('/edit/<string:id>', methods = ['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        edit_mark_list = []
        edit_value = Student_list[int(id)-1]
        Name = request.form.get('Name')
        Age = request.form.get('Age')
        Rollno = request.form.get('Rollno')
        edit_mark_list.append(request.form.get('sub1'))
        edit_mark_list.append(request.form.get('sub2'))
        edit_mark_list.append(request.form.get('sub3'))
        edit_mark_list.append(request.form.get('sub4'))
        edit_mark_list.append(request.form.get('sub5'))

        edit_value['Name'] = Name
        edit_value['Age'] = Age
        edit_value['Rollno'] = Rollno
        edit_value['Marks'] = edit_mark_list

        return redirect(url_for('table'))
    values = Student_list[int(id)-1]
    return render_template('edit.html', values = values)

@app.route("/delete<string:id>",methods=["GET","POST"])
def remove(id):
    Student_list.pop(int(id)-1)
    return redirect(url_for("table"))

if __name__ == ('__main__'):
    app.run(debug=True)
