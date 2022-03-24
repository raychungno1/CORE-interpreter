from error import IdDuplicateError


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
            return Id.identifiers[name]
