from documents.jurisdictions.india import IndiaJurisdiction

JURISDICTION_REGISTRY = {
    "IN": IndiaJurisdiction(),
}


def get_jurisdiction_engine(code: str):
    return JURISDICTION_REGISTRY.get(code)
 