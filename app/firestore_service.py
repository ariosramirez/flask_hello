import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1beta1.document import DocumentReference
from google.cloud.firestore_v1beta1.collection import CollectionReference

#from app.models import UserData


credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users() -> CollectionReference:
    return db.collection('users').get()


def get_user(user_id: str) -> DocumentReference:
    return db.collection('users').document(user_id).get()


def get_todos(user_id: str) -> CollectionReference:
    return (db.collection('users')
              .document(user_id)
              .collection('todos').get())


def put_user(user_data) -> None:
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def put_todo(user_id: str, description: str) -> None:
    todos_collection_ref = (db.collection('users')
                              .document(user_id)
                              .collection('todos'))
    todos_collection_ref.add({'description': description,
                              'done': False})


def delete_todo(user_id: str, todo_id: str) -> None:
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()


def update_todo(user_id: str, todo_id: str, done: bool) -> None:
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': todo_done})


def _get_todo_ref(user_id: str, todo_id: str) -> DocumentReference:
    return db.document(f"users/{user_id}/todos/{todo_id}")
