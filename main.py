from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Actor 
import database_model

app =FastAPI()


#total
@app.get("/total_actors")
def total_actors(db:Session = Depends(get_db)):
    count = db.query(database_model.Actor).count()
    return f"Total actors:{count}"


#reading the data from the database
@app.get("/actors")
def get_actors(db:Session = Depends(get_db)):
    db_actors = db.query(database_model.Actor).all()
    return db_actors  

#getting an actor by id
@app.get("/actors/{id}")
def get_actors_id(id:int,db:Session = Depends(get_db)):
    db_actor = db.query(database_model.Actor).filter(database_model.Actor.actor_id == id).first()
    if db_actor:
        return db_actor
    else:
        return f"id-{id} not found"

#getting an actors by first-name
@app.get("/actors/first_name/{name}")
def get_actor_by_first_name(name : str,db:Session = Depends(get_db)):
    db_actor = db.query(database_model.Actor).filter(database_model.Actor.first_name == name).all()
    if db_actor:
        return db_actor
    else:
        return "Actor Not Found"
    
#printing all the actors with last-name
@app.get("/actors/last_name/{name}")
def get_actor_by_last_name(name:str, db: Session = Depends(get_db)):
    actor = db.query(database_model.Actor).filter(database_model.Actor.last_name == name).all()
    if actor:
        return actor
    else:
        return f"{name} not found"


#adding the actor
@app.post("/actors")
def create_actor(actor:Actor,db:Session = Depends(get_db)):
    db.add(database_model.Actor(**actor.model_dump()))
    db.commit()
    return actor


#updating the actor with id
@app.put("/actors/{id}")
def update_actor(id:int,actor:Actor,db:Session = Depends(get_db)):
    db_actor = db.query(database_model.Actor).filter(database_model.Actor.actor_id == id).first()
    if db_actor:
        db_actor.first_name = actor.first_name
        db_actor.last_name = actor.last_name
        db_actor.last_update = actor.last_update
        db.commit()
        return f"{id} updated"
    else:
        return "actor not found"


#deleting the actor by id
@app.delete("/actors/{id}")
def delete_actor(id:int,db:Session = Depends(get_db)):
    db_actor = db.query(database_model.Actor).filter(database_model.Actor.actor_id == id).first()
    if db_actor:
        db.delete(db_actor)
        db.commit()
        return f"{id} was Deleted"
    else:
        return "Actor Not Found"
    
@app.get("/actors/")
def get_actor(limit:int = 10,db:Session = Depends(get_db)):
    actor = db.query(database_model.Actor).limit(limit).all()
    return actor
    