import numpy as np

def check_constraints(artist, transforms_keys):
    """
    required: set
        Encodings required by the artists
    optional: set
        Encodings the artist supports
    encodings:
        Set of encodings the datasource is providing
    """
    # check required encodings are there
    if not (artist.required <= transforms_keys):
        raise ValueError(f"Required encodings {artist.required}")
    # check optional encodings 
    if not ((transforms_keys - artist.required) 
            <= artist.optional):
        raise ValueError(f"Valid optional encodings: {artist.optional}")

def validate_transforms(fibers, transforms):
    # this is where could tie into GSOD
    for param, transform in transforms.items():
        if np.isscalar(transform):
            # check that input value is valid for the parameter,
            assert True
        else: 
            column, tau  = transform
            for col in np.atleast_1d(column):
                if not tau.validate(fibers[col]['monoid']):
                    raise ValueError(f"Invalid transform {tau} for {col}")

def convert_transforms(view, transforms, exclude=None):
    exclude = [] if exclude is None else exclude
    visual = {}
    for (param, value) in transforms.items():
        if param in exclude:
            continue
        if np.isscalar(value):
            visual[param] = value
        else:
            (var, tau) = value
            if isinstance(var, (str, bytes )):
                visual[param] = tau(view[var])
            else:
                visual[param] = [tau(view[v]) for v in var]

    return visual