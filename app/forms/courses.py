from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, FieldList, FormField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Optional
from wtforms import ValidationError
from app.models.course import SourceType

class CourseTopicForm(FlaskForm):
    id = StringField('ID del Tema', render_kw={'readonly': True}) # For editing existing topics
    title = StringField('Título del Tema', validators=[DataRequired(), Length(max=255)])
    content_path = StringField('Ruta del Contenido', validators=[DataRequired(), Length(max=255)])

class CourseBibliographyForm(FlaskForm):
    id = StringField('ID de la Bibliografía', render_kw={'readonly': True}) # For editing existing bibliography entries
    title = StringField('Título de la Fuente', validators=[DataRequired(), Length(max=255)])
    source_type = SelectField('Tipo de Fuente', choices=[(tag.name, tag.value) for tag in SourceType], validators=[DataRequired()])
    source_value = StringField('Valor de la Fuente (URL o Ruta de Archivo)', validators=[DataRequired(), Length(max=255)])


class CourseForm(FlaskForm):
    title = StringField('Título del Curso', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Descripción del Curso', validators=[Optional(), Length(max=255)])
    status = BooleanField('Activo', default=True)
    support_file = FileField('Archivo de Soporte', validators=[Optional(), Length(max=255)])
    submit = SubmitField('Guardar')

    # Nested formns
    topics = FieldList(FormField(CourseTopicForm), min_entries=0, label='Temas del Curso')
    bibliographies = FieldList(FormField(CourseBibliographyForm), min_entries=0, label='Bibliografía del Curso')

    def validate_on_submit(self):
        # Custom validation to ensure at least one topic and one bibliography entry
        if not super().validate_on_submit():
            return False

        if not self.topics.entries:
            self.topics.errors.append("Debe añadir al menos un tema al curso.")
            return False

        if not self.bibliographies.entries:
            self.bibliographies.errors.append("Debe añadir al menos una entrada de bibliografía al curso.")
            return False

        return True