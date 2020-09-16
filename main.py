from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.fairdb'
db = SQLAlchemy(app)

class FairModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(10))
    latitude = db.Column(db.String(10))
    setcens = db.Column(db.String(15))
    areap = db.Column(db.String(13))
    coddist = db.Column(db.String(9))
    distrito = db.Column(db.String(18))
    codsubpref = db.Column(db.String(2))
    subpref = db.Column(db.String(25))
    regiao5 = db.Column(db.String(6))
    regiao8 = db.Column(db.String(7))
    nome_feira = db.Column(db.String(30))
    registro = db.Column(db.String(6))
    logradouro = db.Column(db.String(34))
    numero = db.Column(db.String(5))
    bairro = db.Column(db.String(20))
    referencia = db.Column(db.String(24))

    def __repr__(self):
        return (
            'Fair('
            f'id = {fair_id}, '
            f'longitude = {longitude}, '
            f'latitude  = {latitude}, '
            f'setcens = {setcens}, '
            f'areap = {areap}, '
            f'coddist = {coddist}, '
            f'distrito = {distrito}, '
            f'codsubpref = {codsubpref}, '
            f'subpref = {subpref}, '
            f'regiao5 = {regiao5}, '
            f'regiao8 = {regiao8}, '
            f'nome_feira = {nome_feira}, '
            f'registro = {registro}, '
            f'logradouro = {logradouro}, '
            f'numero = {numero}, '
            f'bairro = {bairro}, '
            f'referencia = {referencia}'
            ')'
        )

db.create_all()

fair_args = reqparse.RequestParser()
fair_args.add_argument('longitude', type=str, help='Longitude da localização do estabelecimento no território do Município, conforme MDC')
fair_args.add_argument('latitude', type=str, help='Latitude da localização do estabelecimento no território do Município, conforme MDC')
fair_args.add_argument('setcens', type=str, help='Setor censitário conforme IBGE')
fair_args.add_argument('areap', type=str, help='Área de ponderação (agrupamento de setores censitários) conforme IBGE 2010')
fair_args.add_argument('coddist', type=str, help='Código do Distrito Municipal conforme IBGE')
fair_args.add_argument('distrito', type=str, help='Nome do Distrito Municipal')
fair_args.add_argument('codsubpref', type=str, help='Código de cada uma das 31 Subprefeituras (2003 a 2012)')
fair_args.add_argument('subpref', type=str, help='Nome da Subprefeitura (31 de 2003 até 2012)')
fair_args.add_argument('regiao5', type=str, help='Região conforme divisão do Município em 5 áreas')
fair_args.add_argument('regiao8', type=str, help='Região conforme divisão do Município em 8 áreas')
fair_args.add_argument('nome_feira', type=str, help='Denominação da feira livre atribuída pela Supervisão de Abastecimento')
fair_args.add_argument('registro', type=str, help='Número do registro da feira livre na PMSP')
fair_args.add_argument('logradouro', type=str, help='Nome do logradouro onde se localiza a feira livre')
fair_args.add_argument('numero', type=str, help='Um número do logradouro onde se localiza a feira livre')
fair_args.add_argument('bairro', type=str, help='Bairro de localização da feira livre')
fair_args.add_argument('referencia', type=str, help='Ponto de referência da localização da feira livre')

page_args = reqparse.RequestParser()
page_args.add_argument('page', type=int, help='Page number')
page_args.add_argument('per_page', type=int, help='Number of registries per page')

fair_fields = {
    'id': fields.Integer,
    'longitude': fields.String,
    'latitude': fields.String,
    'setcens': fields.String,
    'areap': fields.String,
    'coddist': fields.String,
    'distrito': fields.String,
    'codsubpref': fields.String,
    'subpref': fields.String,
    'regiao5': fields.String,
    'regiao8': fields.String,
    'nome_feira': fields.String,
    'registro': fields.String,
    'logradouro': fields.String,
    'numero': fields.String,
    'bairro': fields.String,
    'referencia': fields.String,
}

paginated_fair_fields = {
    'page': fields.Integer,
    'pages': fields.Integer,
    'per_page': fields.Integer,
    'has_next': fields.Boolean,
    'has_prev': fields.Boolean,
    'items': fields.Nested({
        'id': fields.Integer,
        'longitude': fields.String,
        'latitude': fields.String,
        'setcens': fields.String,
        'areap': fields.String,
        'coddist': fields.String,
        'distrito': fields.String,
        'codsubpref': fields.String,
        'subpref': fields.String,
        'regiao5': fields.String,
        'regiao8': fields.String,
        'nome_feira': fields.String,
        'registro': fields.String,
        'logradouro': fields.String,
        'numero': fields.String,
        'bairro': fields.String,
        'referencia': fields.String
    })
}

class Fair(Resource):
    @marshal_with(fair_fields)
    def get(self, fair_id):
        fair = FairModel.query.filter_by(id=fair_id).first()
        if fair:
            return fair
        else:
            abort(404, message=f'Fair with ID {fair_id} does not exist.')

    @marshal_with(fair_fields)
    def post(self, fair_id):
        try:
            args = fair_args.parse_args()
            fair = FairModel(
                id=fair_id,
                longitude=args['longitude'],
                latitude=args['latitude'],
                setcens=args['setcens'],
                areap=args['areap'],
                coddist=args['coddist'],
                distrito=args['distrito'],
                codsubpref=args['codsubpref'],
                subpref=args['subpref'],
                regiao5=args['regiao5'],
                regiao8=args['regiao8'],
                nome_feira=args['nome_feira'],
                registro=args['registro'],
                logradouro=args['logradouro'],
                numero=args['numero'],
                bairro=args['bairro'],
                referencia=args['referencia'],
            )
            db.session.add(fair)
            db.session.commit()
            return fair, 201
        except:
            abort(409, message=f'Fair with ID {fair_id} already exists.')

    @marshal_with(fair_fields)
    def put(self, fair_id):
        args = fair_args.parse_args()
        fair = FairModel.query.filter_by(id=fair_id).first()
        if fair:
            for field in args:
                if args[field]:
                    setattr(fair, field, args[field])
            db.session.commit()

            return fair
        else:
            abort(404, message=f'Fair with ID {fair_id} does not exist.')

    def delete(self, fair_id):
        fair = FairModel.query.filter_by(id=fair_id).first()
        if fair:
            db.session.delete(fair)
            db.session.commit()
            return '', 204
        else:
            abort(404, message=f'Fair with ID {fair_id} does not exist.')

class FairList(Resource):
    @marshal_with(paginated_fair_fields)
    def get(self):
        args = page_args.parse_args()
        paginated_fairs = FairModel.query.paginate(
            page=args['page'],
            per_page=args['per_page'],
            max_per_page=20
        )
        return paginated_fairs

api.add_resource(Fair, '/fair/<int:fair_id>')
api.add_resource(FairList, '/fairs')

if __name__ == '__main__':
    app.run(debug=True)
