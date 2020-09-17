from flask_restful import Resource, reqparse
from models.v1.fair import FairModel

class Fair(Resource):
    parser = reqparse.RequestParser()
    page_parser = reqparse.RequestParser()

    parser.add_argument('longitude', type=str, help='Longitude da localização do estabelecimento no território do Município, conforme MDC')
    parser.add_argument('latitude', type=str, help='Latitude da localização do estabelecimento no território do Município, conforme MDC')
    parser.add_argument('setcens', type=str, help='Setor censitário conforme IBGE')
    parser.add_argument('areap', type=str, help='Área de ponderação (agrupamento de setores censitários) conforme IBGE 2010')
    parser.add_argument('coddist', type=str, help='Código do Distrito Municipal conforme IBGE')
    parser.add_argument('distrito', type=str, help='Nome do Distrito Municipal')
    parser.add_argument('codsubpref', type=str, help='Código de cada uma das 31 Subprefeituras (2003 a 2012)')
    parser.add_argument('subpref', type=str, help='Nome da Subprefeitura (31 de 2003 até 2012)')
    parser.add_argument('regiao5', type=str, help='Região conforme divisão do Município em 5 áreas')
    parser.add_argument('regiao8', type=str, help='Região conforme divisão do Município em 8 áreas')
    parser.add_argument('nome_feira', type=str, help='Denominação da feira livre atribuída pela Supervisão de Abastecimento')
    parser.add_argument('registro', type=str, help='Número do registro da feira livre na PMSP')
    parser.add_argument('logradouro', type=str, help='Nome do logradouro onde se localiza a feira livre')
    parser.add_argument('numero', type=str, help='Um número do logradouro onde se localiza a feira livre')
    parser.add_argument('bairro', type=str, help='Bairro de localização da feira livre')
    parser.add_argument('referencia', type=str, help='Ponto de referência da localização da feira livre')


    page_parser.add_argument('page', type=int, help='Page number')
    page_parser.add_argument('per_page', type=int, help='Number of registries per page')

    def get(self, fair_id):
        fair = FairModel.find_by_id(fair_id)
        if fair:
            return fair.json()
        return {'message': 'Fair not found'}, 404

    def delete(self, fair_id):
        fair = FairModel.find_by_id(fair_id)
        if fair:
            fair.delete_from_db()
            return {'message': 'Fair has been deleted'}
        return {'message': 'Fair not found'}, 404

    def put(self, fair_id):
        data = Fair.parser.parse_args()
        fair = FairModel.find_by_id(fair_id)

        if fair:
            for field in data:
                if data[field]:
                    setattr(fair, field, data[field])
            fair.save_to_db()
            return fair.json()
        return {'message': 'Fair not found'}, 404


class FairList(Resource):
    def get(self):
        data = Fair.page_parser.parse_args()
        paginated_fairs = FairModel.query.paginate(
            page=data['page'],
            per_page=data['per_page'],
            max_per_page=20
        )

        items = list(map(
            lambda fair: fair.json(),
            paginated_fairs.items
        ))

        response = {
            'page': paginated_fairs.page,
            'total_pages': paginated_fairs.pages,
            'per_page': paginated_fairs.per_page,
            'has_next': paginated_fairs.has_next,
            'has_prev': paginated_fairs.has_prev,
            'items': items
        }

        return response

    def post(self):
        data = Fair.parser.parse_args()
        fair = FairModel(
            longitude=data['longitude'],
            latitude=data['latitude'],
            setcens=data['setcens'],
            areap=data['areap'],
            coddist=data['coddist'],
            distrito=data['distrito'],
            codsubpref=data['codsubpref'],
            subpref=data['subpref'],
            regiao5=data['regiao5'],
            regiao8=data['regiao8'],
            nome_feira=data['nome_feira'],
            registro=data['registro'],
            logradouro=data['logradouro'],
            numero=data['numero'],
            bairro=data['bairro'],
            referencia=data['referencia']
        )
        try:
            fair.save_to_db()
        except:
            return {'message': 'An error occurred inserting the fair'}, 500
        return fair.json(), 201
