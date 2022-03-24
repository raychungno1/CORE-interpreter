from error import IdDuplicateError, IdMissingError, IdUninitializedError


class Id:
    declaring = True
    identifiers = {}

    @staticmethod
    def add_id(name):
        if Id.declaring:
            if name in Id.identifiers:
                raise IdDuplicateError(name)

            Id.identifiers[name] = None

    @staticmethod
    def has_id(name):
        return (name in Id.identifiers)

    @staticmethod
    def set_id(name, val):
        if not(Id.declaring) and (name in Id.identifiers):
            Id.identifiers[name] = val

    @staticmethod
    def get_val(name):
        if not(Id.declaring) and (name in Id.identifiers):
            if Id.identifiers[name] is None:
                raise IdUninitializedError(name)
            return Id.identifiers[name]
