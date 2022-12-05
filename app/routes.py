from functools import wraps
from app import application, engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *
from flask import request, jsonify,make_response
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import Session
from flask_cors import CORS
import uuid
import datetime
from config import Config
import jwt
from .schema import  UserSchema, BasicInformationSchema,EducationListSchema,WorkExperienceListSchema,CertificateListSchema



CORS(application, support_credentials=True)
Base = automap_base()
Base.prepare(engine, reflect=True)
Accounts = Base.classes.account
Resume = Base.classes.resume
session = Session(engine)
metadata = MetaData(engine)




@application.route('/index')
@application.route('/')
def index():
    return 'Welcome to this page'


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'}),401
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user = session.query(Accounts).filter_by(public_id=data['public_id']).first()
        except Exception as ex:
            return jsonify({'message': "invalid token"}),401
    
        return f(current_user, *args, **kwargs)
    return decorator


@application.route('/register', methods=["POST"])
def register():
    data = request.get_json()
    validation_schema = UserSchema()
    try:
        validation_schema.load(data)
    except Exception as ex:
        return jsonify({'message':str(ex)}),400

    user = session.query(Accounts).filter(or_(Accounts.username == data.get("username") , Accounts.email==data.get("email"))).first()
    if user:
        return jsonify({'message':"User exists"}),400
        
    password_hash =  generate_password_hash(data['password'], method='sha256')
    account = Table('account', metadata, autoload=True)
    engine.execute(account.insert(), username=data.get("username"),
                   email=data.get("email"), password=password_hash , admin=False,public_id=str(uuid.uuid4()))
    return jsonify({'message': "registered successfully"})


@application.route('/login', methods=['POST']) 
def login_user():
   auth = request.authorization  
   if not auth or not auth.username or not auth.password: 
       return make_response('Missing credentials', 401, {'Authentication': 'login required"'})   
 
   user = session.query(Accounts).filter_by(username=auth.username).first()
   if user and check_password_hash(user.password, auth.password):
       token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, Config.SECRET_KEY, "HS256")
       return jsonify({'token' : str(token.decode("utf-8"))})

 
   return make_response('could not verify',  401, {'Authentication': '"login required"'})

@application.route('/basic_info', methods=["POST"])
@token_required
def add_basic_info(current_user):
    data = request.get_json()
    validation_schema = BasicInformationSchema()
    try:
        validation_schema.load(data)
    except Exception as ex:
        return jsonify({'message':str(ex)})

    resume_table = Table('resume', metadata, autoload=True)    
    resume = session.query(Resume).filter_by(public_id=current_user.public_id).first()

    if not resume:
        engine.execute(resume_table.insert(), public_id=current_user.public_id,data = {"basic_info" : data})
    else:
        updated_resume = resume.data 
        updated_resume.update({"basic_info" : data})
        engine.execute(resume_table.update(), public_id=current_user.public_id,data = updated_resume)

    return jsonify({"message" : "Basic info has been saved successfully"})



@application.route('/work_experience', methods=["POST"])
@token_required
def add_work_experience(current_user):
    data = request.get_json()
    print(data)
    validation_schema = WorkExperienceListSchema()
    try:
        validation_schema.load(data)
    except Exception as ex:
        return jsonify({'message': str(ex)}),400

    resume_table = Table('resume', metadata, autoload=True)    
    resume = session.query(Resume).filter_by(public_id=current_user.public_id).first()

    if not resume:
        engine.execute(resume_table.insert(), public_id=current_user.public_id,data = {"work_experience" : data})
    else:
        updated_resume = resume.data 
        updated_resume.update({"work_experience" : data})
        engine.execute(resume_table.update(), public_id=current_user.public_id,data = updated_resume)

    return jsonify({"message" : "Work experience has been saved successfully"})


@application.route('/education', methods=["POST"])
@token_required
def add_education(current_user):
    data = request.get_json()
    validation_schema = EducationListSchema()
    try:
        validation_schema.load(data)
    except Exception as ex:
        return jsonify({'message':str(ex)}),400

    resume_table = Table('resume', metadata, autoload=True)    
    resume = session.query(Resume).filter_by(public_id=current_user.public_id).first()

    if not resume:
        engine.execute(resume_table.insert(), public_id=current_user.public_id,data = {"education" : data})
    else:
        updated_resume = resume.data 
        updated_resume.update({"education" : data})
        engine.execute(resume_table.update(), public_id=current_user.public_id,data = updated_resume)

    return jsonify({"message" : "Education has been saved successfully"})


@application.route('/certificates', methods=["POST"])
@token_required
def add_certificates(current_user):
    data = request.get_json()
    validation_schema = CertificateListSchema()
    try:
        validation_schema.load(data)
    except Exception as ex:
        return jsonify({'message':str(ex)}),400

    resume_table = Table('resume', metadata, autoload=True)    
    resume = session.query(Resume).filter_by(public_id=current_user.public_id).first()

    if not resume:
        engine.execute(resume_table.insert(), public_id=current_user.public_id,data = {"certificates" : data})
    else:
        updated_resume = resume.data 
        updated_resume.update({"certificates" : data})
        engine.execute(resume_table.update(), public_id=current_user.public_id,data = updated_resume)

    return jsonify({"message" : "Certificates has been saved successfully"})

@application.route('/others', methods=["POST"])
@token_required
def add_others(current_user):
    data = request.get_json()
    resume_table = Table('resume', metadata, autoload=True)    
    resume = session.query(Resume).filter_by(public_id=current_user.public_id).first()

    if not resume:
        engine.execute(resume_table.insert(), public_id=current_user.public_id,data = {"others" : data})
    else:
        updated_resume = resume.data 
        updated_resume.update({"others" : data})
        engine.execute(resume_table.update(), public_id=current_user.public_id,data = updated_resume)

    return jsonify({"message" : "Others  has been saved successfully"})


@application.route('/resume', methods=["GET"])
@token_required
def get_resume(current_user):
    resume = session.query(Resume).filter_by(public_id=current_user.public_id).first()
    return jsonify({"data" : resume.data})


