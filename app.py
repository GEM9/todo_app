from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    priority = request.form.get('priority')
    
    # Check if the priority is Custom, use a default value if not provided
    if priority == 'Custom':
        priority = request.form.get('custom_priority', 'Custom')

    if task and priority:
        tasks.append({'task': task, 'priority': priority})
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
