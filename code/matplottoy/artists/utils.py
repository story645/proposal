import numpy as np
def check_constraints(artist, transforms):
    """
    required: set
        Encodings required by the artists
    optional: set
        Encodings the artist supports
    encodings:
        Set of encodings the datasource is providing
    """
    # check required encodings are there
    if not (artist.required <= transforms.keys()):
        raise ValueError(f"Required encodings {artist.required}")
    # check optional encodings 
    if not ((transforms.keys() - artist.required) 
            <= artist.optional):
        raise ValueError(f"Valid optional encodings: {artist.optional}")

def validate_transforms(fibers, transforms):
    for column, tau in transforms.values():
        for col in np.atleast_1d(column):
            if not tau.validate(fibers[col]['monoid']):
                raise ValueError(f"Invalid transform {tau} for {col}")

def convert_transforms(view, transforms, exclude=None):
    exclude = [] if exclude is None else exclude
    visual = {}
    for (t, (var, tau)) in transforms.items():
        if t in exclude:
            continue
        if isinstance(var, (str, bytes )):
            visual[t] = tau.convert(view[var])
        else:
            visual[t] = [tau.convert(view[v]) for v in var]
    return visual