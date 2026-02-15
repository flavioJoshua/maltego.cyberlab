from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.template_dir.extensions import registry
from maltego_trx.maltego import UIM_TYPES, MaltegoMsg, MaltegoTransform



""" generico funziona con  qualsiasi  entity in input  """
@registry.register_transform(display_name="persontest-flavio", input_entity="maltego.DNSName",
                             description='Receive DNS name from the Client, and resolve to IP address.',
                             output_entities=["maltego.Phrase"])
class persontest(DiscoverableTransform):
    """
    Returns a phrase greeting a person on the graph.
    """

    @classmethod
    def create_entities(cls, request, response):
        

     
        person_name = getattr(request,'Value','nullo')
        response.addEntity(Phrase, "Hi %s,s nice to meet you!" % person_name)
