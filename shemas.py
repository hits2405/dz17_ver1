from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)  # dump_only=True это запрет на перезапись
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)          #fields.Nested(GenreSchema) прокидываем адрес до другой схемы
    director = fields.Nested(DirectorSchema)    #или fields.Pluck('DirectorSchema', 'name') типа вот только это поле

