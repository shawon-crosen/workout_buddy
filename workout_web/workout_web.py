from app import app, db
from app.models import User, Workout, Exercise

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Workout': Workout,
        'Exercise': Exercise
    }
