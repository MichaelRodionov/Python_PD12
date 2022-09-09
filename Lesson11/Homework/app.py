from flask import Flask, render_template, url_for, redirect, request
import utils as u

json_file = 'candidates.json'
app = Flask(__name__)
menu = [
    {'name': 'ID search', 'url': 'candidate'},
    {'name': 'Name search', 'url': 'name'},
    {'name': 'Skill search', 'url': 'skill'}
]


@app.route('/')
def all_candidates():
    candidates_list: list[dict] = u.load_candidates(json_file)
    return render_template('list.html', candidates_list=candidates_list, menu=menu, title='Main page')


@app.route('/candidate', methods=['GET', 'POST'])
def get_candidate():
    if request.method == 'POST':
        pk = request.form.get('id')
        return redirect(url_for('candidate_pk', pk=pk))
    return render_template('search_id.html', title='Search ID')


@app.route('/candidate/<int:pk>/')
def candidate_pk(pk):
    candidates_list: list[dict] = u.load_candidates(json_file)
    get_by_pk: dict = u.get_by_pk(candidates_list, int(pk))
    return render_template('candidate_pk.html', title=get_by_pk['name'], get_by_pk=get_by_pk)


@app.route('/skill/', methods=['POST', 'GET'])
def get_skill():
    if request.method == 'POST':
        skill = request.form.get('skill')
        return redirect(url_for('candidate_skill', skill=skill))
    return render_template('search_skill.html', title='Search skill')


@app.route('/skill/<skill>')
def candidate_skill(skill):
    candidates_list: list[dict] = u.load_candidates(json_file)
    candidate_by_skill: list[dict] = u.get_by_skill(candidates_list, skill)
    return render_template('candidate_skill.html', title=skill, candidate_by_skill=candidate_by_skill)


@app.route('/name/', methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('candidate_name', name=name))
    return render_template('search_name.html', title='Search name')


@app.route('/name/<name>')
def candidate_name(name):
    candidates_list: list[dict] = u.load_candidates(json_file)
    candidate_by_name: list[dict] = u.get_candidates_by_name(candidates_list, name)
    return render_template('candidate_name.html', title=name, candidate_by_name=candidate_by_name)


if __name__ == "__main__":
    app.run(debug=True)
