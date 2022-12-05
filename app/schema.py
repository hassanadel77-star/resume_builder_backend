from marshmallow import Schema, fields
from marshmallow.validate import Length



class UserSchema(Schema):
    username = fields.String(required=True,validate=Length(min=1,max=50))
    password = fields.String(required=True,validate=Length(min=1,max=150))
    email = fields.Email(required=True)

class BasicInformationSchema(Schema):
    firstname = fields.String(required=True,validate=Length(min=1,max=50))
    lastname = fields.String(required=True,validate=Length(min=1,max=50))
    email = fields.Email(required=True)
    address = fields.String(required=True)

class WorkExperienceSchema(Schema):
    company = fields.String(required=True,validate=Length(min=1,max=150))
    location = fields.String(required=True,validate=Length(min=1,max=150))
    started_on = fields.Date(required=True)
    ended_on = fields.Date()
    title = fields.String(required=True)

class WorkExperienceListSchema(Schema):
    work_experience = fields.Nested(WorkExperienceSchema)

class EducationSchema(Schema):
    institution = fields.String(required=True,validate=Length(min=1,max=355))
    started_on = fields.Date(required=True)
    ended_on = fields.Date()
    eduction_level = fields.String(required=True)
    programe = fields.String(required=True)

class EducationListSchema(Schema):
    education = fields.Nested(EducationSchema)

class CertificateSchema(Schema):
    certification = fields.String(required=True,validate=Length(min=1,max=355))
    issue_date = fields.Date(required=True)
    expiration_date = fields.Date()
    organization = fields.String(required=True)

class CertificateListSchema(Schema):
    certificates = fields.Nested(CertificateSchema)