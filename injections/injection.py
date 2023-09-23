import inject

from irepositorys.irepository import IRepository
from repositorys.respository import FirestoreRepository


def ioc_config(binder):
    binder.bind(IRepository, FirestoreRepository())


def register_ioc():
    inject.configure(ioc_config)
