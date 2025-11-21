from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy import or_
from app.forms.students import StudentForm
from app.models import Student
from app.extensions.alchemy import alchemy as db
from app.extensions.turbo import turbo


students_bp = Blueprint('students', __name__, url_prefix="/students")


@students_bp.route('/', methods=['GET'])
def index():
    return render_template('pages/students/index.html')


@students_bp.route('/pagination', methods=['GET'])
def pagination():
    params = request.args.to_dict()

    query = Student.query.order_by(Student.id.desc())

    if params.get('filter[search]'):
        search = params.get('filter[search]')
        fullname = Student.firstname + ' ' + Student.lastname
        query = query.filter(
            or_(
                fullname.ilike(f'%{search}%'),
                Student.identification == search
            )
        )

    if params.get('filter[gender]'):
        query = query.filter_by(gender=params.get('filter[gender]'))

    page = request.args.get('page', 1, type=int)
    params.pop('page', None)
    students = query.paginate(per_page=10, page=page)

    return render_template('features/students/_table.html', 
        students=students, 
        params=params
    )


@students_bp.route('/create', methods=['GET'])
def create():
    form = StudentForm()
    return render_template('pages/students/create.html',
        form=form, 
        action=url_for('students.store')
    )


@students_bp.route('/store', methods=['POST'])
def store():
    form = StudentForm()

    if form.validate_on_submit():
        student = Student()
        student.identification = form.identification.data
        student.firstname = form.firtname.data
        student.lastname = form.lastname.data
        student.gender = form.gender.data
        student.date_of_birth = form.date_of_birth.data
        student.phone = form.phone.data
        student.email = form.email.data
        student.address = form.address.data
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('students.index'))

    render = render_template('features/students/_form.html', form=form, action=url_for('students.store'))
    return turbo.stream([
        turbo.update(render, 'student-create-form')
    ])


@students_bp.route('<int:id>/edit', methods=['GET'])
def edit(id:int):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    return render_template('pages/students/edit.html', 
        form=form, 
        action=url_for('students.update', id=id)
    )


@students_bp.route('<int:id>/update', methods=['POST'])
def update(id:int):
    form = StudentForm()

    if form.validate_on_submit():
        student = Student.query.get_or_404(id)
        student.identification = form.identification.data
        student.firstname = form.firstname.data
        student.lastname = form.lastname.data
        student.gender = form.gender.data
        student.date_of_birth = form.date_of_birth.data
        student.phone = form.phone.data
        student.email = form.email.data
        student.address = form.address.data
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('students.index'))

    render = render_template('features/students/_form.html', form=form, action=url_for('students.update'))
    return turbo.stream([
        turbo.update(render, 'student-create-form')
    ])


@students_bp.route('<int:id>', methods=['DELETE'])
def destroy(id:int):
    student = Student.query.get_or_404(id)
    return redirect(url_for('students.index'))
