
def stop_list_all():
    values = ['http://www.w3.org/2002/07/owl#Thing',
              'http://www.w3.org/2000/01/rdf-schema#label',
              'http://www.w3.org/2001/XMLSchema#string'
              'http://www.w3.org/2001/XMLSchema#float',
              'http://www.w3.org/2001/XMLSchema#integer',
              'http://www.w3.org/2002/07/owl#Class',
              'http://www.w3.org/2001/XMLSchema#string',
              'http://www.w3.org/2001/XMLSchema#float',
              'http://www.w3.org/2008/05/skos-xl#Label',
              'http://www.w3.org/ns/prov#used',
              'http://purl.org/dc/elements/1.1/identifier',
              'http://www.w3.org/ns/prov#Create',
              'http://www.w3.org/1999/02/22-rdf-syntax-ns#List',
              'http://www.arg.dundee.ac.uk/aif#I-node',
              'http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#String',
              'http://www.w3.org/2000/01/rdf-schema#literal',
              'http://www.w3.org/2002/07/owl#namedindividual',
              'http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#rfc5147string',
              'http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#rfc5147string',
              'http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#endindex',
              'http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#beginindex',
              'http://www.w3.org/2002/07/owl#ontology',
              'http://lemon-model.net/lemon#form',
              'http://www.w3.org/2001/xmlschema#nonnegativeinteger',
              'http://www.w3.org/2001/xmlschema#date']

    values_lower = list(map(str.lower, values))
    return values_lower