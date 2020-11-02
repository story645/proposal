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
        raise ValueError(f"Required encodings {required}")
    # check optional encodings 
    if not ((transforms.keys() - artist.required) 
            <= artist.optional):
        raise ValueError(f"Valid optional encodings: {optional}")

def validate_transforms(data, transforms):
    return all(tau.validate(data.FB.F[column]) 
               for (column, tau) in transforms.values())