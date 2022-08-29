from flask import Flask, render_template
import functions as f

json_file = 'https://jsonkeeper.com/b/AN04'
app = Flask(__name__)


@app.route('/')
def all_candidates():
    candidates_list = f.load_candidates(json_file)
    return render_template('index.html', candidates_list=candidates_list)


@app.route('/candidate/<int:pk>')
def candidate_pk(pk):
    candidates_list = f.load_candidates(json_file)
    candidate_by_pk = f.get_by_pk(candidates_list, pk)
    return render_template('candidate_pk.html', title=candidate_by_pk['name'], candidate_by_pk=candidate_by_pk)


@app.route('/candidate/<skill>')
def candidate_skill(skill):
    candidates_list = f.load_candidates(json_file)
    candidate_by_skill = f.get_by_skill(candidates_list, skill)
    return render_template('candidate_skill.html', title=skill, candidate_by_skill=candidate_by_skill)


if __name__ == "__main__":
    app.run(debug=True)
