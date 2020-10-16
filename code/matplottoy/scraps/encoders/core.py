
def transform(single_bertan_variable_series : ArrayLike) -> ArrayLike:
    ...

def transform(x, y, singles_bertan_variable_series):
    ...

def transform(M, singles_bertan_verabile_series):
    ...

class MySN(SimpleNampsace):
    def __repr_html__(...):
        ...

    def __init__(self, validate, transform):
        super().__init__(validate, transform)

colorobj = SimpleNamespace(validate=f1, transfrom=f2)
colordict = {'validate': f1, 'transfrom': f2}

coleobj = NamedTuple('colorobj', ['validate', 'transform'])

#init/validate = info/meta <- mapping/encoding phase, needs to know if possible
#draw/transform = get('x') <- step to render /needs the things it needs to render
