import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, create_app
from app.models import User,Post
app = create_app()
t   
@app.shell_context_processor
def hello():
    return {"sa":sa, "so":so, "db":db, "User":User, "Post":Post}