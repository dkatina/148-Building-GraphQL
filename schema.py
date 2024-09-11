import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, Director as DirectorModel, db
from sqlalchemy import select

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel #Creating our GraphQL Movie Object Type from our Sqlalchemy Movie Model

class Director(SQLAlchemyObjectType):
    class Meta:
        model = DirectorModel


class Query(graphene.ObjectType):
    movies = graphene.List(Movie) #Can query for a list of all movies
    search_movie = graphene.Field(Movie, id=graphene.Int()) #Returns individual movie
    search_director = graphene.Field(Director, id=graphene.Int())

    def resolve_movies(self, info): #Resolvers are functions that run when the query is called and are actually responsible for interacting with the db
        query = select(MovieModel)
        movies = db.session.execute(query).scalars().all()

        return movies
    
    def resolve_search_movie(self, info, id):
        movie = db.session.get(MovieModel, id)
        return movie
    
    def resolve_search_director(self, info, id):
        director = db.session.get(DirectorModel, id)
        return director

#================Movie Mutations ======================

class AddMovie(graphene.Mutation):
    class Arguments: #The arguments required to create a movie object
        title = graphene.String(required=True)
        year = graphene.Int(required=True)
        director_id = graphene.Int(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, title, director_id, year):
        movie = MovieModel(title=title, director_id=director_id, year=year)
        db.session.add(movie)
        db.session.commit()

        db.session.refresh(movie)
        return AddMovie(movie=movie)
    
class UpdateMovie(graphene.Mutation):
    class Arguments: #The arguments required to create a movie object
        id = graphene.Int(required=True)
        title = graphene.String(required=False)
        year = graphene.Int(required=False)
        director_id = graphene.Int(required=False)

    movie = graphene.Field(Movie)

    def mutate(self, info, id, title=None, director_id=None, year=None):
        movie = db.session.get(MovieModel, id)
        if  not movie:
            return None
        if title:
            movie.title = title
        if director_id:
            movie.director_id = director_id
        if year:
            movie.year = year

        db.session.add(movie)
        db.session.commit()

        db.session.refresh(movie)
        return UpdateMovie(movie=movie)
    
#===============Director stuff======================

class AddDirector(graphene.Mutation):
    class Arguments: #The arguments required to create a director object
        name = graphene.String(required=True)
        
    director = graphene.Field(Director)

    def mutate(self, info, name):
        director = DirectorModel(name=name)
        db.session.add(director)
        db.session.commit()

        db.session.refresh(director)
        return AddDirector(director=director)



class Mutation(graphene.ObjectType):
    create_movie = AddMovie.Field()
    update_movie = UpdateMovie.Field()
    create_director = AddDirector.Field()


