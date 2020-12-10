from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError

from schemas.user import UserSchema


class InstructionSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(max=100)])
    description = fields.String(validate=[validate.Length(max=200)])
    steps = fields.List(fields.String())
    tools = fields.List(fields.String())
    cost = fields.Integer()
    duration = fields.Integer()
    is_publish = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data

    @validates('cost')
    def validate_cost(self, value):
        if value < 0:
            raise ValidationError('Cost cannot be less that 0.')

    @validates('duration')
    def validate_duration(self, value):
        if value < 1:
            raise ValidationError('Duration must be greater that 0.')
        if value > 500:
            raise ValidationError('Duration must be less that 500.')

    author = fields.Nested(UserSchema, attribute='user', dump_only=True,
                           only=['id', 'username'])


