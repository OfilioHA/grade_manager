from flask import Blueprint, render_template, redirect, url_for, request
from app.extensions.alchemy import alchemy as db
from app.extensions.turbo import turbo
from app.forms.courses import CourseForm


courses_bp = Blueprint('courses', __name__, url_prefix="/courses")


@courses_bp.route('/', methods=['GET'])
def index():
    return render_template('pages/courses/index.html')


@courses_bp.route('/pagination', methods=['GET'])
def pagination():
    params = request.args.to_dict()
    return render_template('features/courses/_table.html', params=params)


@courses_bp.route('/create', methods=['GET'])
def create():
    form = CourseForm()
    return render_template('pages/courses/create.html', 
        form=form,
        action=url_for('courses.store')
    )


@courses_bp.route('/store', methods=['POST'])
def store():
    form = CourseForm()

    if form.validate_on_submit():
        return redirect(url_for('courses.index'))
    
    render = render_template('features/courses/_form.html', 
        form=form,
        action=url_for('courses.store')
    )

    return turbo.stream([
        turbo.update(render, 'course-create-form')    
    ])


@courses_bp.route('/<int:id>/edit', methods=['GET'])
def edit(id:int):
    return render_template('pages/courses/edit.html', course_id=id)


@courses_bp.route('/<int:id>/update', methods=['POST'])
def update(id:int):
    return redirect(url_for('courses.index'))


@courses_bp.route('/<int:id>', methods=['DELETE'])
def destroy(id:int):
    return redirect(url_for('courses.index'))