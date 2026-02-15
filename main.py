import sys

# Supponiamo che il nome sia passato come primo argomento
primo = sys.argv[0]
secondo=sys.argv[1] 
terzo= sys.argv[2]

"""
 Se esegui uno script con il seguente comando:

bash
Copy code
python script.py arg1 arg2 arg3
All'interno di script.py, sys.argv conterrà:

sys.argv[0]: "script.py" (o il percorso completo dello script)
sys.argv[1]: "arg1"
sys.argv[2]: "arg2"
sys.argv[3]: "arg3"
 """

# import logging
# import os
# import sys

# # Resetta la configurazione del logger
# for handler in logging.root.handlers[:]:
#     logging.root.removeHandler(handler)

    
# logging.basicConfig(
#     format="%(asctime)s.%(msecs)03d | %(levelname)s | %(name)s | %(funcName)s | line %(lineno)d | %(message)s",    datefmt="%Y-%m-%d %H:%M:%S",
#     level=os.environ.get("LOGLEVEL", "INFO").upper(),
#     filename="audit.log"
# )

# logger=logging.getLogger("Tranformation")

# logger.info("test")

from utility import   log_message

# _strFirst='\n'.join( f"  {Value} "  for  Value in sys.argv[1])
# _strSecond='\n'.join( f" {Value} "  for Value in sys.argv[2] )

log_message(f" Value: {sys.argv[0]}\n First[1]:  { sys.argv[1]} \n Second[2]: { sys.argv[2]} ")



name="test"
# Generiamo l'XML di output
xml_output = f"""
<MaltegoMessage>
    <MaltegoTransformResponseMessage>
        <Entities>
            <Entity Type="maltego.Person">
                <Value>John Doe</Value>
                <Weight>100</Weight>
                <AdditionalFields>
                      <Field Name="notes" DisplayName="Notes" MatchingRule="strict">
                       valore inventato uno
                    </Field>
                    <Field Name="email">john.doe@example.com</Field>
                </AdditionalFields>
                <Notes>
                    <Note>This is a note about John Doe.</Note>
                </Notes>
            </Entity>
              <Entity Type="maltego.Person">
                <Value>John Doe1</Value>
                <Weight>100</Weight>
                <AdditionalFields>
                      <Field Name="notes" DisplayName="Notes" MatchingRule="strict">
                            Valore inventato  due 
                    </Field>
                    <Field Name="email">john.doe@example.com</Field>
                </AdditionalFields>
                <Notes>
                    <Note>This is a note about John Doe.</Note>
                </Notes>
            </Entity>
        </Entities>
    </MaltegoTransformResponseMessage>
</MaltegoMessage>
"""

# Stampiamo l'output su stdout
print(xml_output)
# logger.info( f"quanti elementi in argv:  {len(sys.argv)} ")
# logger.info('\n'.join(f" Valore:  {valore} "   for   valore  in  sys.argv)   )