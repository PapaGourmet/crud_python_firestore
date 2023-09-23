

import os

import firebase_admin  # noqa
from firebase_admin import credentials, firestore  # noqa

from irepositorys.irepository import Any, IRepository, List, T


class FirestoreRepository(IRepository):
    def conn(self):
        path = os.path.dirname(os.path.dirname(__file__))
        key = os.path.join(path, 'key.json')
        cred = credentials.Certificate(key)
        firebase_admin.initialize_app(cred)

    def getAll(self, collectionName: str) -> List[Any]:
        db = firestore.client()
        ordens_ref = db.collection(collectionName)
        docs = ordens_ref.stream()
        data = []

        for doc in docs:
            data.append(doc.to_dict())

        return data

    def getByID(self, collectionName: str, documentId: str) -> Any:
        db = firestore.client()
        ref = db.collection(collectionName).document(documentId)
        result = ref.get()
        if ref:
            data = result.to_dict()
            print(data)
            return data
        else:
            return None

    def add(self, collectionName: str, document: T, documentId: None) -> None:
        obj = document.__dict__
        try:
            db = firestore.client()

            if documentId is not None:
                ref = db.collection(collectionName).document(documentId)
            else:
                ref = db.collection(collectionName).document()

            ref.set(obj)

        except Exception as e:
            print(str(e))

    def deleteByDocumentId(self, collectionName: str, documentId: str) -> None:  # noqa
        try:

            db = firestore.client()
            ref = db.collection(collectionName).document(documentId)

            if ref.get().exists:
                ref.delete()

        except Exception as e:
            print(str(e))

    def updateByDocumentId(self, collectionName, documentId, data) -> None:
        try:
            db = firestore.client()

            ref = db.collection(collectionName).document(documentId)

            if ref.get().exists:
                ref.update(data.__dict__)

        except Exception as e:
            print(str(e))
