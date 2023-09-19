
import xmlrpc.client
from flask_jwt_extended import create_access_token


class OdooAPI:
    cliente_id = 0
    cliente_nombre = ''

    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.common = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(
            self.db, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/object'.format(self.url))
        self.report = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/report'.format(self.url))

    def create_token(self, username, password):
        common = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(self.url))
        uid = common.authenticate(self.db, username, password, {})
        if uid:
            access_token = create_access_token(identity=uid)
        else:
            access_token = None

        return access_token

    def create_token_bot(self, username):
        domain = [['login', '=', username]]
        fields = ['id', 'name']

        result = self.search_read('res.users', domain, fields)
        if result:
            data = result[0]
            self.cliente_id = data['id']
            self.cliente_nombre = data['name']
            access_token = create_access_token(identity=self.cliente_id)
        else:
            access_token = None

        return access_token

    def search_read(self, model, domain, fields):
        ids = self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            'search',
            [domain]
        )
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            'read',
            [ids],
            {'fields': fields}
        )

    def create(self, model, params):
        """
            Metodo para crear registros
        :param model: Modelo Odoo donde crear
        :param params: dict, diccionario de campos
        :return: id del registro creado
        """
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            'create',
            [params]
        )

    def update(self, model, id, params):
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            'write',
            [[id], params]
        )

    def graba_mensaje(self, model, id, mensaje):
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            'message_post',
            [id],
            {'body': mensaje}
        )
