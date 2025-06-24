from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # For session tracking
CORS(app)

# In-memory data storage
polls = {}
votes = {}

@app.route('/')
def index():
    return render_template('index.html', polls=polls)

@app.route('/create', methods=['POST'])
def create():
    question = request.form.get('question')
    options = [request.form.get(f'option{i}') for i in range(1, 4)]

    if not question or not all(options):
        return "All fields are required.", 400

    poll_id = str(uuid.uuid4())
    polls[poll_id] = {
        'question': question,
        'options': {opt: 0 for opt in options}
    }
    votes[poll_id] = {}  # Track who voted
    return redirect(f'/poll/{poll_id}')

@app.route('/poll/<poll_id>')
def poll(poll_id):
    if poll_id not in polls:
        return "Poll not found", 404

    return render_template('poll.html', poll=polls[poll_id], poll_id=poll_id, error=None)

@app.route('/vote/<poll_id>', methods=['POST'])
def vote(poll_id):
    if poll_id not in polls:
        return "Poll not found", 404

    selected = request.form.get('option')
    if not selected:
        return render_template('poll.html', poll=polls[poll_id], poll_id=poll_id, error="Please select an option.")

    voter_id = session.get('voter_id') or str(uuid.uuid4())
    session['voter_id'] = voter_id

    if voter_id in votes[poll_id]:
        return "You have already voted!", 403

    # Record the vote
    if selected in polls[poll_id]['options']:
        polls[poll_id]['options'][selected] += 1
        votes[poll_id][voter_id] = selected
    else:
        return "Invalid option selected", 400

    return redirect(f'/results/{poll_id}')

@app.route('/results/<poll_id>')
def results(poll_id):
    if poll_id not in polls:
        return "Poll not found", 404
    return render_template('results.html', poll=polls[poll_id])

if __name__ == '__main__':
    app.run(debug=True)
