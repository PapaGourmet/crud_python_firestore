from abstracts.classes import Product
from injections.injection import register_ioc
from services.respositoryService import respositoryService

# não alterem esses dados. não mexam neles. esses dados faze a 'inversão de
# responsabilidades' do sistema

register_ioc()
fire = respositoryService()

# troque esses dados pelos dados que façam significado em seu database
collectionName = 'teste'
documentId = 'VSi0uCbJQTpTmb2YNFqu'
product = Product('Nome', 20, 'VSi0uCbJQTpTmb2YNFqu')

# abre a conexão
# => service.service.conn()

# adicona uma objeto a uma coleção. Troque por seu prório objeto
# observação. Crie um objeto tipado e guarde-o em abstracts.classes
# se tiver dúvidas, pergunte ao chatgpt e ele te responderá como
# => fire.service.add(collectionName, product, documentId)

# busca todos os documentos pelo id
# => fire.service.getAll(collectionName)

# busca todos os documentos pelo id
# => fire.service.getByID(collectionName, documentId)

# deleta  o documento pelo id
# => fire.service.deleteByDocumentId(collectionName, documentId)

# atualiza o documento pelo id
# => fire.service.updateByDocumentId(collectionName, documentId, product)
