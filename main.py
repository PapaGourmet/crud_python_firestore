from abstracts.classes import Product
from injections.injection import register_ioc
from services.respositoryService import respositoryService

collectionName = 'teste'
documentId = 'VSi0uCbJQTpTmb2YNFqu'
product = Product('Nome', 20, 'VSi0uCbJQTpTmb2YNFqu')


register_ioc()
service = respositoryService()
service.service.conn()
service.service.updateByDocumentId(collectionName, documentId, product)
