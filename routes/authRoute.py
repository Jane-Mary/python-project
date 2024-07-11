from flask import Blueprint
from controllers.authController import login,register,login_user,register_user,logout


auth = Blueprint('auth', __name__)


auth.route('/login',methods=['GET'], strict_slashes=False)(login)
auth.route('/register',methods=['GET'], strict_slashes=False)(register)
auth.route('/login-user',methods=['POST'], strict_slashes=False)(login_user)
auth.route('/register-user',methods=['POST'], strict_slashes=False)(register_user)
auth.route('/logout',methods=['POST'], strict_slashes=False)(logout)
