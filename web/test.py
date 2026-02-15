import sys

# Definisci un wrapper per il flusso di output
class MultiOutput:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, message):
        for stream in self.streams:
            stream.write(message)

    def flush(self):
        for stream in self.streams:
            stream.flush()

# Usa il wrapper MultiOutput per scrivere sia su console che su file
with open("output.txt", "w") as file:
    multi_out = MultiOutput(sys.stdout, file)
    sys.stdout = multi_out

    print("Questo messaggio viene scritto sia sulla console che nel file.")
    print("Un altro messaggio.")