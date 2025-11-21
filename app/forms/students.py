from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    identification = StringField('Identificación')
    firstname = StringField('Nombres', validators=[DataRequired()])
    lastname = StringField('Apellidos', validators=[DataRequired()])
    gender = StringField('Sexo', validators=[DataRequired()])
    date_of_birth = DateField('Fecha de Nacimiento', format='%Y-%m-%d')
    phone = StringField('Teléfono')
    email = StringField('Correo Electrónico')
    address = StringField('Dirección')
    submit = SubmitField('Guardar')