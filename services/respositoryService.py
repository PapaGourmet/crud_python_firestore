import inject

from irepositorys.irepository import IRepository


class respositoryService():
    @inject.autoparams()
    def __init__(self, service: IRepository) -> None:
        self.service = service
