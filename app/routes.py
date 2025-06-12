
task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['GET', 'POST'])
def index():
    db = get_db_connection()
    cursor = db.cursor()
    
    if request.method == 'POST':
        task = request.form['task']
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()
        return redirect('/')
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    db.close()
    edit_task = None
    edit_id = request.args.get('edit_id')
    if edit_id:
        cursor = get_db_connection().cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (edit_id,))
        edit_task = cursor.fetchone()
    return render_template('index.html', tasks=tasks, edit_task=edit_task)

@task_bp.route('/delete/<int:id>')
def delete(id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()
    db.close()
    return redirect('/')


# Rota para atualizar tarefa (Update)
@task_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    db = get_db_connection()
    cursor = db.cursor()
    if request.method == 'POST':
        new_task = request.form['task']
        cursor.execute("UPDATE tasks SET task = %s WHERE id = %s", (new_task, id))
        db.commit()
        db.close()
        return redirect('/')
    else:
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
        task = cursor.fetchone()
        db.close()
        return render_template('index.html', tasks=[], edit_task=task)
