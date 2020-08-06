from ages import Dog, db
from flask import jsonify, redirect

def create_dog(name, age, breed, year):
    year = int(year)
    dog = Dog(name=name, breed=breed, age=age, year=year)
    db.session.add(dog)
    db.session.commit()
    return dog

def get_all_dogs():
    all_dogs = dog.query.all()
    if all_dogs:
        all_dogs = [dog.as_dict() for dog in all_dogs]
        return jsonify(all_dogs)
    else:
        return jsonify({'message' : 'No doggos found'})

def get_dog():
    dog = Dog.query.get(id)
    if dog: return jsonify(dog.as_dict())
    else: return jsonify(['message' : f'No doggos with id of {id}'])

def update_dog(id, name, breed, age, year):
    dog = dog.query.get(id)
    if dog:
        dog.name = name or dog.name
        dog.breed = breed or dog.breed
        dog.age = age or dog.age
        db.session.commit()
        return jsonify(dog.as_dict())
    else: return jsonify({'message' : f'No doggos with id of {id}'})

def destroy_dog(id):
    dog = Dog.query.get(id)
    if dog:
        db.session.delete(dog)
        db.session.commit()
        return redirect('/dogs')
    else: return jsonify({'message' : 'No dog with id: {id} to delete'})