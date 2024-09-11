from flask import Flask
from models import db
import graphene
from schema import Query, Mutation
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:BAC146@localhost/graphql'

db.init_app(app)

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule( #Registering endpoint similar to creating a route
    '/graphql',
    view_func= GraphQLView.as_view('graphql', schema=schema, graphiql=True) #Setting graphiql as our UI
)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)