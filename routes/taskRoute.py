from flask import Blueprint
from controllers.taskController import index, add_task, create, view, update, delete

task = Blueprint('task', __name__)

task.route('/',methods=['GET'], strict_slashes=False)(index)
task.route('/add-task',methods=['GET'], strict_slashes=False)(add_task)
task.route('/create',methods=['POST'], strict_slashes=False)(create)
task.route('/view/<int:id>',methods=['GET'], strict_slashes=False)(view)
task.route('/update/<int:id>',methods=['GET','POST'], strict_slashes=False)(update)
task.route('/delete/<int:id>',methods=['POST','DELETE'], strict_slashes=False)(delete)